from flask import redirect


class RedirectsController:
    @staticmethod
    def redirect_old_url_blog(url, id):
        new_url = "/article/" + url
        return redirect(new_url)

    @staticmethod
    def redirect_about():
        '''Redirects about page'''
        return redirect('/page/about')

    @staticmethod
    def redirect_app():
        '''Redirects app page'''
        return redirect('/page/app')

    @staticmethod
    def redirect_courses(_):
        '''Redirects blog-old page'''
        return redirect('/type/tutorial/')
