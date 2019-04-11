from pony.orm import db_session
from db.models import User
from flask import session

'''This files contains the function checklogin(),
which checks if the client is logged to his BecauseOfProg account'''


@db_session
def checklogin():
    '''checks if the client is logged to his BecauseOfProg account.
    Returns an object containing all the user informations if he's logged in,
    False if not'''
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
