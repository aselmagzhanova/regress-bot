import elastic
from flask import flash, Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
import globalparams
from Model import HcsStands, HcsSubsystems, JiraTasks, UserLoginInfo
from sqlalchemy import func
import yaml

app = Flask(__name__)

with open("config.yml", 'r') as file:
    config = yaml.load(file)

app.config['SECRET_KEY'] = 'idi_v_svoi_dvor'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%s:%s@%s:%s/%s' % (config['postgresql']['pg_user'],
                                                                         config['postgresql']['pg_password'],
                                                                         config['postgresql']['host'],
                                                                         config['postgresql']['port'],
                                                                         config['postgresql']['pg_database'])

db = SQLAlchemy(app)


@app.route('/')
def root():
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        # check login
        session['login'] = int(db.session.query(UserLoginInfo).filter(
            func.lower(UserLoginInfo.login) == str(request.form['input-login']).lower()).count())
        if session['login'] == 1:
            # check password
            session['password'] = str((db.session.query(
                func.rgbotsm.func_user_auth(str(request.form['input-login']),
                                            str(request.form['input-password']))).all())[0][0])
            if session['password'] == 'True':
                session['login'] = str(request.form['input-login']).lower()
                session['user_name'] = str(db.session.query(
                    func.rgbotsm.func_get_user_name(session['login'])).first()[0])
                return redirect(url_for('create_filter'))
            else:
                flash('Wrong password!')
        else:
            flash('Wrong login!')
    return render_template('login_form.html')


@app.route('/search')
def create_filter():
    globalparams.pg_stands = []
    globalparams.pg_databases = []
    globalparams.pg_subsystems = []
    if session['login'] is None:
        return redirect(url_for('login'))
    for row in db.session.query(HcsStands.stand_name).all():
        globalparams.pg_stands.append(row[0])
    for row in db.session.query(HcsSubsystems.database_name).distinct(HcsSubsystems.database_name).all():
        globalparams.pg_databases.append(row[0])
    for row in db.session.query(HcsSubsystems.subsystem_name).filter(
            func.lower(HcsSubsystems.database_name) == 'hcshmdb').all():
        globalparams.pg_subsystems.append(row[0])
    return render_template("filter_form.html",
                           user_name=session['user_name'],
                           pg_stands=globalparams.pg_stands,
                           pg_databases=globalparams.pg_databases,
                           pg_subsystems=globalparams.pg_subsystems)


@app.route('/search', methods=['POST'])
def create_filter_post():
    if request.method == 'POST':
        if 'button-search' in request.form:
            if request.form.getlist('checkbox-stand') is not None:
                globalparams.elastic_stand = request.form.getlist('checkbox-stand')
            if request.form.getlist('checkbox-database') is not None:
                globalparams.elastic_database = request.form.getlist('checkbox-database')
            if request.form.getlist('checkbox-subsystem') is not None:
                globalparams.elastic_subsystem = request.form.getlist('checkbox-subsystem')
            if request.form['duration'] is not "":
                globalparams.elastic_duration = request.form['duration']
            if request.form['time-from'] and request.form['time-to'] is not "":
                globalparams.elastic_time_range = [request.form['time-from'], request.form['time-to']]
            return redirect(url_for('search_result'))
        if 'button-save-filter' in request.form:
            if request.form.getlist('checkbox-stand') is not None:
                user_filter_stand = request.form.getlist('checkbox-stand')
            if request.form.getlist('checkbox-database') is not None:
                user_filter_subsystem = request.form.getlist('checkbox-database')
            if request.form['duration'] is not "":
                user_filter_duration = request.form['duration']
            if request.form['filter-name'] is not "":
                user_filter_name = request.form['filter-name']
            else:
                user_filter_name = 'NULL'
            try:
                db.session.execute(
                    "select * from rgbotsm.func_create_user_filter('" + user_filter_name + "', \
                     '" + session['login'] + "', \
                      ARRAY" + str(user_filter_stand) + ", \
                      ARRAY" + str(user_filter_subsystem) + ", \
                      '" + user_filter_duration + "');")
                db.session.commit()
            except():
                redirect(url_for('error_500'))
    return '', 204


@app.route('/searchresult')
def search_result():
    if session['login'] is None:
        return redirect(url_for('login'))
    es_data = elastic.get_elastic_regress_result()
    pg_data = {}
    for row in db.session.query(JiraTasks.statement_hash, JiraTasks.issue_number).all():
        pg_data[row[0]] = row[1]
    return render_template("filter_result.html", user_name=session['user_name'], es_data=es_data, pg_data=pg_data)


@app.route('/filters')
def filters_list():
    return render_template('filters_list.html')


@app.route('/jiraissues')
def jira_issues():
    return render_template('jira_issues.html')


@app.route('/userinfo')
def user_info():
    return render_template('user_info.html')


@app.route('/links')
def useful_links():
    return render_template('FAQ.html')


@app.errorhandler(404)
def error_404(e):
    return render_template('404.html'), 404


@app.errorhandler(500)
def error_500(e):
    return render_template('500.html'), 500


if __name__ == '__main__':
    app.run()
