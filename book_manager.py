import pandas as pd
from tabulate import tabulate
from models import Book

class BookManager:
    def __init__(self, db_file="books_db.csv"):
        self.db_file = db_file
        self.books = self._load_books()


    def _load_books(self):
        try:
                df = pd.read_csv(self.db_file)
                return [Book(row["Title"], row["Author"], row["Genre"], int(row["Year"])) for _, row in df.iterrows()]
        except FileNotFoundError:
                return []


    def _save_books(self):
        df = pd.DataFrame([book.get_details() for book in self.books])
        df.to_csv(self.db_file, index=False)


    def add_book(self, book):
        if book.get_details() not in [b.get_details() for b in self.books]:
            self.books.append(book)
            self._save_books()
            print("Book added successfully!")
        else:
            print("Book already exists!")


    def delete_book(self, query):
        matching_books = [book.get_details() for book in self.books if query.lower() in str(book.get_details()).lower()]
        if not matching_books:
            print(f"No books found matching '{query}'.")
            return
        print("Matching books:")
        print(tabulate(matching_books, headers="keys", tablefmt="fancy_grid"))
        try:
            choice = int(input(f"Enter the number of the book to delete (1-{len(matching_books)}): ").strip())
            if 1 <= choice <= len(matching_books):
                book_to_delete = matching_books[choice - 1]
                self.books = [book for book in self.books if book.get_details() != book_to_delete]
                self._save_books()
                print("Book deleted successfully!")
            else:
                print("Invalid choice. Deletion cancelled.")
        except ValueError:
            print("Invalid input. Deletion cancelled.")


    def get_all_books(self):
        return [book.get_details() for book in self.books]


    def search_books(self, query):
        return [book.get_details() for book in self.books if book.matches(query)]


    def update_book(self, query):
        matching_books = [book for book in self.books if book.matches(query)]
        if not matching_books:
            print(f"No books found matching '{query}'.")
            return

        print("Matching books:")
        print(tabulate([book.get_details() for book in matching_books], headers="keys", tablefmt="fancy_grid"))

        try:
            choice = int(input(f"Enter the number of the book to update (1-{len(matching_books)}): ").strip())
            if 1 <= choice <= len(matching_books):
                book_to_update = matching_books[choice - 1]
                current_details = book_to_update.get_details()

                print("Leave the field blank to keep the current value.")

                new_title = input(f"Enter new title (current: {current_details['Title']}): ").strip()
                new_author = input(f"Enter new author (current: {current_details['Author']}): ").strip()
                new_genre = input(f"Enter new genre (current: {current_details['Genre']}): ").strip()
                new_year = input(f"Enter new year (current: {current_details['Year']}): ").strip() 

                book_to_update.set_details(
                    title=new_title ,
                    author=new_author,
                    genre=new_genre ,
                    year=int(new_year) if new_year.isdigit() else None
                )

                self._save_books()
                print("Book updated successfully!")
            else:
                print("Invalid choice. Update cancelled.")
        except ValueError:
            print("Invalid input. Update cancelled.")