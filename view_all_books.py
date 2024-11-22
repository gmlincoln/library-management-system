def view_books(all_books):

    if all_books  != []:

        for book in all_books:
            print(f"\nBook Title: {book['title']} || Author: {book['author']} || ISBN Number: {book['isbn']} || Publishing Year: {book['year']} || Price: {book['price']} || Quantity: {book['quantity']} \n")
            
    else:
        print("\nNo books found in the system.\n")