import pandas as pd

class BookLover:
    def __init__(self, name, email, fav_genre, num_books=0, book_list=pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.fav_genre = fav_genre
        self.num_books = num_books
        self.book_list = book_list

    def add_book(self, book_name, rating):
        """Add a book to the book list if it does not already exist"""
        assert isinstance(book_name, str), f"Expected str for book_name but got {type(book_name)}"
        assert isinstance(rating, int), f"Expected int for book_name but got {type(rating)}"
        assert rating >= 0 and rating <= 5, f"Expected rating between 0 and 5 but got {rating}"

        if not self.has_read(book_name):
            new_book = pd.DataFrame({
                "book_name": [book_name],
                "book_rating": [rating]
                })

            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)
            return True
        else:
            print(f"The book {book_name} already exists in book list!")
            return False
        
    def has_read(self, book_name):
        return book_name in self.book_list["book_name"].tolist()
    
    def num_books_read(self):
        return len(self.book_list)

    def fav_books(self):
        return self.book_list[(self.book_list["book_rating"] > 3)]

if __name__=="__main__":

    bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")

    bkl.add_book("ornithology", 5)

    print(bkl.book_list.head())
