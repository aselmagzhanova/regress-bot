from datetime import date, datetime, timedelta
import yaml


with open('config.yml', 'r') as file:
    config = yaml.load(file)


def return_elastic_indices_names(time_range):
    indices = []
    start_date_ref = datetime.strptime(time_range[0], '%Y-%m-%d')
    start_date = date(start_date_ref.year, start_date_ref.month, start_date_ref.day)
    end_date_ref = datetime.strptime(time_range[1], '%Y-%m-%d')
    end_date = date(end_date_ref.year, end_date_ref.month, end_date_ref.day)
    delta = end_date - start_date
    for i in range(delta.days + 1):
        indices.append(config['elastic']['index'] + (start_date + timedelta(days=i)).isoformat().replace('-', '.'))
    return indices

# это очень костыльно, но нет апи
def return_kibana_link(time_range, stands, databases, duration):
    # собираем названия инлдексов
    indices = return_elastic_indices_names(time_range)
    # выбираем последние 30 дней для показа результатов
    link_text = "https://ft01.dom.test.gosuslugi.ru/kibana/app/kibana#/discover?_g=(refreshInterval:" +\
                "(pause:!t,value:0),time:(from:now-30d,mode:quick,to:now))&_" +\
                "a=(columns:!(_source),filters:!(('$state':(store:appState),"
    # выбираем только записи с тэгом 'postgres'
    program_text = "meta:(alias:!n,disabled:!f,index:'13424010-51ff-11e9-91f0-ef29dfee514f',key:program,negate:!f," +\
                   "params:(query:postgres,type:phrase),type:phrase,value:postgres),query:(match:(program:" +\
                   "(query:postgres,type:phrase)))),('$state':(store:appState),"
    # выбираем стенды
    if len(stands) is not 0:
        stands_text = "meta:(alias:!n,disabled:!f,index:'13424010-51ff-11e9-91f0-ef29dfee514f',key:stand,negate:!f,params:!" +\
                      "(" + ','.join(stands) + "),type:phrases,value:'" + stands[0]
        for stand in stands[1:]:
            stands_text = stands_text + ",%20" + stand
        stands_text = stands_text + "'),query:(bool:(minimum_should_match:1,should:!((match_phrase:(stand:" + stands[0] + "))"
        for stand in stands[1:]:
            stands_text = stands_text + ",(match_phrase:(stand:" + stand + "))"
        stands_text = stands_text + ")))),('$state':(store:appState),"
    else:
        stands_text = ""
    # выбираем базы
    if len(databases) is not 0:
        databases_text = "meta:(alias:!n,disabled:!f,index:'13424010-51ff-11e9-91f0-ef29dfee514f',key:database,negate:!f,params:!" +\
                         "(" + ','.join(databases) + "),type:phrases,value:'" + databases[0]
        for database in databases[1:]:
            databases_text = databases_text + ",%20" + database
        databases_text = databases_text + "'),query:(bool:(minimum_should_match:1,should:!((match_phrase:(database:" + databases[0] + "))"
        for database in databases[1:]:
            databases_text = databases_text + ",(match_phrase:(database:" + database + "))"
        databases_text = databases_text + ")))),('$state':(store:appState),"
    else:
        databases_text = ""
    # выбираем индексы (== дату)
    indices_text = "meta:(alias:!n,disabled:!f,index:'13424010-51ff-11e9-91f0-ef29dfee514f',key:_index,negate:!f,params:!" +\
                   "(" + ','.join(indices) + "),type:phrases,value:'" + indices[0]
    for index in indices[1:]:
        indices_text = indices_text + ",%20" + index
    indices_text = indices_text + "'),query:(bool:(minimum_should_match:1,should:!((match_phrase:(_index:" + indices[0] + "))"
    for index in indices[1:]:
        indices_text = indices_text + ",(match_phrase:(_index:" + index + "))"
    indices_text = indices_text + ")))),('$state':(store:appState),"
    # выбираем длительность запроса
    duration_text = "meta:(alias:!n,disabled:!f,index:'13424010-51ff-11e9-91f0-ef29dfee514f',key:duration,negate:!f,params:" +\
                    "(gte:" + str(duration) + ",lt:99999999),type:range,value:'"
    if duration > 1000:
        duration_text = duration_text + str(duration/1000) + ".00%20to%20100000.00'),"
    else:
        duration_text = duration_text + str(duration / 1000) + "%20to%20100000.00'),"
    duration_text = duration_text + "range:(duration:(gte:" + str(duration) + ",lt:99999999)))),"
    # выбираем сортировку
    sort_text = "index:'13424010-51ff-11e9-91f0-ef29dfee514f',interval:auto,query:(language:lucene,query:''),sort:!('@timestamp',desc))"
    return link_text + program_text + stands_text + databases_text + indices_text + duration_text + sort_text
