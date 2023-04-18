import re


class Article:
    def __init__(self, date: str, category: str, title: str, overview: str, author_id: int, content: str, ID: int, preview_img: str,
                 views: int = 0):
        self.__date = date
        self.__category = category
        self.__views = views
        self.__title = title
        self.__overview = overview
        self.__author = author_id
        self.__content = content
        self.__id = ID
        self.__images: list[str] = self.__extract_images(content)
        self.__preview_img = preview_img

    # Getters
    def get_id(self) -> int: return self.__id
    def get_date(self) -> str: return self.__date
    def get_category(self) -> str: return self.__category
    def get_views(self) -> int: return self.__views
    def get_title(self) -> str: return self.__title
    def get_overview(self) -> str: return self.__overview
    def get_author(self) -> int: return self.__author
    def get_content(self) -> str: return self.__content
    def get_images(self) -> list[str]: return self.__images
    def get_preview_img(self) -> str: return self.__preview_img

    # Setters
    def set_date(self, date: str): self.__date = date
    def set_categories(self, category: str): self.__category = category
    def set_views(self, views: int): self.__views = views
    def set_title(self, title: str): self.__title = title
    def set_overview(self, overview: str): self.__overview = overview
    def set_author(self, author_id: str): self.__author = author_id
    def set_content(self, content: str): self.__content = content
    def set_preview_img(self, preview_img: str): self.__preview_img = preview_img

    # Extract images path from content
    @staticmethod
    def __addResult(array_start, array_dest):
        array_dest.append(array_start[1])

    def __extract_images(self, content: str) -> list[str]:
        """
        Extract images path from content
        :param content: Content to extract images from
        :return: List of path to image
        """
        # Image in markdown: ![](path)
        regex = r"!\[(.*?)\]\((.*?)\)"
        matches = re.finditer(regex, content, re.MULTILINE)
        images = []
        for matchNum, match in enumerate(matches, start=1):
            self.__addResult(match.groups(), images)
        return images
