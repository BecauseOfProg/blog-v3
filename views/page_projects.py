from flask import render_template
from app import application


@application.route("/page/projects")
def projects():
    '''Returns a static file'''
    return render_template('page/projects.html')
