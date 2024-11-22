from  save_all_books import save_all_books


def add_book(all_books):
    title = input("Enter Book Title: ")
    author = input("Enter Author Name: ")
    isbn = input("Enter ISBN Number: ")
    published_year = int(input("Enter Publishing Year: "))
    price = int(input("Enter Book Price: "))
    quantity = int(input("Enter Quantity Number: "))

    book = {
        "title": title,
        "author": author,
        "isbn": isbn,
        "year": published_year,
        "price": price,
        "quantity": quantity
    }

    all_books.append(book)
    save_all_books(all_books)

    print("Book added successfully!")

    return all_books