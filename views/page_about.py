from pony.orm import db_session, select
from db.models import Articles, User
from flask import render_template
from app import application


@application.route("/page/about")
@db_session
def about():
    '''Displays the 'about' page with a stafflist'''
    stafflist = []
    staff = select(p for p in User if p.validate == 1)[:]
    for p in staff:
        stafflist.append([p.grade, p.username, p.description,
                          p.displayname, p.avatar])
    return render_template('page/about.html', staff=stafflist)
