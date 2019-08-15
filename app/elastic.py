from datetime import date, datetime, timedelta
import elasticsearch
import globalparams
import yaml


with open("config.yml", 'r') as file:
    config = yaml.load(file)


def create_elastic_conn():
    # create connection
    es = elasticsearch.Elasticsearch([config['elastic']['host']], port=config['elastic']['port'])
    return es


def parse_date():
    date_range = []
    if globalparams.es_input_data['elastic_time_range'][0] is not "*":
        start_date_ref = datetime.strptime(globalparams.es_input_data['elastic_time_range'][0], '%Y-%m-%d')
        start_date = date(start_date_ref.year, start_date_ref.month, start_date_ref.day)
        end_date_ref = datetime.strptime(globalparams.es_input_data['elastic_time_range'][1], '%Y-%m-%d')
        end_date = date(end_date_ref.year, end_date_ref.month, end_date_ref.day)
        delta = end_date - start_date
        for i in range(delta.days + 1):
            date_range.append((start_date + timedelta(days=i)).isoformat().replace('-', '.'))
    return date_range


def get_voshod_indices():
    es = create_elastic_conn()
    indices_dates = []
    for index in es.indices.get(config['elastic']['index'] + '*'):
        indices_dates.append(datetime.strptime(index[7:], '%Y.%m.%d'))
    indices_range = []
    indices_range.append('voshod-' + min(indices_dates).strftime('%Y.%m.%d'))
    indices_range.append('voshod-' + max(indices_dates).strftime('%Y.%m.%d'))
    return indices_range


def get_elastic_regress_result():
    es = create_elastic_conn()
    date_range = parse_date()
    queries_hash = []
    es_dict = {}
    if globalparams.es_input_data['elastic_time_range'][0] is not "*":
        index = 1
        for index_date in date_range:
            print(config['elastic']['index'] + index_date)
            # check conn
            try:
                es_conn_hits = es.search(index=config['elastic']['index'] + index_date, body={
                    "query": {
                        "bool": {
                            "must": [
                                # get only postgres logs
                                {"query_string": {
                                                    "fields": ["tags"],
                                                    "query": "postgres"
                                                }
                                },
                                # stand
                                {"terms": {
                                    "stand": globalparams.es_input_data['elastic_stand']
                                      }
                                 },
                                # database
                                {"terms": {
                                    "database": globalparams.es_input_data['elastic_database']
                                      }
                                 }
                                # comment out when elastic indexes change names
                                # {"match": {
                                #    "@timestamp": "2019-06-07"
                                #      }
                                # }
                                ],
                            # filter out query duration
                            "filter": {
                                "range": {
                                    "duration": {
                                        "gte": globalparams.es_input_data['elastic_duration'],
                                        "lte": 99999999
                                    }
                                }
                            }
                        }
                    }
                }, request_timeout=1)
                print("hits " + str(index) + " len = " + str(len(es_conn_hits)))
                for hit in es_conn_hits['hits']['hits']:
                    if hit["_source"]["statement_hash"] not in queries_hash:
                        es_dict[hit["_source"]["statement_hash"]] = {
                            'elastic_query_hash': hit["_source"]["statement_hash"],
                            'elastic_query_params': 'null',
                            'elastic_query_stand': hit["_source"]["stand"],
                            'elastic_query_database': hit["_source"]["database"],
                            'elastic_query_text': hit["_source"]["statement"],
                            'elastic_query_duration': hit["_source"]["duration"],
                            'elastic_query_date': hit["_source"]["pgtime"],
                            'elastic_query_transactionid': hit["_source"]["transactionID"]}
                        queries_hash.append(hit["_source"]["statement_hash"])
                    else:
                        if hit["_source"]["duration"] > es_dict[hit["_source"]["statement_hash"]]['elastic_query_duration']:
                            es_dict.pop(hit["_source"]["statement_hash"])
                            es_dict[hit["_source"]["statement_hash"]] = {
                                'elastic_query_hash': hit["_source"]["statement_hash"],
                                'elastic_query_params': 'null',
                                'elastic_query_stand': hit["_source"]["stand"],
                                'elastic_query_database': hit["_source"]["database"],
                                'elastic_query_text': hit["_source"]["statement"],
                                'elastic_query_duration': hit["_source"]["duration"],
                                'elastic_query_date': hit["_source"]["pgtime"],
                                'elastic_query_transactionid': hit["_source"]["transactionID"]}
                    index += 1
            except elasticsearch.ConnectionError:
                print("ES connection error")
        print("LEN: " + str(len(es_dict)))
    return es_dict


es_dict = get_elastic_regress_result()
