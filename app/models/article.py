from pony.orm import Required, PrimaryKey, Json, desc, db_session
from core.database import db
from core.exceptions import NoArticlesFound
from core.utils.fill_informations import fill_informations

'''This is the model of a blog article. It matches the `articles` table in the database.'''


class Articles(db.Entity):
    url = PrimaryKey(str)
    title = Required(str)
    timestamp = Required(float)
    author = Required(str)
    type = Required(str)
    category = Required(str)
    description = Required(str, column="desc")
    labels = Required(Json)
    banner = Required(str)
    content = Required(str, max_len=50000)
    article_language = Required(str)

    _table_ = "articles"

    @staticmethod
    @db_session
    def get_articles_in_range(min, max):
        lasts_art = Articles.select().order_by(
            desc(Articles.timestamp))[min:max]
        list_of_dict = []
        for item in lasts_art:
            list_of_dict.append(fill_informations(item))
        return list_of_dict

    @staticmethod
    @db_session
    def search_articles(keyword, page):
        keyword = keyword.lower()
        all_data = Articles.select(
            lambda a: keyword in a.title.lower() or keyword in a.description.lower()
        ).order_by(
            desc(Articles.timestamp)
        )
        total_articles = len(all_data)
        data = all_data[page * 10:page * 10 + 10]
        if data == []:
            raise NoArticlesFound
        else:
            articles = []
            for item in data:
                articles.append(fill_informations(item))
            return articles, total_articles
