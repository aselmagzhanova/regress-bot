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
        start_date_ref = datetime.strptime(globalparams.es_input_data['elastic_time_range'][0], '%m/%d/%Y')
        start_date = date(start_date_ref.year, start_date_ref.month, start_date_ref.day)
        end_date_ref = datetime.strptime(globalparams.es_input_data['elastic_time_range'][1], '%m/%d/%Y')
        end_date = date(end_date_ref.year, end_date_ref.month, end_date_ref.day)
        delta = end_date - start_date
        for i in range(delta.days + 1):
            date_range.append((start_date + timedelta(days=i)).isoformat().replace('-', '.'))
    return date_range


def get_elastic_regress_result():
    es = create_elastic_conn()
    date_range = parse_date()
    es_dict = {}
    if globalparams.es_input_data['elastic_time_range'][0] is not "*":
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
                                 },
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
                                        "gte": globalparams.es_input_data['elastic_duration']
                                    }
                                }
                            }
                        }
                    }
                }, request_timeout=1)
                index = 1
                for hit in es_conn_hits['hits']['hits']:
                    es_dict[index] = {'elastic_query_hash': hit["_source"]["statement_hash"],
                                      'elastic_query_params': 'null',
                                      'elastic_query_stand': hit["_source"]["stand"],
                                      'elastic_query_database': hit["_source"]["database"],
                                      'elastic_query_text': hit["_source"]["statement"],
                                      'elastic_query_duration': hit["_source"]["duration"],
                                      'elastic_query_date': hit["_source"]["pgtime"]}
                    index += 1
                print("LEN: " + str(len(es_conn_hits)))
            except elasticsearch.ConnectionError:
                print("ES connection error")
    return es_dict


es_dict = get_elastic_regress_result()
