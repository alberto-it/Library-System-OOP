class Book:
    def __init__(self, title, author, isbn, genre, pub_dt):
        self.__title = title
        self.__author = author
        self.__isbn = isbn
        self.__genre = genre
        self.__publication_date = pub_dt
        self.__available = True

    def check_out(self):
        print(f"\nDone! Just checked out {self.get_title()} by {self.get_author()}!")
        self.__available = False
        
    def return_book(self):
        print(f"\nThanks for returning {self.get_title()} by {self.get_author()}!")
        self.__available = True

    def get_title(self):
       return self.__title
    
    def set_title(self, new_title):
       self.__title = new_title

    def get_author(self):
        return self.__author

    def get_isbn(self):
        return self.__isbn

    def get_genre(self):
        return self.__genre

    def get_publication_date(self):
        return self.__publication_date

    def available(self):
        return self.__available
    
    def __str__(self):
        return f"\nTitle:\t{self.get_title()}\nAuthor:\t{self.get_author()}\nISBN:\t{self.get_isbn()}\nGenre:\t{self.get_genre()}\nPublication Date: {self.get_publication_date()}\nAvailable: {['No','Yes'][self.available()]}"