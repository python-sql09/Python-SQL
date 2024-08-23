# Exercise 1: Create Your Own Class
class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
    
    def display(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")

# Create instances of the Book class
book1 = Book("1984", "George Orwell", "Dystopian")
book2 = Book("To Kill a Mockingbird", "Harper Lee", "Historical Fiction")
book3 = Book("The Catcher in the Rye", "J.D. Salinger", "Literary Fiction")

# Display book details
book1.display()
book2.display()
book3.display()