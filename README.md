
# **E-Book Management System**

## **Description**
The **E-Book Management System** is a Python-based application that provides a simple yet powerful way to manage and analyze books. It allows users to perform operations such as adding, deleting, updating, and searching for books while also offering analytical insights, such as distribution by genre, publication year, and most frequent authors.

---

## **Features**
### **1. Book Management**
- Add new books with details like title, author, genre, and year.
- Delete books based on a keyword search.
- Update book information.
- Search books by keywords (title, author, genre, or year).
- Display all stored books in a tabulated format.

### **2. Book Analytics**
- Analyze the distribution of books by genre.
- View the count of books published by year.
- Identify the most frequently listed authors.

---

## **Files in the Project**
### **1. `main.py`**
- The entry point of the application.
- Provides a user-friendly menu-driven interface for book management and analytics.
- Imports functionalities from the other modules.

### **2. `models.py`**
- Defines the abstract base class `BookBase` and its concrete implementation `Book`.
- Implements encapsulation and provides methods like `get_details()` and `matches()` to manage book attributes.
- Includes functionality for updating book details with optional input fields.

### **3. `book_manager.py`**
- Manages the CRUD operations for books.
- Reads and writes data to a CSV file (`books_db.csv`) to persist book records.
- Supports:
  - Adding new books.
  - Deleting books.
  - Updating book details.
  - Searching and displaying books in a tabulated format.

### **4. `book_analyzer.py`**
- Analyzes the stored books to provide insights.
- Uses the `pandas` library for data processing and `tabulate` for formatted output.
- Provides statistical analysis:
  - Book counts by genre.
  - Book counts by year.
  - Frequency of authors.

### **5. `books_db.csv`**
- The database file that stores book records in CSV format.
- Automatically updated when books are added, deleted, or modified.
- Includes the following columns:
  - **Title**: The title of the book.
  - **Author**: The author’s name.
  - **Genre**: The book’s genre.
  - **Year**: The year of publication.


---

## **Technologies Used**
- **Programming Language:** Python  
- **Libraries:**
  - `pandas` - For data processing and analytics.
  - `tabulate` - For displaying data in a readable tabular format.

---

## **How to Run the Project**
1. **Install Requirements**  
   Install the required Python libraries:
   ```bash
   pip install pandas tabulate
   ```

2. **Run the Application**  
   Execute the `main.py` file:
   ```bash
   python main.py
   ```

3. **Follow the On-Screen Instructions**  
   Use the menu to:
   - Add, delete, update, or search for books.
   - Perform data analysis.

---

## **Project Structure**
```
E-BookManagementSystem/
├── main.py             # Entry point of the application
├── models.py           # Defines the Book class
├── book_manager.py     # Manages CRUD operations
├── book_analyzer.py    # Performs book data analysis
└── books_db.csv        # (Auto-generated) Stores book records
```

---

## **Examples**
### **Adding a Book**
```text
Enter the book title: The Great Gatsby
Enter the author's name: F. Scott Fitzgerald
Enter the genre: Fiction
Enter the publication year: 1925
Book added successfully!
```

### **Analyzing Data**
#### Output for Genre Analysis:
```text
Books by Genre:
╒═════════════════╤═════════╕
│ Genre           │ Count   │
╞═════════════════╪═════════╡
│ Fiction         │ 15      │
│ Science Fiction │ 5       │
│ Mystery         │ 7       │
╘═════════════════╧═════════╛
```

---

## **Future Enhancements**
- Add support for managing multiple libraries or categories.
- Enable exporting analysis results to PDF or Excel.
- Implement a graphical user interface (GUI) for easier interaction.


