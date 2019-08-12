########################################################################################################################
### PG PARAMS ##########################################################################################################
pg_stands = []
pg_databases = []
pg_subsystems = []


########################################################################################################################
### ELASTIC QUERY PARAMS ###############################################################################################
es_input_data = {'elastic_stand': ['null'],
                 'elastic_database': ['null'],
                 'elastic_subsystem': ['null'],
                 'elastic_duration': -1,
                 'elastic_time_range': ['*', '*']}


########################################################################################################################
### ELASTIC RESULT PARAMS ##############################################################################################
es_output_data = {}
# elastic_query_hash = ''
# elastic_query_text = ''
# elastic_query_params = 'null'
# elastic_query_duration = ''
# elastic_query_date = None


########################################################################################################################
### JIRA + PG TASK ADD PARAMS ##########################################################################################
pg_team_lineup = {}
pg_query_explain = ''
jira_issues = []
issues_statuses = {}
