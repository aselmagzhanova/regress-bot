from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route('/')
def root():
    return redirect(url_for('login'))


@app.route('/login')
def login():
    return render_template('login_form.html')


@app.route('/search')
def create_filter():
    return render_template('filter_form.html')


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
