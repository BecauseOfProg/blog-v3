from urllib.parse import urlparse
import feedparser
import re


def clean_descr(descr):
    '''Links: cuts a text if it's too long'''
    cleanregex = re.compile('<.*?>')
    cleandescr = re.sub(cleanregex, '', descr)
    # Removing any html tag from the text

    if len(cleandescr) > 500:
        cleandescr = cleandescr[:300]+"... Lisez la suite de l'article sur le site d'origine!"
    return cleandescr


def get_hostname(url):
    '''Get only the hostname of a website,
    without 'www' or any protocol or folder'''
    o = urlparse(url) # We're using urlparse
    hostname = o.netloc # and selecting only the netloc
    if o.netloc.startswith("www."): # removes wwww. if exists
        hostname = hostname[4:]
    return hostname


def links_list(length, description):
    '''Returns a dictionnary of linksfrom the an rss feed proxy:
    it can remove some entries or remove all descriptions (faster loading)'''
    d = feedparser.parse('https://gh.becauseofprog.fr/rss-proxy/'+str(length)+'/'+description)
    return d
