class Author:
    def __init__(self, username: str, password, real_name: str, ID: int ,email: str, gender="Other", dob: str="00/00/0000", bio:str="", expertise:str="",
                 publication_history:list[int] = []):
        self.__username = username
        self.__password = password
        self.__name = real_name
        self.__id = ID
        self.__gender = gender
        self.__dob = dob
        self.__email = email
        self.__bio = bio
        self.__expertise = expertise
        self.__publication_history: list[str] = publication_history

    # Getters
    def get_id(self) -> str: return self.__id
    def get_username(self) -> str: return self.__username
    def get_password(self) -> str: return self.__password   # Return the hashed password for comparison
    def get_name(self) -> str: return self.__name
    def get_gender(self) -> str: return self.__gender
    def get_dob(self) -> str: return self.__dob
    def get_email(self) -> str: return self.__email
    def get_bio(self) -> str: return self.__bio
    def get_expertise(self) -> str: return self.__expertise
    def get_publication_history(self) -> list[str]: return self.__publication_history

    # Setters
    def set_password(self, password): self.__password = password    # Incase change password
    def set_name(self, name): self.__name = name    # Incase change real name
    def set_gender(self, gender): self.__gender = gender
    def set_dob(self, dob): self.__dob = dob
    def set_email(self, email): self.__email = email
    def set_bio(self, bio): self.__bio = bio
    def set_expertise(self, expertise): self.__expertise = expertise

    def add_article(self, article_id: str):
        """
        Add an article to the publication history of the author
        :param article_id: ID of the article
        :return: None
        """
        self.__publication_history.append(article_id)