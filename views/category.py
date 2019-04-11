from utils.fill_informations import fill_informations
from pony.orm import db_session, select, desc
from db.models import Articles, User
from flask import render_template
from app import application
import json


@application.route("/categorie/<cat_article>/<int:page>")
@application.route("/categorie/<cat_article>", defaults={'page': 0})
@application.route("/categorie/<cat_article>/", defaults={'page': 0})
@db_session
def show_cat(cat_article, page):
    '''Displays list.html with the lasts articles of a given category.
    Returns an error if the page is empty or if category does not exists.'''
    try:
        with open('static/data.json') as json_data:
            data = json.load(json_data)
            icon = data["categories"][cat_article]
            json_data.close()
    except:
        return render_template('components/erreur.html',
                               erreur="La catégorie entrée est invalide !")

    data = select(a for a in Articles if cat_article in a.category).order_by(
        desc(Articles.timestamp)
    )[page * 10: page * 10 + 10]

    if data == []:
        erreur = "La page recherchée n'existe pas! (404)"
        return render_template('components/erreur.html', erreur=erreur), 404
    data_dict = []
    for item in data:
        data_dict.append(fill_informations(item))

    return render_template('list.html', template="Catégorie", type=cat_article,
                           data=data_dict, icon=icon, page=page)
