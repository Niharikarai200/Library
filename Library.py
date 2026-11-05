
# Dictionary to store book names and their status
books = {}


# Function to add a new book
def add_book():
    name = input("Enter book name: ")

    if name in books:
        print("Book already exists!")
    else:
        books[name] = "Available"
        print("Book added successfully!")


# Function to search for a book
def search_book():
    name = input("Enter book name to search: ")

    if name in books:
        print("Book:", name)
        print("Status:", books[name])
    else:
        print("Book not found!")


# Function to issue a book
def issue_book():
    name = input("Enter book name to issue: ")

    if name in books:
        if books[name] == "Available":
            books[name] = "Issued"
            print("Book issued successfully!")
        else:
            print("Book is already issued!")
    else:
        print("Book not found!")


# Function to return a book
def return_book():
    name = input("Enter book name to return: ")

    if name in books:
        if books[name] == "Issued":
            books[name] = "Available"
            print("Book returned successfully!")
        else:
            print("Book is already available!")
    else:
        print("Book not found!")


# Function to display all books
def display_books():
    if len(books) == 0:
        print("Library is empty!")
    else:
        print("\n--- Library Books ---")

        for name, status in books.items():
            print("Book:", name, "| Status:", status)


# Main function to run the library system
def main():
    while True:
        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add a Book")
        print("2. Search for a Book")
        print("3. Issue a Book")
        print("4. Return a Book")
        print("5. Display All Books")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_book()
        elif choice == "2":
            search_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            display_books()
        elif choice == "6":
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")


# Start the program
main()
