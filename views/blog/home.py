from utils.fill_informations import fill_informations
from utils.links import links_list
from pony.orm import db_session, select, desc
from flask import render_template
from db.models import Articles, User
import requests
from app import application


@application.route("/")
@db_session
def home():
    '''Homepage of your blog'''
    last = (
        select(
            (a.title, a.description, a.banner, a.url, a.timestamp) for a in Articles)
        .order_by(-5)
        .first()
    )
    lasts_art = select(a for a in Articles).order_by(desc(Articles.timestamp))[1:4]
    list_of_dict = []
    for item in lasts_art:
        list_of_dict.append(fill_informations(item))

    r = requests.get('https://api.becauseofprog.fr/v1/posts/last')
    devblog = r.json()
    return render_template('blog/home.html', last=last, lasts=list_of_dict,
                           devblog=devblog)
