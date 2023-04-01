from hashlib import sha256
from model.dbquery import Database
from model.author import Author
from model.article import Article

db = Database()


class Newspapers:
    def __init__(self):
        self.__hot_articles: list[Article] = db.get_articles_sort_views(1)
        self.__recent_articles: list[Article] = []
        self.__current_author: Author | None = None     # Default to None when not logged in

    @staticmethod
    def __convert_to_Author(author_info) -> Author:
        username = author_info['username']
        password = author_info['password']
        ID = author_info['_id']
        name = author_info['name']
        email = author_info['email']
        bio = author_info['bio']
        expertise = author_info['expertise']
        publication_history = author_info['publication_history']
        author = Author(username, password, name, ID, email, bio, expertise, publication_history)
        return author

    @staticmethod
    def __convert_to_Article(article_info) -> Article:
        date = article_info['date']
        category = article_info['category']
        viewed = article_info['viewed']
        title = article_info['title']
        description = article_info['description']
        author_id = article_info['author']
        content = article_info['content']
        ID = article_info['_id']
        article = Article(date, category, viewed, title, description, author_id, content, ID)
        return article

    # Signup, Login and Logout
    @staticmethod
    def create_author(username: str, password: str, real_name: str) -> bool:
        """
        :return: False if username is already taken, True otherwise
        """
        hashed_password = sha256(password.encode()).hexdigest()
        check = db.check_exist_username(username)
        if check:
            return False
        author_id = db.count_all_authors() + 1
        author = Author(username, hashed_password, real_name, author_id)
        db.add_author_to_db(author)
        return True

    def login(self, username: str, password: str) -> bool:
        """
        :return: True if login is successful, False otherwise
        """
        hashed_password = sha256(password.encode()).hexdigest()
        author_info = db.authors_collection.find_one({'username': username, 'password': hashed_password})
        if author_info is None:
            return False
        author_obj = self.__convert_to_Author(author_info)
        self.__current_author = author_obj
        return True

    def logout(self):
        self.__current_author = None

    # Actions when not logged in
    @staticmethod
    def get_all_categories() -> list[str]:
        return db.get_all_categories()

    def get_author_by_name(self, name: str):
        author = db.get_author_by_name(name)
        if author is not None:
            author_obj = self.__convert_to_Author(author)
            return author_obj
        return None

    def get_article_by_title(self, text: str) -> list[Article] | None:
        """
        :return: List of Article objs or None if there are no articles with the title containing text
        """
        articles = db.get_article_by_title(text)    # List of articles that its title containing text
        if len(articles) == 0:
            return None
        article_objs: list[Article] = []
        for article in articles:
            article_obj = self.__convert_to_Article(article)    # Convert to Article object
            article_objs.append(article_obj)
        return article_objs

    def get_articles_by_category(self, category: str) -> list[Article] | None:
        """
        :return: List of Article objs with matching category or None if not found
        """
        article_objs: list[Article] = []
        articles = db.get_article_by_category(category)
        for article in articles:
            article_obj = self.__convert_to_Article(article)
            article_objs.append(article_obj)
        return article_objs

    def get_articles_by_author(self, author_name: str) -> list[Article] | None:
        """
        :return: List of Article objs or None if there are no articles by the author
        :raise ValueError: If author is not found
        """
        article_objs: list[Article] = []
        author = db.get_author_by_name(author_name)     # Check if author exists
        if author is None:
            raise ValueError("Author not found")
        article_ids = author['publication_history']
        if len(article_ids) == 0:
            return None
        for ID in article_ids:
            article = db.get_article_by_id(ID)
            article_obj = self.__convert_to_Article(article)
            article_objs.append(article_obj)
        return article_objs

    def get_articles_sort_by_views(self, limit: int) -> list[Article]:
        article_objs: list[Article] = []
        articles = db.get_articles_sort_views(limit)
        for article in articles:
            article_obj = self.__convert_to_Article(article)
            article_objs.append(article_obj)
        return article_objs

    # Actions when logged in (Includes actions when not logged in)
    def add_article(self, date: str, category: str, views: int, title: str, overview: str, content: str) -> None:
        """
        :raise Exception: if the author is not logged in
        """
        # Check if the author is logged in
        if self.__current_author is None:
            raise Exception("User is not logged in")

        author_id = self.__current_author.get_id()
        article_id = db.count_all_articles() + 1
        article = Article(date, category, views, title, overview, author_id, content, article_id)
        self.__current_author.add_article(article.get_id())
        db.update_pub_history(author_id, article_id)
        db.add_articles_to_db(article)

    def set_email(self, email: str) -> None:
        """
        :raise Exception: if the author is not logged in
        """
        if self.__current_author is None:
            raise Exception("User is not logged in")
        self.__current_author.set_email(email)
        db.set_email(self.__current_author.get_id(), email)

    def set_bio(self, bio: str) -> None:
        """
        :raise Exception: if the author is not logged in
        """
        if self.__current_author is None:
            raise Exception("User is not logged in")
        self.__current_author.set_bio(bio)
        db.set_bio(self.__current_author.get_id(), bio)

    def set_expertise(self, expertise: str) -> None:
        """
        :raise Exception: if the author is not logged in
        """
        if self.__current_author is None:
            raise Exception("User is not logged in")
        self.__current_author.set_expertise(expertise)
        db.set_expertise(self.__current_author.get_id(), expertise)
