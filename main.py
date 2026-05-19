class Library:

    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def display_books(self):
        print(f"Books in {self.name} Library:")
        for book in self.books:
            print(f"- {book}")
    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"{book} has been removed from the library.")
        else:
            print(f"{book} is not found in the library.")
    def lend_book(self, book):
        if book in self.books:
            self.books.remove(book)
            print(f"You have borrowed {book}.")
        else:
            print(f"{book} is not available for borrowing.")
    def return_book(self, book):
        self.books.append(book)
        print(f"You have returned {book}.")
lib=Library("City Library")
while True:
    print("\nLibrary Management System")
    print("1. Add Book")
    print("2. Display Books")
    print("3. Remove Book")
    print("4. Lend Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        book_name = input("Enter the name of the book to add: ")
        lib.add_book(book_name)
    elif choice == '2':
        lib.display_books()
    elif choice == '3':
        book_name = input("Enter the name of the book to remove: ")
        lib.remove_book(book_name)
    elif choice == '4':
        book_name = input("Enter the name of the book to lend: ")
        lib.lend_book(book_name)
    elif choice == '5':
        book_name = input("Enter the name of the book to return: ")
        lib.return_book(book_name)
    elif choice == '6':
        print("Exiting the Library Management System.")
        break
    else:
        print("Invalid choice. Please try again.")
