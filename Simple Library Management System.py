# Simple Library Management System
# Using Python basics, control flow, and data structures

# Sample book collection
books = [
    {"id": 1, "title": "Python Basics", "author": "John Doe", "available": True},
    {"id": 2, "title": "Data Structures", "author": "Jane Smith", "available": True},
    {"id": 3, "title": "Algorithms in Python", "author": "Mike Johnson", "available": True},
]

# Borrowed books list
borrowed_books = []

# Function to display all books
def display_books():
    print("\nAvailable Books:")
    for book in books:
        status = "Available" if book["available"] else "Not Available"
        print(f"ID: {book['id']} | Title: {book['title']} | Author: {book['author']} | Status: {status}")

# Function to borrow a book
def borrow_book():
    display_books()
    book_id = int(input("\nEnter the ID of the book you want to borrow: "))
    for book in books:
        if book["id"] == book_id:
            if book["available"]:
                book["available"] = False
                borrowed_books.append(book)
                print(f"You have borrowed '{book['title']}'")
            else:
                print("Sorry, this book is already borrowed.")
            return
    print("Book ID not found.")

# Function to return a book
def return_book():
    if not borrowed_books:
        print("No books are currently borrowed.")
        return
    print("\nBorrowed Books:")
    for book in borrowed_books:
        print(f"ID: {book['id']} | Title: {book['title']}")
    book_id = int(input("\nEnter the ID of the book you want to return: "))
    for book in borrowed_books:
        if book["id"] == book_id:
            book["available"] = True
            borrowed_books.remove(book)
            print(f"You have returned '{book['title']}'")
            return
    print("Book ID not found in borrowed books.")

# Function to add a new book
def add_book():
    title = input("Enter the book title: ")
    author = input("Enter the author name: ")
    # Automatically generate a new ID
    book_id = max(book["id"] for book in books) + 1 if books else 1
    new_book = {"id": book_id, "title": title, "author": author, "available": True}
    books.append(new_book)
    print(f"Book '{title}' by {author} added with ID {book_id}.")

# Main program loop
while True:
    print("\nLibrary Management System")
    print("1. Display all books")
    print("2. Borrow a book")
    print("3. Return a book")
    print("4. Add a new book")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    if choice == "1":
        display_books()
    elif choice == "2":
        borrow_book()
    elif choice == "3":
        return_book()
    elif choice == "4":
        add_book()
    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
