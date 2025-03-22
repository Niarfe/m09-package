import unittest

from booklover import BookLover

class BookLoverTestSuite(unittest.TestCase):

    def test_1_add_book(self):
        # add a book and test if it is in `book_list`.
        bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")
        bkl.add_book("ornithology", 5)

        self.assertTrue(bkl.has_read("ornithology"))
        

    def test_2_add_book(self):
        # add the same book twice. Test if it's in `book_list` only once.
        bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")
        bkl.add_book("ornithology", 5)
        bkl.add_book("ornithology", 5)

        self.assertEqual(bkl.num_books_read(), 1)


    def test_3_has_read(self):
        # pass a book in the list and test if the answer is `True`.
        bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")

        self.assertTrue(bkl.add_book("ornithology", 5))

    def test_4_has_read(self):
        # pass a book NOT in the list and use `assert False` to test the answer is `True`
        bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")
        bkl.add_book("ornithology", 5)
        
        self.assertFalse(not bkl.has_read("ornithology"), True)

    def test_5_num_books_read(self):
        # add some books to the list, and test num_books matches expected.
        bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")
        bkl.add_book("ornithology", 5)
        bkl.add_book("to kill a mockingbird", 1)
        bkl.add_book("how to make an atomic bomb", 3)
        bkl.add_book("how to make friends and influence people", 1)
        bkl.add_book("practical electronics", 5)

        self.assertEqual(bkl.num_books_read(), 5)

    def test_6_fav_books(self):
        # add some books with ratings to the list, making sure some of them have rating > 3.
        # Your test should check that the returned books have rating  > 3
        bkl = BookLover("Wile", "wile.e.coyote@gmail.com", "science")
        bkl.add_book("ornithology", 5)
        bkl.add_book("to kill a mockingbird", 1)
        bkl.add_book("how to make an atomic bomb", 3)
        bkl.add_book("how to make friends and influence people", 1)
        bkl.add_book("practical electronics", 5)

        favorites = bkl.fav_books()

        favorites.apply(lambda row: self.assertTrue(row["book_rating"] > 3), axis=1)


if __name__ == '__main__':

    unittest.main(verbosity=3)
