from classes.book import Book

class Library:
    def __init__(self):
        self.books_list = []

    def add_book(self,new_book):
        if isinstance(new_book,Book):
            self.books_list.append(new_book)
        else:
            raise ValueError("can not add a stranger book")
            
    def available_books(self):
        available_books = []
        for book in self.books_list:
            if book.is_available():
                available_books.append(book.name)
        return available_books

