# 35. Class Book
class Book:
    def __init__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price

    def display(self):
        print(f"{self.title} by {self.author}, Price: {self.price}")

book1 = Book("Python Basics", "Alice", 299)
book1.display()
