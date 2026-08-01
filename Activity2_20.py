class book:

    def __init__(self, book, pages):
        self.book = book
        self.pages = pages

    def display(self):
        print("Pages:", self.pages)

harry_potter = book("harry_potter", 1000)
harry_potter.display()