class Article:
    def __init__(self, date: str, category: str, views: int, title: str, description: str, author_name: str, content: str):
        self.date = date
        self.categories = category
        self.views = views
        self.title = title
        self.description = description
        self.author = author_name
        self.content = content

    # Getters
    def get_date(self) -> str: return self.date
    def get_categories(self) -> str: return self.categories
    def get_views(self) -> int: return self.views
    def get_title(self) -> str: return self.title
    def get_description(self) -> str: return self.description
    def get_author(self) -> str: return self.author
    def get_content(self) -> str: return self.content

    # Setters
    def set_date(self, date: str): self.date = date
    def set_categories(self, category: str): self.categories = category
    def set_views(self, views: int): self.views = views
    def set_title(self, title: str): self.title = title
    def set_description(self, description: str): self.description = description
    def set_author(self, author: str): self.author = author
    def set_content(self, content: str): self.content = content

class Author:
    def __init__(self, username: str, password, display_name: str):
        self.__username = username
        self.__password = password
        self.__name = display_name
        self.__email = ""
        self.__bio = ""
        self.__expertise = ""
        self.__publication_history: list[Article] = []

    # Getters
    def get_name(self) -> str: return self.__name
    def get_email(self) -> str: return self.__email
    def get_bio(self) -> str: return self.__bio
    def get_expertise(self) -> str: return self.__expertise
    def get_publication_history(self) -> list[Article]: return self.__publication_history

    # Setters
    def set_name(self, name): self.__name = name
    def set_email(self, email): self.__email = email
    def set_bio(self, bio): self.__bio = bio
    def set_expertise(self, expertise): self.__expertise = expertise

    def add_article(self, article: Article):
        """
        Add an article to the publication history of the author
        :param article: Article object
        :return: None
        """
        self.__publication_history.append(article)
