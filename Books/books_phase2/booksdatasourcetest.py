import unittest
import booksdatasource

class BooksDataSourceTest:
    def setUp(self):
        self.booksDataSource = booksdatasource.BooksDataSource(books.csv, authors.csv, books_authors.csv)

    def tearDown(self):
        pass
    
    def testBookZero(self):
        self.assertEquals("All Clear", booksDataSource.book(0))

    def test_book_ID_negative(self):
        self.assertRaises(ValueError, self.bookDataSource.book, -1)

    def test_book_ID_decimal(self):
        self.assertRaises(TypeError, self.bookDataSource.book, 5.5)

    def test_book_ID_too_big(self):
        self.assertRaises(ValueError, self.bookDataSource.book, 100)

    def test_books_valid_author_ID(self):
        self.assertEquals(self.bookDataSource.books(author_id=1), ["And Then There Were None", "Murder on the Orient Express"])

    def test_books_author_ID_wrong_books(self):
        self.assertNotEquals(self.bookDataSource.books(author_id=1), ["Good Omens"])

    def test_books_author_ID_negative_ID(self):
        self.assertRaises(ValueError, self.bookDataSource.books(author_id=-1))

    def test_books_
