from flask import Flask
from core.utils.image_proxy import image_proxy
from core.utils.links import get_hostname, clean_descr
from core.utils.time_to_rss import time_to_rss
import datetime


application = Flask(__name__, template_folder='../app/views', static_folder='../resources/static')
application.secret_key = 'HYP_7qbKg(*+A+h:'

application.add_template_global(name='image_proxy', f=image_proxy)
application.add_template_global(name='get_hostname', f=get_hostname)
application.add_template_global(name='clean_descr', f=clean_descr)
application.add_template_global(name='datetime', f=datetime)
application.add_template_global(name='time_to_rss', f=time_to_rss)
