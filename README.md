# Library Management System
This program simulates a library management system using Object-Oriented Programming (OOP) concepts. Here's a breakdown of the code and how to use it:

## Classes:

**Library:** This class represents the library itself. It holds information about books, users, and authors through separate lists. It provides methods to perform operations on these entities.

**Book:** This class represents a book in the library. It stores details like title, author, ISBN, genre, publication date, and availability status. It includes methods to check-out and return books.

**User:** This class represents a user registered with the library. It stores user name and library ID.

**Author:** This class represents an author whose books are in the library. It stores author name and biography.

## Files:

**main.py:** This is the main program file. It creates a Library object and presents a menu to the user for various operations.

**library.py:** This file contains the definition of the Library class.

**book.py:** This file contains the definition of the Book class.

**user.py:** This file contains the definition of the User class.

**author.py:** This file contains the definition of the Author class.

## Running the Program:

1. Save all the five files (main.py, library.py, book.py, user.py, author.py) in the same directory.
2. Open a terminal or command prompt and navigate to the directory where you saved the files.
3. Run **main.py**

## Explanation of Features:

The program offers a menu-driven interface with functionalities categorized by Books, Users, and Authors. Here's what each section offers:

### Book Operations:

* **Add a new book:** Enter details like title, author, ISBN, genre, and publication date.
* **Borrow a book:** Search for a book by title and borrow it if available (requires a user to be registered).
* **Return a book:** Search for a borrowed book by title and return it.
* **Search for a book:** Find a book by title and see if it's available.
* **Display all books:** View a list of all books in the library with details and availability status.

### User Operations:

* **Add a new user:** Register a new user with a name and library ID.
* **View user details:** Search for a registered user and see their details like borrowed books.
* **Display all users:** View a list of all registered users with their details.

### Author Operations:

* **Add a new author:** Register a new author with a name and biography.
* **View author details:** Search for a registered author and see their biography.
* **Display all authors:** View a list of all registered authors and their biographies.

## Code Breakdown:

* *main.py:* This is the main program that initiates the library object and presents the user with the main menu. It takes user input for choices and redirects to specific methods in the Library class based on the selection.

* *library.py:* This file defines the Library class which manages the overall library system. It contains methods for:
    * Adding, searching, borrowing, and returning books.
    * Adding, searching, and displaying information about users.
    * Adding, searching, and displaying information about authors.
    * Validating publication date format.
    * Printing details of all books in the library.

* *book.py:* This file defines the Book class which represents a book in the library. It stores information like title, author, ISBN, genre, publication date, and availability status. It also has methods for checking out and returning books.

* *user.py:* This file defines the User class which represents a registered user of the library. It stores information like name and library ID. It also has methods for managing borrowed books (adding and removing titles from a borrowed list).

* *author.py:* This file defines the Author class which represents an author of books in the library. It stores information like name and biography.

### Note:

* This is a basic implementation and doesn't use a database for data persistence. When you exit the program, all the data is lost.
* Error handling is included for invalid user input and data validation.
* GitHub Repository: https://github.com/alberto-it/Library-System-OOP