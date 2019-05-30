from flask import render_template
from app import application


@application.route("/page/app")
def app():
    '''Returns a static file'''
    return render_template('page/app.html')
