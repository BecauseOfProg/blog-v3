from flask import Flask
from utils.image_proxy import image_proxy
from utils.links import get_hostname, clean_descr
from utils.time_to_rss import time_to_rss

import datetime

application = Flask(__name__)
application.secret_key = "HYP_7qbKg(*+A+h:"

# application.config.update(
#     TESTING=True,
#     SECRET_KEY=b'HYP_7qbKg(*+A+h:'

# )

# application.jinja_env.globals.update(image_proxy=image_proxy)
# application.jinja_env.globals.update(get_hostname=get_hostname)
# application.jinja_env.globals.update(clean_descr=clean_descr)
# application.jinja_env.globals.update(datetime=datetime)
# application.jinja_env.globals.update(time_to_rss=time_to_rss)

application.add_template_global(name='image_proxy', f=image_proxy)
application.add_template_global(name='get_hostname', f=get_hostname)
application.add_template_global(name='clean_descr', f=clean_descr)
application.add_template_global(name='datetime', f=datetime)
application.add_template_global(name='time_to_rss', f=time_to_rss)
