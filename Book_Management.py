# Function to read data from the file
def read_books():
    books = []
    try:
        with open("book.txt", "r") as file:
            # Skip the header line
            next(file)
            for line in file:
                title, author, year, price = line.strip().split(",")
                books.append({
                    "Title": title,
                    "Author": author,
                    "Year": int(year),
                    "Price": float(price)
                })
        return books
    except FileNotFoundError:
        print("Error: File 'books.txt' not found!")
        return []

# Function to search for books by title or author
def search_books(books):
    search_term = input("Enter title or author to search: ").lower()
    results = []
    for book in books:
        if search_term in book["Title"].lower() or search_term in book["Author"].lower():
            results.append(book)
    if results:
        print("\nSearch Results:")
        for book in results:
            print(f"Title: {book['Title']}, Author: {book['Author']}, Year: {book['Year']}, Price: ${book['Price']:.2f}")
    else:
        print("No matching books found.")

# Function to update details of a book
def update_book(books):
    title = input("Enter the title of the book to update: ")
    found = False
    for book in books:
        if book["Title"].lower() == title.lower():
            print(f"Current Details: {book}")
            new_author = input("Enter new author (leave blank to keep current): ")
            new_year = input("Enter new year (leave blank to keep current): ")
            new_price = input("Enter new price (leave blank to keep current): ")
            
            if new_author:
                book["Author"] = new_author
            if new_year:
                try:
                    book["Year"] = int(new_year)
                except ValueError:
                    print("Error: Year must be an integer!")
                    return
            if new_price:
                try:
                    book["Price"] = float(new_price)
                except ValueError:
                    print("Error: Price must be a number!")
                    return
            
            found = True
            print("Book details updated successfully!")
            break
    if not found:
        print("Book not found!")

# Function to append new book details to the file
def append_book():
    title = input("Enter title: ")
    author = input("Enter author: ")
    year = input("Enter year: ")
    price = input("Enter price: ")
    
    try:
        year = int(year)
        price = float(price)
    except ValueError:
        print("Error: Year must be an integer, and price must be a number!")
        return
    
    with open("books.txt", "a") as file:
        file.write(f"\n{title},{author},{year},{price}")
    print("New book added successfully!")

# Main menu
def main():
    while True:
        print("\nBook Records Management System")
        print("1. Search Books")
        print("2. Update Book Details")
        print("3. Add New Book")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            books = read_books()
            search_books(books)
        elif choice == "2":
            books = read_books()
            update_book(books)
            # Write updated data back to the file
            with open("books.txt", "w") as file:
                file.write("Title,Author,Year,Price\n")
                for book in books:
                    file.write(f"{book['Title']},{book['Author']},{book['Year']},{book['Price']}\n")
        elif choice == "3":
            append_book()
        elif choice == "4":
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    main()