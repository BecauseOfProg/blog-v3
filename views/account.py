from flask import render_template, request, session, redirect
from utils.valid_login import valid_login
from utils.checklogin import checklogin
from pony.orm import db_session
from app import application
from db.models import User

'''Every page or route related to the account or the user connection
is included in this file.'''


@application.route('/account')
@db_session
def show_account():
    '''Shows the account page (a static page for now) or
    redirects the user to the login form'''
    u = checklogin()
    if u is not False:
        return render_template('members/account.html', u=u)
    else:
        return redirect('/login')


@application.route('/logout')
def logout():
    '''Logs out the user, removes cookies'''
    session.pop('username', None)
    session.pop('token', None)
    return redirect('/')


@application.route('/login', methods=['GET', 'POST'])
@db_session
def show_login():
    '''Display the login form if request is GET,
    logs in the user with the given informations if request is POST'''
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
