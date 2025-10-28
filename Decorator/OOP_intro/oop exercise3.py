# Define the Book class
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

# Create three Book objects
book1 = Book("1984", "George Orwell")
book2 = Book("To Kill a Mockingbird", "Harper Lee")
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald")

# Print their details
print(f"Book 1: {book1.title} by {book1.author}")
print(f"Book 2: {book2.title} by {book2.author}")
print(f"Book 3: {book3.title} by {book3.author}")
