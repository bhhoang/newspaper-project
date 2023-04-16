from pymongo import MongoClient
from .article import Article
from .author import Author
import configparser
import os

config = configparser.ConfigParser()
config.read(os.path.join(os.path.dirname(__file__), '../base.conf'))
DATABASE = config['DEFAULT']['host']

class Database:
    def __init__(self):

        self.__client = MongoClient(DATABASE)
        self.__database = self.__client['newspapers_db']
        self.articles_collection = self.__database['newspapers']
        self.authors_collection = self.__database['authors']

    def count_all_authors(self) -> int:
        return self.articles_collection.count_documents({})

    def count_all_articles(self) -> int:
        return self.articles_collection.count_documents({})

    def get_all_articles(self) -> list[Article]:
        article_objs: list[Article] = []
        articles = self.articles_collection.find()
        for article in articles:
            date = article['date']
            category = article['category']
            viewed = article['viewed']
            title = article['title']
            description = article['description']
            author = article['author']
            content = article['content']
            ID = article['_id']
            new_article = Article(date, category, viewed, title, description, author, content, ID)
            article_objs.append(new_article)
        return article_objs

    def add_articles_to_db(self, article: Article):
        articles_data = {
            '_id': article.get_id(),
            'date': article.get_date(),
            'category': article.get_category(),
            'viewed': article.get_views(),
            'title': article.get_title(),
            'description': article.get_overview(),
            'author': article.get_author(),
            'content': article.get_content(),
            'preview_img': article.get_preview_img(),
        }

        # Insert the article into the database
        self.articles_collection.insert_one(articles_data)

    def add_author_to_db(self, author: Author):
        authors_data = {
            '_id': author.get_id(),
            'username': author.get_username(),
            'password': author.get_password(),
            'name': author.get_name(),
            'email': author.get_email(),
            'bio': author.get_bio(),
            'expertise': author.get_expertise(),
            'publication_history': author.get_publication_history()
        }

        # Insert the author into the database
        self.authors_collection.insert_one(authors_data)

    def _check_exist_username(self, username: str) -> bool:
        """
        :return: True when the username is in the database, False otherwise
        """
        result = self.authors_collection.find_one({'username': username})
        if result is None:
            return False
        password = result.get('password', None)
        return password
    
    def _check_exist_email(self, email: str) -> bool:
        """
        :return: True when the email is in the database, False otherwise
        """
        result = self.authors_collection.find_one({'email': email})
        if result is None:
            return False
        password = result.get('password', None)
        return password
    
    def _delete_article(self, ft: dict):
        self.articles_collection.delete_one(ft)

    def get_all_categories(self) -> list[str]:
        categories = self.articles_collection.distinct('categories')
        return categories

    def get_article_by_title(self, text: str):
        articles = []     # list of article
        results = self.articles_collection.find()
        for result in results:
            if text in result['title']:
                articles.append(result)
        return articles

    def get_article_by_category(self, category: str):
        articles = []
        result = self.articles_collection.find({'category': category})
        for article in result:
            articles.append(article)
        return articles

    def get_article_by_id(self, ID):
        return self.articles_collection.find_one({'_id': ID})

    def get_articles_sort_views(self, limit: int):
        articles = []
        result = self.articles_collection.find().sort('viewed', -1).limit(limit)
        for article in result:
            articles.append(article)
        return articles

    def get_articles_sort_date(self, limit: int):
        articles = []
        result = self.articles_collection.find().sort('date', -1).limit(limit)
        for article in result:
            articles.append(article)
        return articles

    def get_author_by_name(self, name: str):
        author = self.authors_collection.find_one({'name': name})
        return author
    
    def get_author_by_id(self, ID: int):
        return self.authors_collection.find_one({'_id': ID})

    def update_publish_history(self, author_id: int, article_id: int):
        # Get the author's publication history
        history = self.authors_collection.find_one({'_id': author_id}, {'_id': 0, 'publication_history': 1})
        history_array = history['publication_history']
        # Add the new article to the history
        history_array.append(article_id)
        # Update the author's publication history
        self.authors_collection.update_one({'_id': author_id}, {'$set': {'publication_history': history_array}})

    def set_email(self, author_id: int, email: str):
        self.authors_collection.update_one({'_id': author_id}, {'$set': {'email': email}})

    def set_bio(self, author_id: int, bio: str):
        self.authors_collection.update_one({'_id': author_id}, {'$set': {'bio': bio}})

    def set_expertise(self, author_id: int, expertise: str):
        self.authors_collection.update_one({'_id': author_id}, {'$set': {'expertise': expertise}})

