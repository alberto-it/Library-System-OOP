from library import Library
library = Library()

""" Possible sample test data to start out with... """

from book import Book
book = Book("1984", "George Orwell","9780451524935","Dystopian/Political Fiction","1949-06-08")
library.add_book(book)
book = Book("The Lord of the Rings", "J.R.R. Tolkien","9780261102694","Fantasy","1954-07-01")
library.add_book(book)
book = Book("Animal Farm", "George Orwell","9780261102123","Political Satire","1945-08-17")
library.add_book(book)

from user import User
user = User("Jane Doe","LIB-1001")
library.add_user(user)
user = User("John Doe","LIB-1002")
library.add_user(user)
                 
from author import Author
author = Author("George Orwell","British Novelist who advocated for democratic socialism.")
library.add_author(author)
author = Author("J.R.R. Tolkien","Renowned English writer and scholar born in South Africa in 1892.")
library.add_author(author)

print("\nWelcome to the Library Management System!")

while True:
    print("\nMain Menu:")
    print(" 1. Book Operations")
    print(" 2. User Operations")       
    print(" 3. Author Operations")            
    print(" 4. Quit")
    
    choice = input("\nEnter your choice (1-4): ")
    if   choice == '1': library.book_operations()
    elif choice == '2': library.user_operations()
    elif choice == '3': library.author_operations()
    elif choice == '4':
        print("\nExiting the Library Management System...\n")
        break
    else: print(f"\nInvalid choice. Please enter a number between 1 and 4!")