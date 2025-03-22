from booklover import BookLover

bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")
bkl.add_book("ornithology", 5)

assert bkl.has_read("ornithology")

print("Number of books read:", bkl.num_books_read())


