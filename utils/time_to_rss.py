from time import gmtime, strftime


def time_to_rss(time):
    return strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime(time))
