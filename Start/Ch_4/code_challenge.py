# Python code​​​​​​‌‌‌​‌‌‌​​‌​‌‌‌​‌​‌​‌​‌​​​ below
# Use print("messages...") to debug your solution.

show_expected_result = False
show_hints = False

class Book():
    def __init__(self, title, author, pages, cover, antique, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.cover = cover
        self.antique = antique
        self.price = price

    # TODO: Implement the str and repr functions
    def __str__(self):
        return f"{self.title} by {self.author}: {self.pages}, {self.cover}, {self.price}"

    def __repr__(self):
        return f"<Book:{self.title}:{self.author}:{self.pages}:{self.cover}:{self.antique}:{self.price}>"

    # TODO: Implement the adjustedprice attribute
    def __getattr__(self, attr):
        if attr == "adjustedprice":
            val = self.price
            if self.antique == True:
                val += 10.0
            if self.cover == "Paperback":
                val -= 2.0
            return val

    # TODO: Implement comparisons <, >, <=, >=
    def __ge__(self, other):
        return self.pages >= other.pages

    def __gt__(self, other):
        return self.pages > other.pages

    def __le__(self, other):
        return self.pages <= other.pages

    def __lt__(self, other):
        return self.pages < other.pages

# This is how your code will be called.
# You can edit these values to try different testing cases (don't change var names)
title1 = "War and Peace"
author1 = "Leo Tolstoy"
pages1 = 1225
booktype1 = "Hard" # "Hard" or "Paperback"
antique1 = True
price1 = 29.95

title2 = "Brave New World"
author2 = "Aldous Huxley"
pages2 = 311
booktype2 = "Paperback" # "Hard" or "Paperback"
antique2 = False
price2 = 32.50

# DON'T CHANGE THIS CODE
book1 = Book(title1, author1, pages1, booktype1, antique1, price1)
print(book1)
book2 = Book(title2, author2, pages2, booktype2, antique2, price2)
print(book2)

print(str(book1))
print(repr(book1))
print(f"adjustedprice: {book1.adjustedprice:.2f} regular price: {book1.price}")
print(f"adjustedprice: {book2.adjustedprice:.2f} regular price: {book2.price}")
print(book1 < book2)
