from flask import Flask
from flask import render_template, redirect,url_for
from flask import request,session

app = Flask(__name__)

@app.route('/login', methods=['POST','GET'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username']=='admin':
            session['username'] = request.form['username']
            return redirect('/home')
        else:
            error = 'Invalid username/password'
    return render_template('login.html', error=error)

@app.route('/home')
def home():
    return render_template('home.html',username=session['username'])

app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0')
