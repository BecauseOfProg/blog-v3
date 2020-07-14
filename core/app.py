from flask import Flask
import datetime

from core.utils.breadcrumb import breadcrumb
from core.utils.image_proxy import image_proxy
from core.utils.links import get_hostname, clean_descr
from core.utils.time_to_rss import time_to_rss

from core.data.categories import categories
from core.data.types import types


application = Flask(
    __name__,
    template_folder='../app/views',
    static_folder='../resources/static',
    static_url_path='')
application.secret_key = 'HYP_7qbKg(*+A+h:'

application.add_template_global(name='image_proxy', f=image_proxy)
application.add_template_global(name='get_hostname', f=get_hostname)
application.add_template_global(name='clean_descr', f=clean_descr)
application.add_template_global(name='datetime', f=datetime)
application.add_template_global(name='time_to_rss', f=time_to_rss)
application.add_template_global(name='breadcrumb', f=breadcrumb)


@application.context_processor
def context_processor():
    return dict(TYPES=types, CATEGORIES=categories)
