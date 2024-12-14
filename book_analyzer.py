import pandas as pd
from tabulate import tabulate

class BookAnalyzer:
    def __init__(self, books):
        self.books = books

    def analyze(self):
        df = pd.DataFrame(self.books)
        if df.empty:
            print("No books available for analysis.")
            return

        print("\nBooks by Genre:")
        print(tabulate(df["Genre"].value_counts().reset_index(), headers=["Genre", "Count"], tablefmt="fancy_grid"))

        print("\nBooks by Year:")
        print(tabulate(df["Year"].value_counts().sort_index().reset_index(), headers=["Year", "Count"], tablefmt="fancy_grid"))

        print("\nMost Frequent Author:")
        print(tabulate(df["Author"].value_counts().reset_index(), headers=["Author", "Count"], tablefmt="fancy_grid"))
    