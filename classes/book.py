class Book:
    total_books = 0
    def __init__(self,name,auther,copies):
        if copies < 1:
            raise ValueError("copies must be atleast 1")
        self.name = name
        self.auther = auther
        self.copies = copies
        self.available = self.copies
        Book.total_books += 1

    def borrow(self):
        if self.is_available():
            self.available -= 1 
        else:
            raise ValueError("no copies available")

    def return_book(self):
        if self.available == self.copies:
            raise ValueError("all books are in")
        self.available += 1

    def is_available(self):
        if self.available < 1:
            return False
        return True

    def __str__(self):
        return f"{self.name} by {self.auther} ({self.available}/{self.copies} available)"
     









        



