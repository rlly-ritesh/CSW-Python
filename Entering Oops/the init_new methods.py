class Book:
    def __init__(self,title,author,pages):
        self.title = title
        self.author = author
        self.pages = pages
        print(f"Book Created : {self.title}")
    def info(self):
        return f"{self.title} by {self.author} ({self.pages} pages)"
book1 = Book("Python Programming", "Ritesh Sahoo",450)
book2 = Book("Data Science","Jane Doe",380)
print(book1.info())
print(book2.info())
