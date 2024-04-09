from book import Book
from user import User
from author import Author

import re

class Library:
    def __init__(self):
        self.books = []
        self.users = []
        self.authors = []

    def valid_pub_date(self, pub_date):
        return bool(re.match(r"^\d{4}-\d{2}-\d{2}$", pub_date))

    def book_operations(self):
        print("\nBook Operations:")
        print(" 1. Add a new book")
        print(" 2. Borrow a book")
        print(" 3. Return a book")
        print(" 4. Search for a book")
        print(" 5. Display all books")

        while True:
            choice = input("\nEnter your choice (1-5): ")
            if choice == '1':
                author_name = input("\nEnter the Author of the Book to be Added: ")
                author = self.find_author(author_name)
                if author:
                    print(f"\nBTW, here is the library's bio on {author_name}: {author.get_biography()}")
                    title = input(f"\nEnter the Book of {author_name} to be Added: ")
                    isbn = input(f"\nEnter the ISBN for {title}: ")
                    genre = input("\nEnter the Genre: ")
                    pub_dt = input("\nEnter the Publication Date (YYYY-MM-DD): ")
                    while not self.valid_pub_date(pub_dt): pub_dt = input("\nPlease redo with Date Format YYYY-MM-DD: ")
                    self.add_book(Book(title, author_name, isbn, genre, pub_dt))
                    print("\nThe book", title, "by", author_name, "has been added!")
                else: print("\nPlease add author", author_name, "to the library system prior to adding book!")
                break

            if choice == '2':
                user = self.find_user(input("\nEnter the Name of the Borrower/User: "))
                if user:
                    title = input("\nEnter the Title of the Book to Borrow: ")
                    if self.borrow_book(title): user.borrowed_book(title)
                else:  print("\nUser must be in the library system in order to borrow a book!")
                break

            if choice == '3':
                title = input("\nEnter the Title of the Book to Return: ")
                if self.return_book(title):
                    user = self.find_borrower(title)
                    user.returned_book(title)
                break

            if choice == '4':
                title = input("\nEnter the Title of the Book to Find: ")
                book = self.find_books(title)
                if book: print(book)
                else: print("\nBook Title", title, "was Not Found in the Library System!")
                break
                
            if choice == '5':
                for book in self.books: print(book)
                if not self.books: print("\nThere are currently No Books in the Library System!")
                break
                
            print(f"\nInvalid choice. Please enter a number between 1 and 5!")

    def add_book(self, book):
        self.books.append(book)

    def find_books(self, title):
        for book in self.books:
            if book.get_title() == title: return book
        return None
    
    def borrow_book(self, title):
        book = self.find_books(title)
        if book:
            if book.available():
                book.check_out()
                return True
            else: print(f"\n{title} is currently Not Available!")
        else: print(f"\n{title} does Not Exist in the Library System!")
        return False

    def return_book(self, title):
        book = self.find_books(title)
        if book:
            if book.available(): print("\nHmm? Cannot return a book that hasn't been checked out yet!")
            else:
                book.return_book()
                return True
        else: print(f"\n{title} was Not Found in our Library System!")
        return False
    
    def find_borrower(self, title):
        for user in self.users:
            if title in user.get_borrowed_list(): return user
        return None    

    def add_user(self, user):
        self.users.append(user)

    def find_user(self, name):
        for user in self.users:
            if user.get_name() == name: return user
        return None

    def user_operations(self):
        print("\nUser Operations::")
        print(" 1. Add a new user")
        print(" 2. View user details")        
        print(" 3. Display all users")

        while True:    
            choice = input("\nEnter your choice (1-3): ")
            if choice == '1':
                name = input("\nEnter User Name: ")
                library_id = input(f"\nEnter Library ID for user {name}: ")
                self.add_user(User(name, library_id))
                print("\nUser", name, "has been added!")
                break

            if choice == '2':
                name = input("\nEnter the Name of the User to View: ")
                user = self.find_user(name)
                if user: print(user)
                else: print("\nUser", name, "was Not Found in the Library System!")
                break

            if choice == '3':
                for user in self.users: print(user)
                if not self.users: print("\nThere are currently No Users in the Library System!")
                break

            print(f"\nInvalid choice. Please enter a number between 1 and 3")

    def add_author(self, author):
        self.authors.append(author)

    def find_author(self, name):
        for author in self.authors:
            if author.get_name() == name: return author
        return None

    def author_operations(self):
        print("\nAuthor Operations::")
        print(" 1. Add a new author")
        print(" 2. View author details")        
        print(" 3. Display all authors")

        while True:
            choice = input("\nEnter your choice (1-3): ")
            if choice == '1':
                name = input("\nEnter Author's Name: ")
                bio = input(f"\nEnter {name}'s Biography: ")
                self.add_author(Author(name, bio))
                print("\nAuthor", name, "has been added!")
                break
                
            if choice == '2':
                name = input("\nEnter the name of the author to view: ")
                author = self.find_author(name)
                if author: print(author)
                else: print("\nAuthor", name, "was Not Found in the Library System!")
                break

            if choice == '3':
                for author in self.authors: print(author)
                if not self.authors: print("\nThere are currently No Authors in the Library System!")
                break
                
            print(f"\nInvalid choice. Please enter a number between 1 and 3")