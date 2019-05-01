from app import application
from views import index, article, blog, category, type
from views import page_about, page_app, page_links, page_search, page_projects
from views import account, new_post, misc

if __name__ == '__main__':
    application.run(host='0.0.0.0', port=5001)
