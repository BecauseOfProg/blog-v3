from utils.links import links_list
from flask import render_template
from app import application


@application.route("/page/links")
def links():
    links = links_list(20, "true")
    len_links = len(links['entries'])
    return render_template('page/liens.html', links=links, len_links=len_links)
