from book_manager import BookManager
from book_analyzer import BookAnalyzer
from models import Book
from tabulate import tabulate

if __name__== "__main__":
    print("Welcome to the Book Management System!")
    manager = BookManager()

    while True:
        try:
            print("\nOptions:")
            print("1. Add a new book")
            print("2. Delete a book")
            print("3. Display all books")
            print("4. Search for a book")
            print("5. Update a book ")
            print("6. Analyze book data")
            print("7. Exit")
            choice = input("Enter your choice (1-7): ").strip()

            if choice == "1":
                title = input("Enter the book title: ").strip()
                author = input("Enter the author's name: ").strip()
                genre = input("Enter the genre: ").strip()
                year = input("Enter the publication year: ").strip()
                if year.isdigit():
                    manager.add_book(Book(title, author, genre, int(year)))
                else:
                    print("Invalid year. Please enter a numeric value for the year.")
            elif choice == "2":
                query = input("Enter a keyword to search for the book to delete: ").strip()
                manager.delete_book(query)

            elif choice == "3":
                books = manager.get_all_books()
                if books:
                    print(tabulate(books, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("No books available.")

            elif choice == "4":
                query = input("Enter a keyword to search for books: ").strip()
                results = manager.search_books(query)
                if results:
                    print(tabulate(results, headers="keys", tablefmt="fancy_grid"))
                else:
                    print("No matching books found.")
                    
            elif choice == "5":
                query = input("Enter a keyword to search for the book to update: ").strip()
                manager.update_book(query)

            elif choice == "6":
                analyzer = BookAnalyzer(manager.get_all_books())
                analyzer.analyze()


            elif choice == "7":
                print("Exiting the Book Management System. Goodbye!")
                break

            else:
                print("Invalid choice. Please enter a number between 1 and 7.")

        except Exception as e:
            print(f"An error occurred: {e}")