
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    @classmethod
    def make_default(cls):
        return cls("Unknown", "Unknown")


book1 = Book.make_default()

print("Title:", book1.title)
print("Author:", book1.author)
