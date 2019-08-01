from flask import flash, Flask, redirect, render_template, request, session, url_for
from flask_sqlalchemy import SQLAlchemy
from Model import UserLoginInfo
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
    return render_template('filter_form.html', user_name=session['user_name'])


@app.route('/searchresult')
def search_result():
    return render_template('filter_result.html')


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


if __name__ == '__main__':
    app.run()
