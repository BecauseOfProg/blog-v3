from pony.orm import db_session
from db.models import User
from flask import session


@db_session
def checklogin():
    if 'token' in session:
        u = User.get(token=session['token'])
    else:
        try:
            u = User.get(token=request.cookies.get('token'))
            session['token'] = u.token
            session['username'] = u.username
        except:
            return False
    return u
