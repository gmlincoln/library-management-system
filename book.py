from add_books import add_book
from view_all_books import view_books


all_books = [] 

while True:
    print("Welcome to Library Management System")
    print("0. Exit")
    print("1. Add a Book ")
    print("2. View All Books")

    choice = input("Enter your choice : ")
    
    if choice == "0":
        print("Thanks for using Library Management System")
        break

    elif choice == "1":
        all_books = add_book(all_books)
    
    elif choice == "2":
        view_books(all_books)

    else:
        print("Invalid choice! Please try again.\n")