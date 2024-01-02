from flask import Flask, render_template, request, redirect, url_for, session
from cassandra.cluster import Cluster
import os
import time

app = Flask(__name__)
app.secret_key = 'secret_app_key'

# Connect to Cassandra
cluster = Cluster([os.environ.get('CASSANDRA_HOST', '127.0.0.1')])
session_cassandra = cluster.connect('my_test_app')


@app.route('/')
def home():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    # Check credentials from Cassandra
    query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}' ALLOW FILTERING"
    result = session_cassandra.execute(query)

    if result.one():
        session['username'] = username
        return redirect(url_for('welcome'))
    else:
        return render_template('login.html', error='Invalid credentials')


@app.route('/welcome')
def welcome():
    if 'username' in session:
        return render_template('welcome.html', username=session['username'])
    else:
        return redirect(url_for('home'))


@app.route('/logout')
def logout():
    session.pop('username', None)
    return redirect(url_for('home'))


if __name__ == '__main__':
    time.sleep(5)
    app.run(debug=True, host='0.0.0.0', port=8000)

