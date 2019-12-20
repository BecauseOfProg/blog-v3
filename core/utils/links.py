from urllib.parse import urlparse
import feedparser
import re

'''Contains useful fucntions to display links on the home page and on
the links page. The links are taken from a RSS Feed and then the
description can be edited, to avoid reproducing content'''


def clean_descr(descr):
    '''Links: cuts a text if it's too long'''
    caption = "... Lisez la suite de l'article sur le site d'origine!"

    cleanregex = re.compile('<.*?>')
    cleandescr = re.sub(cleanregex, '', descr)
    # Removing any html tag from the text

    if len(cleandescr) > 500:
        cleandescr = cleandescr[:300] + caption
    return cleandescr


def get_hostname(url):
    '''Get only the hostname of a website,
    without 'www' or any protocol or folder'''
    o = urlparse(url)    # We're using urlparse
    hostname = o.netloc  # and selecting only the netloc
    if o.netloc.startswith("www."):  # removes wwww. if exists
        hostname = hostname[4:]
    return hostname


def links_list(source, length, description):
    '''Returns a dictionnary of linksfrom the an rss feed proxy:
    it can remove some entries or remove all descriptions (faster loading)
    Description is True or False. Source parameter can be links, twitter, mastodon, instagram'''
    if source == "links": feed_url = "https://gh.becauseofprog.fr/rss-proxy/"+str(length)+'/'+description
    else: feed_url = source

    d = feedparser.parse(feed_url)
    return d
