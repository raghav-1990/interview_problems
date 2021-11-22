import logging
import time
import sys

logging.basicConfig(level=logging.DEBUG)

available_books =  ["The Godfather", "To kill a mockingbird", "The Da Vinci code", "The god of small things"]
library_info = [
            {
                "name": "The Godfather",
                "author": "mario puzo",
                "check_out_time": None
            },
            {
                "name": "To kill a mockingbird",
                "author": "harper lee",
                "check_out_time": None
            },
            {
                "name": "The Da Vinci code",
                "author": "dan brown",
                "check_out_time": None
            },
            {
                "name": "The god of small things",
                "author": "arundhati roy",
                "check_out_time": None
            },
        ]       

class LMS(object):
    
    def __init__(self):
        """Init method to initialise the library with available books"""
        self.available_books = available_books
        self.library_info = library_info
        self.checked_out_books = []
        logging.info("Library has been initialised")

    def add_books_to_library(self, bookname:str, author:str):
        """Method to add books to the library
            Args:
                bookname: name of the book to the added to the library
                author: name of the author of the book being added
        """
        logging.info(f"Book {bookname} is being added to the library")
        self.available_books.append(bookname)
        self.library_info.append({
            "name": bookname,
            "author": author,
            "check_out_time": None
            })
    
    def show_all_books(self):
        """Method to show all the avaialble books in the library to the user"""
        logging.info("The following books are present in the library")
        for each in self.available_books:
            print(each)

    def checkout_book(self, bookname:str):
        """Method to checkout book from the library
         Args:
                bookname: name of the book to be checked out from the library
        """
        if bookname in self.available_books:
            logging.info(f"the following book {bookname} is being checked out")
            self.available_books.remove(bookname)
            self.checked_out_books.append(bookname)
            for each in self.library_info:
                if each["name"] == bookname:
                    each['check_out_time'] = time.time()
        else:
            logging.info(f"Book {bookname} requested by you is unavailable")

    def return_book_auto(self):
        """Method to return book to the library automatically after 2 week period"""
        if len(self.checked_out_books) > 0:
            current_time = time.time()
            for each in self.library_info:
                if each["check_out_time"] and current_time - each["check_out_time"] > 1209600:
                    each["check_out_time"] = None
                    self.available_books.append(each["name"])
                    self.checked_out_books.remove(each["name"])

    def return_book(self, bookname:str):
        """Method to return book to the library
         Args:
                bookname: name of the book to be returned to the library
        """
        logging.info(f"the following book {bookname} is being returned")
        self.available_books.append(bookname)
        self.checked_out_books.remove(bookname)
        for each in self.library_info:
            if each["name"] == bookname:
                each["check_out_time"] = None
    
    def fetch_book_info(self, bookname:str):
        """Method to provide information about a particular book
             Args:
                bookname: name of the book whose infor is required
        """
        book_info = [info for info in self.library_info if info["name"] == bookname]
        if book_info:
            print(book_info[0])
        else:
            logging.info(f"Information about the book {bookname} is not available")

def main():
    lib = LMS()
    print("Welcome to the Library.")
    while True:
        lib.return_book_auto()
        user_input = input("Please select one of the following actions:- \n 1. add \n 2. checkout \n 3. return \n 4. show_all \n 5. book_info \n 6. exit \n")
        
        if user_input == "add":
            bookname = input("Please enter name of the book to be entered to the library:- ")
            author = input("Please enter the name of the author:- ")
            lib.add_books_to_library(bookname, author)

        elif user_input == "checkout":
            bookname = str(input("Please enter name of the book to be checked out from the library:- "))
            lib.checkout_book(bookname)

        elif user_input == "return":
            bookname = input("Please enter name of the book to be returned to the library:- ")
            lib.return_book(bookname)

        elif user_input == "show_all":
            lib.show_all_books()

        elif user_input == "book_info":
            bookname = input("Please enter name of the book you need information for:- ")
            lib.fetch_book_info(bookname)

        elif user_input == "exit":
            sys.exit()

        else:
            logging.error("Please enter a valid action")

if __name__ == "__main__":
    main()
