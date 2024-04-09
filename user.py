class User:
    def __init__(self, name, library_id):
        self.__name = name
        self.__library_id = library_id

        self.__borrowed_books = []
    
    def get_name(self):
        return self.__name

    def get_library_id(self):
        return self.__library_id
    
    def borrowed_book(self, book_title):
        self.__borrowed_books.append(book_title)

    def returned_book(self, book_title):
        self.__borrowed_books.remove(book_title)

    def get_borrowed_list(self):
        return self.__borrowed_books
    
    def __str__(self):
        return f"\nName: {self.get_name()}\nLibrary ID: {self.get_library_id()}\nBorrowed Books: {', '.join(self.get_borrowed_list())}"