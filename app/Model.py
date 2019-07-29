from sqlalchemy import Column, Integer, String, ARRAY, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# database mapping


# rgbotsm.hcs_connect_info
class HcsConnectInfo(Base):
    __tablename__ = 'hcs_connect_info'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    subsystem_id = Column(Integer, ForeignKey('hcs_subsystems.id'), nullable=False)
    server_id = Column(Integer, ForeignKey('hcs_servers.id'), nullable=False)

    def __init__(self,
                 id=None,
                 subsystem_id=None,
                 server_id=None):
        self.id = id
        self.subsystem_id = subsystem_id
        self.server_id = server_id

    def __repr__(self):
       return '<id: %r\n subsystem_id: %r\n server_id: %r>' % (self.id,
                                                               self.subsystem_id,
                                                               self.server_id)


# rgbotsm.hcs_members
class HcsMembers(Base):
    __tablename__ = 'hcs_members'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String, nullable=False)
    user_name = Column(String, nullable=False)

    def __init__(self,
                 id=None,
                 login=None,
                 user_name=None):
        self.id = id
        self.login = login
        self.user_name = user_name

    def __repr__(self):
       return '<id: %r\n login: %r\n user_name: %r>' % (self.id,
                                                        self.login,
                                                        self.user_name)


# rgbotsm.hcs_servers
class HcsServers(Base):
    __tablename__ = 'hcs_servers'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    stand_id = Column(Integer, ForeignKey('hcs_stands.id'), nullable=False)
    server_name = Column(String, nullable=False)
    host = Column(String, nullable=False)
    port = Column(Integer, nullable=False)

    def __init__(self,
                 id=None,
                 stand_id=None,
                 server_name=None,
                 host=None,
                 port=None):
        self.id = id
        self.stand_id = stand_id
        self.user_name = server_name
        self.host = host
        self.port = port

    def __repr__(self):
       return '<id: %r\n stand_id: %r\n server_name: %r\n host: %r\n port: %r>' % (self.id,
                                                                                   self.stand_id,
                                                                                   self.server_name,
                                                                                   self.host,
                                                                                   self.port)


# rgbotsm.hcs_stands
class HcsStands(Base):
    __tablename__ = 'hcs_stands'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    stand_name = Column(String, nullable=False)

    def __init__(self,
                 id=None,
                 stand_name=None):
        self.id = id
        self.stand_name = stand_name

    def __repr__(self):
       return '<id: %r\n stand_name: %r>' % (self.id,
                                             self.stand_name)


# rgbotsm.hcs_subsystems
class HcsSubsystems(Base):
    __tablename__ = 'hcs_subsystems'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    database_name = Column(String, nullable=False)
    subsystem_name = Column(String, nullable=False)

    def __init__(self,
                 id=None,
                 database_name=None,
                 subsystem_name=None):
        self.id = id
        self.database_name = database_name
        self.subsystem_name = subsystem_name

    def __repr__(self):
       return '<id: %r\n database_name: %r\n subsystem_name: %r>' % (self.id,
                                                                     self.database_name,
                                                                     self.subsystem_name)


# rgbotsm.hcs_team_lineups
class HcsTeamLineups(Base):
    __tablename__ = 'hcs_team_lineups'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    team_id = Column(Integer, ForeignKey('hcs_teams.id'), nullable=False)
    tpm_id = Column(Integer, ForeignKey('hcs_members.id'), nullable=False)
    teamlead_id = Column(Integer, ForeignKey('hcs_members.id'), nullable=False)
    analyst_id = Column(Integer, ForeignKey('hcs_members.id'), nullable=False)
    qa_id = Column(Integer, ForeignKey('hcs_members.id'), nullable=False)
    dba_id = Column(Integer, ForeignKey('hcs_members.id'), nullable=False)

    def __init__(self,
                 id=None,
                 team_id=None,
                 tpm_id=None,
                 teamlead_id=None,
                 analyst_id=None,
                 qa_id=None,
                 dba_id=None):
        self.id = id
        self.team_id = team_id
        self.tpm_id = tpm_id
        self.teamlead_id = teamlead_id
        self.analyst_id = analyst_id
        self.qa_id = qa_id
        self.dba_id = dba_id

    def __repr__(self):
       return '<id: %r\n team_id: %r\n tpm_id: %r\n teamlead_id: %r\n analyst_id: %r\n qa_id: %r\n ' \
              'dba_id: %r>' % (self.id,
                               self.team_id,
                               self.tpm_id,
                               self.teamlead_id,
                               self.analyst_id,
                               self.qa_id,
                               self.dba_id)


