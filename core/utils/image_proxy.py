from urllib.parse import urlparse, quote

'''This file contains the function image_proxy'''


def image_proxy(url, width, height):
    '''Optimize images and pictures by resizing them to apppropriate sizes
    and reducing their size. We're using Photon, a PHP application used on
    WordpPress to proxify and dynamically resize pictures. '''
    
    proxy = "https://i.cdn.becauseofprog.fr/"
    o = urlparse(url)
    
    if width == 0 and height == 0:
        ret =  proxy+o.netloc+o.path
        # Don't try to resize pictures if the width and heigth equals to 0
    elif width == 0:
        ret = proxy+o.netloc+o.path+"?h="+str(height)
    elif height == 0:
        ret = proxy+o.netloc+o.path+"?w="+str(width)
    else:
        ret = proxy+o.netloc+o.path+"?resize="+str(width)+","+str(height)
    
    return ret
