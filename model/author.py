from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from article import Article


class Author:
    def __init__(self, username: str, password, real_name: str):
        self.__username = username
        self.__password = password
        self.__name = real_name
        self.__email = ""
        self.__bio = ""
        self.__expertise = ""
        self.__publication_history: list[Article] = []

    # Getters
    def get_username(self) -> str: return self.__username
    def get_password(self) -> str: return self.__password   # Return the hashed password for comparison
    def get_name(self) -> str: return self.__display_name
    def get_email(self) -> str: return self.__email
    def get_bio(self) -> str: return self.__bio
    def get_expertise(self) -> str: return self.__expertise
    def get_publication_history(self) -> list[Article]: return self.__publication_history

    # Setters
    def set_password(self, password): self.__password = password    # Incase change password
    def set_name(self, name): self.__display_name = name    # Incase change display name
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