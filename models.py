from abc import ABC, abstractmethod

class BookBase(ABC):
    @abstractmethod
    def get_details(self):
        pass

    @abstractmethod
    def matches(self, query):
        pass

class Book(BookBase):
    def __init__(self, title, author, genre, year):
        self.__title = title
        self.__author = author
        self.__genre = genre
        self.__year = year

    def get_details(self):
        return {
            "Title": self.__title,
            "Author": self.__author,
            "Genre": self.__genre,
            "Year": self.__year
        }

    def matches(self, query):
        query_lower = query.lower()
        return (
            query_lower in self.__title.lower() or
            query_lower in self.__author.lower() or
            query_lower in self.__genre.lower() or
            str(self.__year) == query
        )

    def set_details(self, title=None, author=None, genre=None, year=None):
        if title:
            self.__title = title
        if author:
            self.__author = author
        if genre:
            self.__genre = genre
        if year:
            self.__year = year