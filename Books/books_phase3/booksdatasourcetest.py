import unittest
import booksdatasource

class BooksDataSourceTest(unittest.TestCase):
    def setUp(self):
        self.booksDataSource = booksdatasource.BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')

    def tearDown(self):
        pass
    
    '''
        Unit tests for book
    '''
    def test_book_zero(self):
        self.assertEqual({'id':0, 'title':'All Clear', 'publication_year':2010}, self.booksDataSource.book(0))
        
    def test_book_ID_valid(self):
        self.assertEqual({'id':2, 'title':'Beloved', 'publication_year':1987}, self.booksDataSource.book(2))
    
    def test_book_ID_incorrect_result(self):
        self.assertNotEqual({'id':0, 'title':'All Clear', 'publication_year':2010}, self.booksDataSource.book(2))

    def test_book_ID_negative(self):
        self.assertRaises(ValueError, self.booksDataSource.book, -1)

    def test_book_ID_too_big(self):
        self.assertRaises(ValueError, self.booksDataSource.book, 100)
        
    '''
        Unit tests for books
    '''

    def test_books_no_parameters(self):
        self.assertEqual([{'id':30, 'title':'1Q84', 'publication_year':2009}, {'id':31, 'title':'A Wild Sheep Chase', 'publication_year':1982}, {'id':0, 'title':'All Clear', 'publication_year':2010}, {'id':1, 'title':'And Then There Were None', 'publication_year':1939}, {'id':2, 'title':'Beloved', 'publication_year':1987}, {'id':3, 'title':'Blackout', 'publication_year':2010}, {'id':43, 'title':'Bleak House', 'publication_year':1852}, {'id':4, 'title':'Elmer Gantry', 'publication_year':1927}, {'id':5, 'title':'Emma', 'publication_year':1815}, {'id':6, 'title':'Good Omens', 'publication_year':1990}, {'id':44, 'title':'Great Expectations', 'publication_year':1860}, {'id':32, 'title':'Hard-Boiled Wonderland and the End of the World', 'publication_year':1985}, {'id':7, 'title':'Jane Eyre', 'publication_year':1847}, {'id':8, 'title':'Leave it to Psmith', 'publication_year':1923}, {'id':9, 'title':'Love in the Time of Cholera', 'publication_year':1985}, {'id':10, 'title':'Main Street', 'publication_year':1920}, {'id':41, 'title':'Middlemarch', 'publication_year':1871}, {'id':11, 'title':"Midnight's Children", 'publication_year':1981}, {'id':12, 'title':'Mirror Dance', 'publication_year':1994}, {'id':13, 'title':'Moby Dick', 'publication_year':1851}, {'id':14, 'title':'Murder on the Orient Express', 'publication_year':1934}, {'id':33, 'title':'My Ántonia', 'publication_year':1918}, {'id':15, 'title':'Neverwhere', 'publication_year':1996}, {'id':34, 'title':'O Pioneers!', 'publication_year':1913}, {'id':16, 'title':'Omoo', 'publication_year':1847}, {'id':17, 'title':'One Hundred Years of Solitude', 'publication_year':1967}, {'id':18, 'title':'Pride and Prejudice', 'publication_year':1813}, {'id':36, 'title':'Rebecca', 'publication_year':1938}, {'id':19, 'title':'Right Ho, Jeeves', 'publication_year':1934}, {'id':20, 'title':'Sense and Sensibility', 'publication_year':1813}, {'id':21, 'title':'Shards of Honor', 'publication_year':1986}, {'id':42, 'title':'Silas Marner', 'publication_year':1861}, {'id':22, 'title':'Sula', 'publication_year':1973}, {'id':23, 'title':'The Code of the Woosters', 'publication_year':1938}, {'id':37, 'title':'The Fifth Season', 'publication_year':2015}, {'id':38, 'title':'The Obelisk Gate', 'publication_year':2015}, {'id':35, 'title':'The Power', 'publication_year':2016}, {'id':24, 'title':'The Satanic Verses', 'publication_year':1988}, {'id':46, 'title':'The Spy Who Came in From the Cold', 'publication_year':1963}, {'id':39, 'title':'The Stone Sky', 'publication_year':2015}, {'id':25, 'title':'The Tenant of Wildfell Hall', 'publication_year':1848}, {'id':26, 'title':'Thief of Time', 'publication_year':1996}, {'id':40, 'title':'Three Men in a Boat (to Say Nothing of the Dog)', 'publication_year':1889}, {'id':45, 'title':'Tinker, Tailor, Soldier, Spy', 'publication_year':1974}, {'id':27, 'title':'To Say Nothing of the Dog', 'publication_year':1997}, {'id':28, 'title':'Villette', 'publication_year':1853}, {'id':29, 'title':'Wuthering Heights', 'publication_year':1847}], self.booksDataSource.books())
    
    def test_books_valid_author_ID(self):
        self.assertEqual(self.booksDataSource.books(author_id=1), [{'id':1, 'title':"And Then There Were None", 'publication_year':1939}, {'id':14, 'title':'Murder on the Orient Express', 'publication_year':1934}])

    def test_books_author_ID_wrong_books(self):
        self.assertNotEqual(self.booksDataSource.books(author_id=1), [{'id':6, 'title':'Good Omens', 'publication_year':1990}])

    def test_books_author_ID_negative_ID(self):
        self.assertRaises(ValueError, self.booksDataSource.books, author_id=-1)
    
    def test_books_author_ID_too_big(self): 
        self.assertRaises(ValueError, self.booksDataSource.books, author_id = 90)
        
    def test_books_valid_search_text(self):
        self.assertEqual(self.booksDataSource.books(search_text="mirror"), [{'id':12, 'title':'Mirror Dance', 'publication_year':1994}])
        
    def test_books_search_text_no_result(self):
        self.assertEqual(self.booksDataSource.books(search_text="phuoc"), [])
    
    def test_books_search_text_wrong_result(self):
        self.assertNotEqual(self.booksDataSource.books(search_text="Chase"), [{'id':29, 'title':'Wuthering Heights', 'publication_year':1847}])
    
    def test_books_start_year(self):
        self.assertEqual(self.booksDataSource.books(start_year = 2015), [{'id':37, 'title':'The Fifth Season', 'publication_year':2015}, {'id':38, 'title':'The Obelisk Gate', 'publication_year':2015}, {'id':35, 'title':'The Power', 'publication_year':2016}, {'id':39, 'title':'The Stone Sky', 'publication_year':2015}])
        
    def test_books_start_year_wrong_books(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 1990), [])
        
    def test_books_end_year(self):
        self.assertEqual(self.booksDataSource.books(end_year = 1830), [{'id':5, 'title':'Emma', 'publication_year':1815}, {'id':18, 'title':'Pride and Prejudice', 'publication_year':1813}, {'id':20, 'title':'Sense and Sensibility', 'publication_year':1813}])
        
    def test_books_end_year_wrong_books(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 2010), [{'id':5, 'title':'Emma', 'publication_year':1815}, {'id':18, 'title':'Pride and Prejudice', 'publication_year':1813}, {'id':20, 'title':'Sense and Sensibility', 'publication_year':1813}])
        
    def test_books_sort_by_default_wrong_order(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 2015), [{'id':37, 'title':'The Fifth Season', 'publication_year':2015}, {'id':35, 'title':'The Power', 'publication_year':2016}, {'id':39, 'title':'The Stone Sky', 'publication_year':2015}, {'id':38, 'title':'The Obelisk Gate', 'publication_year':2015}])
        
    def test_books_sort_by_year(self):
        self.assertEqual(self.booksDataSource.books(start_year = 2015, sort_by = 'year'), [{'id':37, 'title':'The Fifth Season', 'publication_year':2015}, {'id':38, 'title':'The Obelisk Gate', 'publication_year':2015}, {'id':39, 'title':'The Stone Sky', 'publication_year':2015}, {'id':35, 'title':'The Power', 'publication_year':2016}])
        
    def test_books_sort_by_year_wrong_order(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 2015, sort_by = 'year'), [{'id':35, 'title':'The Power', 'publication_year':2016}, {'id':37, 'title':'The Fifth Season', 'publication_year':2015}, {'id':38, 'title':'The Obelisk Gate', 'publication_year':2015}, {'id':39, 'title':'The Stone Sky', 'publication_year':2015}])

    def test_books_author_ID_and_start_year(self):
        self.assertEqual(self.booksDataSource.books(author_id=1, start_year=1939), [{'id':1, 'title':"And Then There Were None", 'publication_year':1939}])

    def test_books_search_text_and_end_year(self):
        self.assertEqual(self.booksDataSource.books(end_year=1830, search_text='and'), [{'id':18, 'title':'Pride and Prejudice', 'publication_year':1813}, {'id':20, 'title':'Sense and Sensibility', 'publication_year':1813}])
        
    '''
        Unit test for author
    '''
    
    def test_author_ID_valid(self):
        self.assertEqual({'id':18, 'last_name':'Alderman', 'first_name':'Naomi', 'birth_year':1974, 'death_year':None}, self.booksDataSource.author(18))
    
    def test_author_ID_incorrect_result(self):
        self.assertNotEqual("Trevor Noah", self.booksDataSource.author(18))
        
    def test_author_ID_zero(self):
        self.assertEqual({'id':0, 'last_name':'Willis', 'first_name':'Connie', 'birth_year':1945, 'death_year':None}, self.booksDataSource.author(0))

    def test_author_ID_negative(self):
        self.assertRaises(ValueError, self.booksDataSource.author, -1)

    def test_author_ID_too_big(self):
        self.assertRaises(ValueError, self.booksDataSource.author, 100)
    
    '''
        Unit test for authors
    '''
    
    def test_authors_no_parameters(self):
        self.assertEqual(self.booksDataSource.authors(), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':23, 'last_name':'Dickens', 'first_name':'Charles', 'birth_year':1812, 'death_year':1870}, {'id':7, 'last_name':'Brontë', 'first_name':'Charlotte', 'birth_year':1816, 'death_year':1855}, {'id':15, 'last_name':'Brontë', 'first_name':'Emily', 'birth_year':1818, 'death_year':1848}, {'id':22, 'last_name':'Eliot', 'first_name':'George', 'birth_year':1819, 'death_year':1880}, {'id':13, 'last_name':'Melville', 'first_name':'Herman', 'birth_year':1819, 'death_year':1891}, {'id':14, 'last_name':'Brontë', 'first_name':'Ann', 'birth_year':1820, 'death_year':1849}, {'id':21, 'last_name':'Jerome', 'first_name':'Jerome K.', 'birth_year':1859, 'death_year':1927}, {'id':17, 'last_name':'Cather', 'first_name':'Willa', 'birth_year':1873, 'death_year':1947}, {'id':8, 'last_name':'Wodehouse', 'first_name':'Pelham Grenville', 'birth_year':1881, 'death_year':1975}, {'id':3, 'last_name':'Lewis', 'first_name':'Sinclair', 'birth_year':1885, 'death_year':None}, {'id':10, 'last_name':'Lewis', 'first_name':'Sinclair', 'birth_year':1885, 'death_year':1951}, {'id':1, 'last_name':'Christie', 'first_name':'Agatha', 'birth_year':1890, 'death_year':1976}, {'id':19, 'last_name':'DuMaurier', 'first_name':'Daphne', 'birth_year':1907, 'death_year':1989}, {'id':9, 'last_name':'Márquez', 'first_name':'Gabriel García', 'birth_year':1927, 'death_year':2014}, {'id':24, 'last_name':'Carré', 'first_name':'John Le', 'birth_year':1931, 'death_year':None}, {'id':2, 'last_name':'Morrison', 'first_name':'Toni', 'birth_year':1931, 'death_year':None}, {'id':0, 'last_name':'Willis', 'first_name':'Connie', 'birth_year':1945, 'death_year':None}, {'id':11, 'last_name':'Rushdie', 'first_name':'Salman', 'birth_year':1947, 'death_year':None}, {'id':6, 'last_name':'Pratchett', 'first_name':'Terry', 'birth_year':1948, 'death_year':2015}, {'id':12, 'last_name':'Bujold', 'first_name':'Lois McMaster', 'birth_year':1949, 'death_year':None}, {'id':16, 'last_name':'Murakami', 'first_name':'Haruki', 'birth_year':1949, 'death_year':None}, {'id':5, 'last_name':'Gaiman', 'first_name':'Neil', 'birth_year':1960, 'death_year':None}, {'id':20, 'last_name':'Jemisen', 'first_name':'N.K.', 'birth_year':1972, 'death_year':None}, {'id':18, 'last_name':'Alderman', 'first_name':'Naomi', 'birth_year':1974, 'death_year':None}])
    
    def test_authors_valid_book_ID(self):
        self.assertEqual(self.booksDataSource.authors(book_id=1), [{'id':1, 'last_name':'Christie', 'first_name':'Agatha', 'birth_year':1890, 'death_year':1976}])

    def test_authors_book_ID_wrong_author(self):
        self.assertNotEqual(self.booksDataSource.authors(book_id=1), ["John Oliver"])

    def test_authors_book_ID_negative_ID(self):
        self.assertRaises(ValueError, self.booksDataSource.authors, book_id=-1)
        
    def test_authors_book_ID_too_big(self): 
        self.assertRaises(ValueError, self.booksDataSource.authors, book_id=90)
                
    def test_authors_valid_search_text(self):
        self.assertEqual(self.booksDataSource.authors(search_text="Agatha"), [{'id':1, 'last_name':'Christie', 'first_name':'Agatha', 'birth_year':1890, 'death_year':1976}])
        
    def test_authors_valid_search_text_all_lower_case(self):
        self.assertEqual(self.booksDataSource.authors(search_text="agatha"), [{'id':1, 'last_name':'Christie', 'first_name':'Agatha', 'birth_year':1890, 'death_year':1976}])
        
    def test_authors_search_text_no_result(self):
        self.assertEqual(self.booksDataSource.authors(search_text="phuoc"), [])
    
    def test_authors_search_text_wrong_result(self):
        self.assertNotEqual(self.booksDataSource.authors(search_text="Agatha"), [{'id':29, 'title':'Wuthering Heights', 'publication_year':1847}])
    
    def test_authors_start_year_correct_results(self): 
        self.assertEqual(self.booksDataSource.authors(start_year = 2015), [{'id':3, 'last_name':'Lewis', 'first_name':'Sinclair', 'birth_year':1885, 'death_year':None}, {'id':24, 'last_name':'Carré', 'first_name':'John Le', 'birth_year':1931, 'death_year':None}, {'id':2, 'last_name':'Morrison', 'first_name':'Toni', 'birth_year':1931, 'death_year':None}, {'id':0, 'last_name':'Willis', 'first_name':'Connie', 'birth_year':1945, 'death_year':None}, {'id':11, 'last_name':'Rushdie', 'first_name':'Salman', 'birth_year':1947, 'death_year':None}, {'id':6, 'last_name':'Pratchett', 'first_name':'Terry', 'birth_year':1948, 'death_year':2015}, {'id':12, 'last_name':'Bujold', 'first_name':'Lois McMaster', 'birth_year':1949, 'death_year':None}, {'id':16, 'last_name':'Murakami', 'first_name':'Haruki', 'birth_year':1949, 'death_year':None}, {'id':5, 'last_name':'Gaiman', 'first_name':'Neil', 'birth_year':1960, 'death_year':None}, {'id':20, 'last_name':'Jemisen', 'first_name':'N.K.', 'birth_year':1972, 'death_year':None}, {'id':18, 'last_name':'Alderman', 'first_name':'Naomi', 'birth_year':1974, 'death_year':None}])
        
    def test_authors_start_year_wrong_authors(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 1990), [])
    
    def test_authors_start_year_no_authors(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 3100), [])
    
    def test_authors_end_year_correct_results(self):
        self.assertEqual(self.booksDataSource.authors(end_year = 1816), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':23, 'last_name':'Dickens', 'first_name':'Charles', 'birth_year':1812, 'death_year':1870}, {'id':7, 'last_name':'Brontë', 'first_name':'Charlotte', 'birth_year':1816, 'death_year':1855}])
        
    def test_authors_end_year_no_lower_case_authors(self):
        self.assertNotEqual(self.booksDataSource.authors(end_year = 1812), [{'id':4, 'last_name':'austen', 'first_name':'jane', 'birth_year':1775, 'death_year':1817}, {'id':23, 'last_name':'dickens', 'first_name':'charles', 'birth_year':1812, 'death_year':1870}])
        
    def test_authors_end_year_wrong_results(self):
        self.assertNotEqual(self.booksDataSource.authors(end_year = 1812), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}])
        
    def test_authors_sort_by_birth_year(self):
        self.assertEqual(self.booksDataSource.authors(end_year = 1816, sort_by = 'birth_year'), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':23, 'last_name':'Dickens', 'first_name':'Charles', 'birth_year':1812, 'death_year':1870}, {'id':7, 'last_name':'Brontë', 'first_name':'Charlotte', 'birth_year':1816, 'death_year':1855}])
#        
    def test_authors_sort_by_birth_year_wrong_order(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 1816, sort_by = 'birth_year'), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':7, 'last_name':'Brontë', 'first_name':'Charlotte', 'birth_year':1816, 'death_year':1855}, {'id':23, 'last_name':'Dickens', 'first_name':'Charles', 'birth_year':1812, 'death_year':1870}])
        
    def test_authors_two_parameters_start_year_end_year(self): 
        self.assertEqual(self.booksDataSource.authors(start_year = 1816, end_year = 1900), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':23, 'last_name':'Dickens', 'first_name':'Charles', 'birth_year':1812, 'death_year':1870}, {'id':7, 'last_name':'Brontë', 'first_name':'Charlotte', 'birth_year':1816, 'death_year':1855}, {'id':15, 'last_name':'Brontë', 'first_name':'Emily', 'birth_year':1818, 'death_year':1848}, {'id':22, 'last_name':'Eliot', 'first_name':'George', 'birth_year':1819, 'death_year':1880}, {'id':13, 'last_name':'Melville', 'first_name':'Herman', 'birth_year':1819, 'death_year':1891}, {'id':14, 'last_name':'Brontë', 'first_name':'Ann', 'birth_year':1820, 'death_year':1849}, {'id':21, 'last_name':'Jerome', 'first_name':'Jerome K.', 'birth_year':1859, 'death_year':1927}, {'id':17, 'last_name':'Cather', 'first_name':'Willa', 'birth_year':1873, 'death_year':1947}, {'id':8, 'last_name':'Wodehouse', 'first_name':'Pelham Grenville', 'birth_year':1881, 'death_year':1975}, {'id':3, 'last_name':'Lewis', 'first_name':'Sinclair', 'birth_year':1885, 'death_year':None}, {'id':10, 'last_name':'Lewis', 'first_name':'Sinclair', 'birth_year':1885, 'death_year':1951}, {'id':1, 'last_name':'Christie', 'first_name':'Agatha', 'birth_year':1890, 'death_year':1976}])
        
    def test_authors_two_parameters_search_text_sort_by(self):
        self.assertEqual(self.booksDataSource.authors(search_text = 'an', sort_by = 'birth_year'), [{'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':13, 'last_name':'Melville', 'first_name':'Herman', 'birth_year':1819, 'death_year':1891}, {'id':14, 'last_name':'Brontë', 'first_name':'Ann', 'birth_year':1820, 'death_year':1849}, {'id':11, 'last_name':'Rushdie', 'first_name':'Salman', 'birth_year':1947, 'death_year':None}, {'id':5, 'last_name':'Gaiman', 'first_name':'Neil', 'birth_year':1960, 'death_year':None}, {'id': 18, 'death_year': None, 'first_name': 'Naomi', 'last_name': 'Alderman', 'birth_year': 1974}])
    
    def test_authors_two_parameters_search_text_sort_by(self):
        self.assertEqual(self.booksDataSource.authors(search_text = 'an', sort_by = 'last_name'), [{'id': 18, 'death_year': None, 'first_name': 'Naomi', 'last_name': 'Alderman', 'birth_year': 1974}, {'id':4, 'last_name':'Austen', 'first_name':'Jane', 'birth_year':1775, 'death_year':1817}, {'id':14, 'last_name':'Brontë', 'first_name':'Ann', 'birth_year':1820, 'death_year':1849}, {'id':5, 'last_name':'Gaiman', 'first_name':'Neil', 'birth_year':1960, 'death_year':None}, {'id':13, 'last_name':'Melville', 'first_name':'Herman', 'birth_year':1819, 'death_year':1891}, {'id':11, 'last_name':'Rushdie', 'first_name':'Salman', 'birth_year':1947, 'death_year':None}])
   
if __name__ == '__main__':
    unittest.main()
