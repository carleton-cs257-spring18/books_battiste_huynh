import unittest
import booksdatasource

class BooksDataSourceTest:
    def setUp(self):
        self.booksDataSource = booksdatasource.BooksDataSource(books.csv, authors.csv, books_authors.csv)

    def tearDown(self):
        pass
    
    def test_book_zero(self):
        self.assertEqual("All Clear", booksDataSource.book(0))

    def test_book_ID_negative(self):
        self.assertRaises(ValueError, self.bookDataSource.book, -1)

    def test_book_ID_decimal(self):
        self.assertRaises(TypeError, self.bookDataSource.book, 5.5)

    def test_book_ID_too_big(self):
        self.assertRaises(ValueError, self.bookDataSource.book, 100)

    def test_books_valid_author_ID(self):
        self.assertEqual(self.bookDataSource.books(author_id=1), ["And Then There Were None", "Murder on the Orient Express"])

    def test_books_author_ID_wrong_books(self):
        self.assertNotEqual(self.bookDataSource.books(author_id=1), ["Good Omens"])

    def test_books_author_ID_negative_ID(self):
        self.assertRaises(ValueError, self.bookDataSource.books(author_id=-1))

    def test_books_author_ID_decimal_ID(self): 
        self.assertRaises(TypeError, self.bookDataSource.books(author_id=1.2))
        
    def test_books_author_ID_too_big(self): 
        self.assertRaises(ValueError, self.bookDataSource.books(author_id=90))
        
    def test_books_valid_search_text(self):
        self.assertEqual(self.bookDataSource.books(search_text="mirror"), ["Mirror Dance"])
        
    def test_books_search_text_no_result(self):
        self.assertEqual(self.bookDataSource.books(search_text="phuoc"), [])
    
    def test_books_search_text_wrong_result(self):
        self.assertNotEqual(self.bookDataSource.books(search_text="Chase"), ["Wuthering Heights"])
    
    def test_books_start_year(self):
        self.assertEqual(self.bookDataSource.books(start_year = 2015), ['The Fifth Season', 'The Obelisk Gate', 'The Power', 'The Stone Sky'])
        
    def test_books_start_year_wrong_books(self):
        self.assertNotEqual(self.bookDataSource.books(start_year = 1990), [])
        
    def test_books_end_year(self):
        self.assertEqual(self.bookDataSource.books(start_year = 1830), ['Emma', 'Pride and Prejudice', 'Sense and Sensibility'])
        
    def test_books_end_year_wrong_books(self):
        self.assertNotEqual(self.bookDataSource.books(start_year = 2010), ['Emma', 'Pride and Prejudice', 'Sense and Sensibility'])
    
    def test_books_sort_by_default(self):
        self.assertEqual(self.bookDataSource.books(start_year = 2015), ['The Fifth Season', 'The Obelisk Gate', 'The Power', 'The Stone Sky'])
        
    def test_books_sort_by_year(self)
        self.assertEqual(self.bookDataSource.books(start_year = 2015, sort_by = 'year'), ['The Fifth Season', 'The Obelisk Gate', 'The Stone Sky', 'The Power'])
        
    def test_books_sort_by_default_wrong_order(self):
        self.assertNotEqual(self.bookDataSource.books(start_year = 2015), ['The Fifth Season', 'The Power', 'The Stone Sky', 'The Obelisk Gate'])
        
    def test_books_sort_by_year_wrong_order(self):
        self.assertNotEqual(self.bookDataSource.books(start_year = 2015, sort_by = 'year'), ['The Power', 'The Fifth Season', 'The Obelisk Gate', 'The Stone Sky'])
        
    