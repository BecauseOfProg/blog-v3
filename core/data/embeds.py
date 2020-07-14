embeds = {
    "links": {
        "name": "Les liens",
        "description": "Les dernières actualités sélectionnées pour vous",
        "buttons": [
            {"text": "Twitter", "link": "https://twitter.com/BecauseOfProg"},
            {"text": "RSS", "link": "#"}
        ],
        "title_card": True,
        "source": "https://gh.becauseofprog.fr/links/?do=atom",
        "columns": "s12 m4",
        "fixed_height": True,
        "domain_as_descr": True,
        "custom_title": False,
        "include_enclosure": False
    },
    "twitter": {
        "name": "",
        "description": "",
        "buttons": [],
        "title_card": False,
        "source": "https://gh.becauseofprog.fr/rss-bridge/?action=display&bridge=Twitter&context=By+username&u=becauseofprog&norep=on&nopic=on&noimg=on&format=Atom",
        "columns": "s12 m12",
        "fixed_height": False,
        "domain_as_descr": False,
        "custom_title": True,
        "custom_title_text": "Nouveau tweet",
        "include_enclosure": False
    },
    "mastodon": {
        "name": "",
        "description": "",
        "buttons": [],
        "title_card": False,
        "source": "https://mstdn.io/@bop.rss",
        "columns": "s12 m12",
        "fixed_height": False,
        "domain_as_descr": False,
        "custom_title": True,
        "custom_title_text": "Nouveau toot",
        "include_enclosure": False
    },
    "instagram": {
        "name": "",
        "description": "Publié sur notre fil instagram",
        "buttons": [],
        "title_card": False,
        "source": "https://gh.becauseofprog.fr/rss-bridge/?action=display&bridge=Instagram&context=Username&u=becauseofprog&media_type=all&format=Atom",
        "columns": "s12 m12",
        "fixed_height": False,
        "domain_as_descr": False,
        "custom_title": False,
        "include_enclosure": True
    }
}
