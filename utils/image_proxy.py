from urllib.parse import urlparse

'''This file contains the function image_proxy'''


def image_proxy(url, width, height):
    '''Optimize images and pictures by resizing them to apppropriate sizes
    and reducing their size. Currently we're using a reverse proxy
    and the real pictures comes from lesnumeriques.com'''
    proxy = "https://image-proxy.becauseofprog.fr/"
    o = urlparse(url)
    if width == 0 or height == 0:
        return proxy+o.netloc+o.path
        # Don't try to resize pictures if the width or heigth equals to 0
    else:
        out = proxy+o.netloc+o.path+"?resize="+str(width)+","+str(height)
        return out
