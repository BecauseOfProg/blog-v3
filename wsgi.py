from app import application

from views import index, article, blog, category, type, misc
from views.page import about, app, links, search, projects
from views.members import account, new_post

if __name__ == '__main__':
    application.run()
