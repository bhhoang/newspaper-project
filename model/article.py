from __future__ import annotations
from typing import TYPE_CHECKING
import re


if TYPE_CHECKING:
    from author import Author


class Article:
    def __init__(self, date: str, category: str, views: int, title: str, overview: str, author: Author, content: str):
        self.__date = date
        self.__categories = category
        self.__views = views
        self.__title = title
        self.__overview = overview
        self.__author = author
        self.__content = content
        self.__images: list[str] = []

    # Getters
    def get_date(self) -> str: return self.__date
    def get_categories(self) -> str: return self.__categories
    def get_views(self) -> int: return self.__views
    def get_title(self) -> str: return self.__title
    def get_author(self) -> Author: return self.__author
    def get_content(self) -> str: return self.__content

    # Setters
    def set_date(self, date: str): self.__date = date
    def set_categories(self, category: str): self.__categories = category
    def set_views(self, views: int): self.__views = views
    def set_title(self, title: str): self.__title = title
    def set_author(self, author: str): self.__author = author
    def set_content(self, content: str): self.__content = content

    # Extract images path from content
    # @staticmethod
    # def extract_images(content: str) -> list[str]:
    #     """
    #     Extract images path from content
    #     :param content: Content to extract images from
    #     :return: List of paths to images
    #     """
    #     # Image in markdown: ![](path)
    #     regex = r"!\[(.*?)\]\((.*?)\)"
    #     matches = re.finditer(regex, content, re.MULTILINE)
    #
    #     for matchNum, match in enumerate(matches, start=1):
    #         for groupNum in range(0, len(match.groups())):
    #             groupNum = groupNum + 1
    #             print("Group {groupNum} found at {start}-{end}: {group}".format(groupNum=groupNum,
    #                                                                             start=match.start(groupNum),
    #                                                                             end=match.end(groupNum),
    #                                                                             group=match.group(groupNum)))
    #         printResult(match.groups())