from app import application

from views.blog import article, blog, category, home, type
from views.members import account, new_post
from views.page import about, app, links, projects, search
from views import misc

if __name__ == '__main__':
  application.run()
