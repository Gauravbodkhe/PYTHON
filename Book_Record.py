def read_books():
    with open("books.txt", "r") as file:
        return [line.strip().split(",") for line in file]

def write_books(books):
    with open("books.txt", "w") as file:
        for book in books:
            file.write(",".join(book) + "\n")

def search_books(books, key, value):
    results = [book for book in books if book[key].lower() == value.lower()]
    if results:
        print("Matching records:")
        for book in results:
            print(f"Title: {book[0]}, Author: {book[1]}, Year: {book[2]}, Price: {book[3]}")
    else:
        print("No matching records found.")

def update_book(books, title, field, new_value):
    for book in books:
        if book[0].lower() == title.lower():
            if field == "title":
                book[0] = new_value
            elif field == "author":
                book[1] = new_value
            elif field == "year":
                book[2] = new_value
            elif field == "price":
                book[3] = new_value
            print("Book updated successfully.")
            return
    print("Book not found.")

def append_book(books, new_book):
    books.append(new_book)
    print("New book added successfully.")

def main():
    while True:
        print("\n1. Search by Title\n2. Search by Author\n3. Update Book\n4. Add New Book\n5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter title to search: ")
            books = read_books()
            search_books(books, 0, title)
        elif choice == "2":
            author = input("Enter author to search: ")
            books = read_books()
            search_books(books, 1, author)
        elif choice == "3":
            title = input("Enter title of the book to update: ")
            field = input("Enter field to update (title/author/year/price): ")
            new_value = input(f"Enter new {field}: ")
            books = read_books()
            update_book(books, title, field, new_value)
            write_books(books)
        elif choice == "4":
            new_book = [
                input("Enter title: "),
                input("Enter author: "),
                input("Enter year: "),
                input("Enter price: ")
            ]
            books = read_books()
            append_book(books, new_book)
            write_books(books)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")


# Run the program
if __name__ == "__main__":
    main()

    '''Python Programming,John Doe,2021,500
    Data Science,Jane Smith,2020,700
    Algorithms,Robert Brown,2001,600
    Sangram,Gaurav,2025,20,000
    '''