from flask import render_template
from core.app import application
from app.controllers.blog import BlogController
from app.controllers.redirects import RedirectsController
from app.controllers.page import PageController
from app.controllers.members import MembersController
from app.controllers.staff import StaffController
from app.controllers.misc import MiscController

# ----------------- BLOG -----------------

application.add_url_rule('/', None, BlogController.show_home)
application.add_url_rule('/blog/', None, BlogController.show_blog, defaults={'page': 0})
application.add_url_rule('/blog/<int:page>', None, BlogController.show_blog)
application.add_url_rule('/article/<string:url>', None, BlogController.show_article)
application.add_url_rule('/categorie/<string:category>/<int:page>', None, BlogController.show_category)
application.add_url_rule('/categorie/<string:category>', None, BlogController.show_category, defaults={'page': 0})
application.add_url_rule('/type/<string:type>/<int:page>', None, BlogController.show_type)
application.add_url_rule('/type/<string:type>', None, BlogController.show_type, defaults={'page': 0})

# ----------------- MEMBERS -----------------

application.add_url_rule('/account', None, MembersController.show_account)
application.add_url_rule('/logout', None, MembersController.logout)
application.add_url_rule('/login', None, MembersController.show_login, methods=['GET', 'POST'])
application.add_url_rule('/user/<string:username>', None, MembersController.show_user_page)

# ----------------- PAGES -----------------

application.add_url_rule('/page/about', None, PageController.about)
application.add_url_rule('/page/app', None, PageController.app)
application.add_url_rule('/page/links', None, PageController.links)
application.add_url_rule('/page/links-embed', None, PageController.links_embed)
application.add_url_rule('/page/projects', None, PageController.projects)
application.add_url_rule('/page/search/', None, PageController.search, defaults={'keyword': None, 'page': 0})
application.add_url_rule('/page/search/<string:keyword>/', None, PageController.search, defaults={'page': 0})
application.add_url_rule('/page/search/<string:keyword>/<int:page>/', None, PageController.search)

# ----------------- STAFF -----------------

application.add_url_rule('/new-post', None, StaffController.new_post, methods=['GET', 'POST'])

# ----------------- REDIRECTS -----------------

application.add_url_rule('/blog/<string:url>-<int:id>', None, RedirectsController.redirect_old_url_blog)
application.add_url_rule('/courses/', None, RedirectsController.redirect_courses)
application.add_url_rule('/courses/<whatever>', None, RedirectsController.redirect_courses)
application.add_url_rule('/app/', None, RedirectsController.redirect_app)
application.add_url_rule('/members/', None, RedirectsController.redirect_about)
application.add_url_rule('/community/', None, RedirectsController.redirect_about)
application.add_url_rule('/about/', None, RedirectsController.redirect_about)

# ----------------- MISC -----------------

application.add_url_rule('/pwabuilder-sw.js', None, MiscController.get_pwa)
application.add_url_rule('/blog.rss', None, MiscController.get_rss)
application.add_url_rule('/tout.rss', None, MiscController.get_rss)
application.add_url_rule('/sitemap-articles.xml', None, MiscController.get_sitemap)

@application.errorhandler(404)
def page_not_found(_):
  '''Returns the 404 error page'''
  erreur = "La page recherchée n'existe pas! (404)"
  return render_template('components/erreur.html',
                         erreur=erreur), 404