from flask import render_template, request, session, redirect
from utils.valid_login import valid_login
from utils.checklogin import checklogin
from pony.orm import db_session
from app import application
from db.models import User


@application.route('/account')
@db_session
def show_account():
    u = checklogin()
    if u is not False:
        return render_template('members/account.html', u=u)
    else:
        return redirect('/login')


@application.route('/logout')
def logout():
    session.pop('username', None)
    session.pop('token', None)
    return redirect('/')


@application.route('/login', methods=['GET', 'POST'])
@db_session
def show_login():
    if 'token' in session:
        return redirect('/')
    if request.method == 'POST':
        if valid_login(request.form['username'], request.form['password']):
            u = User.get(email=request.form['username'])
            session['token'] = u.token
            session['username'] = u.username
            return redirect('/')
        else:
            return render_template('members/login.html',
                                   error="Les identifiants sont invalides")
    else:
        return render_template('members/login.html')