# rgbotsm.hcs_teams
class HcsTeams(Base):
    __tablename__ = 'hcs_teams'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    team_number = Column(Integer, nullable=False)
    subsystem_id = Column(Integer, ForeignKey('hcs_subsystems.id'), nullable=False)

    def __init__(self,
                 id=None,
                 team_number=None,
                 subsystem_id=None):
        self.id = id
        self.team_number = team_number
        self.subsystem_id = subsystem_id

    def __repr__(self):
       return '<id: %r\n team_number: %r\n subsystem_id: %r>' % (self.id,
                                                                 self.team_number,
                                                                 self.subsystem_id)


# rgbotsm.jira_tasks
class JiraTasks(Base):
    __tablename__ = 'jira_tasks'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    stand_id = Column(Integer, ForeignKey('hcs_stands.id'), nullable=False)
    subsystem_id = Column(Integer, ForeignKey('hcs_subsystems.id'), nullable=False)
    statement_hash = Column(String, nullable=False)
    statement_text = Column(String, nullable=False)
    issue_number = Column(String, nullable=False)
    creation_date = Column(DateTime, nullable=False)

    def __init__(self,
                 id=None,
                 stand_id=None,
                 subsystem_id=None,
                 statement_hash=None,
                 statement_text=None,
                 issue_number=None,
                 creation_date=None):
        self.id = id
        self.stand_id = stand_id
        self.subsystem_id = subsystem_id
        self.statement_hash = statement_hash
        self.statement_text = statement_text
        self.issue_number = issue_number
        self.creation_date = creation_date

    def __repr__(self):
       return '<id: %r\n stand_id: %r\n subsystem_id: %r\n statement_hash: %r\n statement_text: %r\n ' \
              'issue_number: %r\n creation_date: %r>' % (self.id,
                                                         self.stand_id,
                                                         self.subsystem_id,
                                                         self.statement_hash,
                                                         self.statement_text,
                                                         self.issue_number,
                                                         self.creation_date)


# rgbotsm.user_filters
class UserFilters(Base):
    __tablename__ = 'user_filters'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user_login_info.id'), nullable=False)
    filter_name = Column(String, nullable=False)
    stand_id = Column(ARRAY(Integer), nullable=True)
    subsystem_id = Column(ARRAY(Integer), nullable=True)
    table_names = Column(ARRAY(String), nullable=True)
    key_words = Column(ARRAY(String), nullable=True)
    duration = Column(Integer, nullable=True)

    def __init__(self,
                 id=None,
                 user_id=None,
                 filter_name=None,
                 stand_id=None,
                 subsystem_id=None,
                 table_names=None,
                 key_words=None,
                 duration=None):
        self.id = id
        self.user_id = user_id
        self.filter_name = filter_name
        self.stand_id = stand_id
        self.subsystem_id = subsystem_id
        self.table_names = table_names
        self.key_words = key_words
        self.duration = duration

    def __repr__(self):
       return '<id: %r\n user_id: %r\n filter_name: %r\n stand_id: %r\n subsystem_id: %r\n ' \
              'table_names: %r\n key_words: %r\n duration: %r>' % (self.id,
                                                                   self.user_id,
                                                                   self.filter_name,
                                                                   self.stand_id,
                                                                   self.subsystem_id,
                                                                   self.table_names,
                                                                   self.key_words,
                                                                   self.duration)


# rgbotsm.user_login_info
class UserLoginInfo(Base):
    __tablename__ = 'user_login_info'
    __table_args__ = {'schema': 'rgbotsm'}
    id = Column(Integer, primary_key=True, nullable=False)
    login = Column(String, nullable=False)
    pass_hash = Column(String, nullable=True)

    def __init__(self,
                 id=None,
                 login=None,
                 pass_hash=None):
        self.id = id
        self.login = login
        self.pass_hash = pass_hash

    def __repr__(self):
       return '<id: %r\n login: %r\n pass_hash: %r>' % (self.id,
                                                        self.login,
                                                        self.pass_hash)
