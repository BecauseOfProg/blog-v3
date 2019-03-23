from urllib.parse import urlparse


def image_proxy(url, width, height):
    '''Optimize images and pictures by resizing them to apppropriate sizes
    and reducing their size. Currently we're using a reverse proxy
    and the real pictures comes from lesnumeriques.com'''
    cdn_link = "https://image-proxy.becauseofprog.fr/"
    o = urlparse(url)
    if width == 0 or height == 0:
        return cdn_link+o.netloc+o.path
        # Don't try to resize pictures if the width or heigth equals to 0
    else:
        out = str(cdn_link)+str(o.netloc)+str(o.path)+"?resize="+str(width)+","+str(height)
        return out
