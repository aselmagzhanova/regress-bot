from jira import JIRA
import yaml


with open('config.yml', 'r') as file:
    config = yaml.load(file)

jira = None
project_id = -1


# create jira connection
def jira_conn():
    global jira
    jira = JIRA(auth=(config['jira']['login'], config['jira']['password']),
                options={'server': config['jira']['server'],
                         'verify': False})
    print(jira)


# find HCS-project id
def get_project_id():
    global jira
    global project_id
    jira_conn_object = jira
    projects = jira_conn_object.projects()
    for project in projects:
        if project.key == 'HCS':
            project_id = project.id
    print(project_id)
    return project_id


def create_task(query_data, team_lineup):
    global jira
    global project_id
    jira_conn()
    jira_conn_object = jira
    # find HCS-project id
    project_id = get_project_id()
    # jira issue fields
    # summary
    summary = query_data['elastic_query_stand'] + ': ' + \
              query_data['elastic_query_database'] + \
              ' оптимизация ' + \
              " ".join(query_data['elastic_query_text'].replace('\n', '').split())[0:70]
    # description (with 'with_parameters' tag OR without 'with_parameters' tag)
    if query_data['elastic_query_params'] != 'null':
        description = '''Долгая работа запроса: 
        {code}
        %s
        {code}
        Пример самого долгого запроса с параметрами (дата - %s):
        {code}
        %s
        {code}
        Максимальное время - %s мс.
        План запроса на стенде %s:
        {code}
        %s
        {code}
        ''' % (query_data['elastic_query_text'],
               query_data['elastic_query_date'],
               'null',
               query_data['elastic_query_duration'],
               query_data['elastic_query_stand'],
               'null')

    else:

        description = '''Долгая работа запроса: 
                {code}
                %s
                {code}
                Дата - %s
                На стенде %s параметры для запроса не обнаружены (либо запрос в них не нуждается).
                Максимальное время - %s мс.
                ''' % (query_data['elastic_query_text'],
                       query_data['elastic_query_date'],
                       query_data['elastic_query_stand'],
                       query_data['elastic_query_duration'])

    # fill issue fields dict
    issue_dict = {
        'project': {'id': project_id},
        'summary': summary,
        'issuetype': {'name': 'Bug'},
        'components': [{'name': 'База данных'}, {'name': 'Оптимизация производительности'}],
        # Аналитик
        'customfield_10044': {'name': team_lineup.get('analyst')},
        # ТРП
        'customfield_15120': {'name': team_lineup.get('tpm')},
        # Тимлид
        'customfield_10828': {'name': team_lineup.get('teamlead')},
        # Инженер по тестированию
        'customfield_16120': {'name': team_lineup.get('qa')},
        'fixVersions': [{'name': '12.2.3.0'}],
        # Код сценария из ЧТЗ
        'customfield_12621': '-',
        # Шаги воспроизведения
        'customfield_14531': 'Выяснить, какой функционал пораждает запрос',
        # Фактический результат
        'customfield_15522': description,
        # Ожидаемый результат
        'customfield_15523': 'Запрс выполняется менее * сек/мин',
        # Ссылка на ЧТЗ
        'customfield_10821': '-',
        'environment':  query_data['elastic_query_stand'],
        # Версия ЧТЗ
        'customfield_12120': '-',
        # Предусловие
        'customfield_15520': '-',
        # Ответственный за задачу
        'assignee': {'name': team_lineup.get('dba')}
    }

    jira_issue = jira_conn_object.create_issue(fields=issue_dict)

    return str(jira_issue.key)


def return_status(issue_number):
    global jira
    global project_id
    jira_conn()
    jira_conn_object = jira
    print(issue_number)
    current_issue = jira_conn_object.issue(issue_number)
    return current_issue.fields.status


def reopen_task(issue_number):
    global jira
    global project_id
    jira_conn()
    jira_conn_object = jira
    jira_conn_object.transition_issue(issue_number, transition='На анализ')
    current_issue = jira_conn_object.issue(issue_number)
    teamlead = current_issue.raw['fields']['customfield_10828']['name']
    jira_conn_object.assign_issue(issue_number, teamlead)

print(return_status('HCS-88972'))
