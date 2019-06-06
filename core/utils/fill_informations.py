from datetime import datetime
from app.models.user import User

'''This file contains the function fill_informations'''


def fill_informations(post):
    '''Returns a dictionnary with all the usefull info about a given article'''
    response = {
        "timestamp": datetime.fromtimestamp(post.timestamp),
        "title": post.title,
        "url": post.url,
        "type": post.type,
        "category": post.category,
        "author": User[post.author],
        "banner": post.banner,
        "description": post.description,
        "labels": post.labels
    }
    return response
