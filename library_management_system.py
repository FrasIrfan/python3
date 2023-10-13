class Library:
    def __init__(self):
        self.num_books = 0   
        self.book_list = []  
    
    def add_book(self, book_title):
        self.book_list.append(book_title)
        self.num_books += 1
        print(f"{book_title} has been added to the library")
    
    def print_all_books(self):
        print("The books in the library are:")
        for book in self.book_list:
            print(book)
    
    def get_num_books(self):
        return self.num_books

if __name__ == "__main__":
    library = Library()
    library.add_book(input("Enter the Book Name:"))
    # library.add_book("The Lord of the Rings")
    # library.add_book("The Hunger Games")
    library.print_all_books()
    print(f"The number of books in the library is {library.get_num_books()}")
