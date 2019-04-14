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
        self.assertEqual("All Clear", self.booksDataSource.book(0))
        
    def test_book_ID_valid(self):
        self.assertEqual("Beloved", self.booksDataSource.book(2))
    
    def test_book_ID_incorrect_result(self):
        self.assertNotEqual("A Monster Calls", self.booksDataSource.book(2))

    def test_book_ID_negative(self):
        self.assertRaises(ValueError, self.booksDataSource.book, -1)

    def test_book_ID_decimal(self):
        self.assertRaises(TypeError, self.booksDataSource.book, 5.5)

    def test_book_ID_too_big(self):
        self.assertRaises(ValueError, self.booksDataSource.book, 100)
        
    '''
        Unit tests for books
    '''

    def test_books_no_parameters(self):
        self.assertEqual([{0:'All Clear'}, {1:'And Then There Were None'}, {2:'Beloved'}, {3:'Blackout'}, {4:'Elmer Gantry'}, {5:'Emma'}, {6:'Good Omens'}, {7:'Jane Eyre'}, {8:'Leave it to Psmith'}, {9:'Love in the Time of Cholera'}, {10:'Main Street'}, {11:"Midnight's Children"}, {12:'Mirror Dance'}, {13:'Moby Dick'}, {14:'Murder on the Orient Express'}, {15:'Neverwhere'}, {16:'Omoo'}, {17:'One Hundred Years of Solitude'}, {18:'Pride and Prejudice'}, {19:'Right Ho, Jeeves'}, {20:'Sense and Sensibility'}, {21:'Shards of Honor'}, {22:'Sula'}, {23:'The Code of the Woosters'}, {24:'The Satanic Verses'}, {25:'The Tenant of Wildfell Hall'}, {26:'Thief of Time'}, {27:'To Say Nothing of the Dog'}, {28:'Villette'}, {29:'Wuthering Heights'}, {30:'1Q84'}, {31:'A Wild Sheep Chase'}, {32:'Hard-Boiled Wonderland and the End of the World'}, {33:'My Ántonia'}, {34:'O Pioneers!'}, {35:'The Power'}, {36:'Rebecca'}, {37:'The Fifth Season'}, {38:'The Obelisk Gate'}, {39:'The Stone Sky'}, {40:'Three Men in a Boat (to Say Nothing of the Dog)'}, {41:'Middlemarch'}, {42:'Silas Marner'}, {43:'Bleak House'}, {44:'Great Expectations'}, {45:'Tinker, Tailor, Soldier, Spy'}, {46:'The Spy Who Came in From the Cold'}], self.booksDataSource.books())
    
    def test_books_valid_author_ID(self):
        self.assertEqual(self.booksDataSource.books(author_id=1), ["And Then There Were None", "Murder on the Orient Express"])

    def test_books_author_ID_wrong_books(self):
        self.assertNotEqual(self.booksDataSource.books(author_id=1), ["Good Omens"])

    def test_books_author_ID_negative_ID(self):
        self.assertRaises(ValueError, self.booksDataSource.books, author_id=-1)

    def test_books_author_ID_decimal_ID(self): 
        self.assertRaises(TypeError, self.booksDataSource.books, author_id=1.2)
        
    def test_books_author_ID_too_big(self): 
        self.assertRaises(ValueError, self.booksDataSource.books, author_id = 90)
        
    def test_books_valid_search_text(self):
        self.assertEqual(self.booksDataSource.books(search_text="mirror"), ["Mirror Dance"])
        
    def test_books_search_text_no_result(self):
        self.assertEqual(self.booksDataSource.books(search_text="phuoc"), [])
    
    def test_books_search_text_wrong_result(self):
        self.assertNotEqual(self.booksDataSource.books(search_text="Chase"), ["Wuthering Heights"])
    
    def test_books_start_year(self):
        self.assertEqual(self.booksDataSource.books(start_year = 2015), ['The Fifth Season', 'The Obelisk Gate', 'The Power', 'The Stone Sky'])
        
    def test_books_start_year_wrong_books(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 1990), [])
        
    def test_books_end_year(self):
        self.assertEqual(self.booksDataSource.books(end_year = 1830), ['Emma', 'Pride and Prejudice', 'Sense and Sensibility'])
        
    def test_books_end_year_wrong_books(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 2010), ['Emma', 'Pride and Prejudice', 'Sense and Sensibility'])
        
    def test_books_sort_by_default_wrong_order(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 2015), ['The Fifth Season', 'The Power', 'The Stone Sky', 'The Obelisk Gate'])
        
    def test_books_sort_by_year(self):
        self.assertEqual(self.booksDataSource.books(start_year = 2015, sort_by = 'year'), ['The Fifth Season', 'The Obelisk Gate', 'The Stone Sky', 'The Power'])
        
    def test_books_sort_by_year_wrong_order(self):
        self.assertNotEqual(self.booksDataSource.books(start_year = 2015, sort_by = 'year'), ['The Power', 'The Fifth Season', 'The Obelisk Gate', 'The Stone Sky'])

    def test_books_author_ID_and_start_year(self):
        self.assertEqual(self.booksDataSource.books(author_id=1, start_year=1939), ["And Then There Were None"])

    def test_books_search_text_and_end_year(self):
        self.assertEqual(self.booksDataSource.books(end_year=1830, search_text='and'), ['Pride and Prejudice', 'Sense and Sensibility'])
        
    '''
        Unit test for author
    '''
    
    def test_author_ID_valid(self):
        self.assertEqual("Naomi Alderman", self.booksDataSource.author(18))
    
    def test_author_ID_incorrect_result(self):
        self.assertNotEqual("Trevor Noah", self.booksDataSource.author(18))
        
    def test_author_ID_zero(self):
        self.assertEqual("Connie Willis", self.booksDataSource.author(0))

    def test_author_ID_negative(self):
        self.assertRaises(ValueError, self.booksDataSource.author, -1)

    def test_author_ID_decimal(self):
        self.assertRaises(TypeError, self.booksDataSource.author, 5.5)

    def test_author_ID_too_big(self):
        self.assertRaises(ValueError, self.booksDataSource.author, 100)
    
    '''
        Unit test for authors
    '''
    
    def test_authors_no_parameters(self):
        self.assertEqual(self.booksDataSource.authors(), [{0: 'Connie Willis'}, {1: 'Agatha Christie'}, {2: 'Toni Morrison'}, {3: 'Sinclair Lewis'}, {4: 'Jane Austen'}, {5: 'Neil Gaiman'}, {6: 'Terry Pratchett'}, {7: 'Charlotte Brontë'}, {8: 'Pelham Grenville Wodehouse'}, {9: 'Gabriel García Márquez'}, {10: 'Sinclair Lewis'}, {11: 'Salman Rushdie'}, {12: 'Lois McMaster Bujold'}, {13: 'Herman Melville'}, {14: 'Ann Brontë'}, {15: 'Emily Brontë'}, {16: 'Haruki Murakami'}, {17: 'Willa Cather'}, {18: 'Naomi Alderman'}, {19: 'Daphne DuMaurier'}, {20: 'N.K. Jemisen'}, {21: 'Jerome K. Jerome'}, {22: 'Geogre Eliot'}, {23: 'Charles Dickens'}, {24: 'John Le Carré'}])
    
    def test_authors_valid_book_ID(self):
        self.assertEqual(self.booksDataSource.authors(book_id=1), ["Agatha Christie"])

    def test_authors_book_ID_wrong_author(self):
        self.assertNotEqual(self.booksDataSource.authors(book_id=1), ["John Oliver"])

    def test_authors_book_ID_negative_ID(self):
        self.assertRaises(ValueError, self.booksDataSource.authors, book_id=-1)

    def test_authors_book_ID_decimal_ID(self): 
        self.assertRaises(TypeError, self.booksDataSource.authors, book_id=1.2)
        
    def test_authors_book_ID_too_big(self): 
        self.assertRaises(ValueError, self.booksDataSource.authors, book_id=90)
                
    def test_authors_valid_search_text(self):
        self.assertEqual(self.booksDataSource.authors(search_text="Agatha"), ["Agatha Christie"])
        
    def test_authors_valid_search_text_all_lower_case(self):
        self.assertEqual(self.booksDataSource.authors(search_text="agatha"), ["Agatha Christie"])
        
    def test_authors_search_text_no_result(self):
        self.assertEqual(self.booksDataSource.authors(search_text="phuoc"), [])
    
    def test_authors_search_text_wrong_result(self):
        self.assertNotEqual(self.booksDataSource.authors(search_text="Agatha"), ["Wuthering Heights"])
    
    def test_authors_start_year_correct_results(self):
        self.assertEqual(self.booksDataSource.authors(start_year = 2015), ['Naomi Alderman', 'Lois McMaster Bujold', 'John Le Carré', 'Neil Gaiman', 'N.K. Jemisen', 'Sinclair Lewis', 'Toni Morrison', 'Haruki Murakami', 'Terry Pratchett', 'Salman Rushdie', 'Connie Willis'])
        
    def test_authors_start_year_wrong_authors(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 1990), [])
    
    def test_authors_start_year_no_authors(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 3100), [])
    
    def test_authors_end_year_correct_results(self):
        self.assertEqual(self.booksDataSource.authors(start_year = 1816), ['Jane Austen', 'Charlotte Brontë', 'Charles Dickens'])
        
    def test_authors_end_year_no_lower_case_authors(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 1812), ['jane austen', 'charlotte brontë', 'charles dickens'])
        
    def test_authors_end_year_wrong_results(self):
        self.assertEqual(self.booksDataSource.authors(start_year = 1812), ['Jane Austen'])
        
    def test_authors_sort_by_birth_year(self):
        self.assertEqual(self.booksDataSource.authors(start_year = 1816, sort_by = 'birth_year'), ['Jane Austen', 'Charles Dickens', 'Charlotte Brontë'])
        
    def test_authors_sort_by_brith_year_wrong_order(self):
        self.assertNotEqual(self.booksDataSource.authors(start_year = 1816, sort_by = 'birth_year'), ['Jane Austen', 'Charlotte Brontë', 'Charles Dickens'])
        
    def test_authors_two_parameters_start_year_end_year(self): 
        self.assertEqual(self.booksDataSource.authors(start_year = 1816, end_year = 1900), ['Jane Austen', 'Ann Brontë', 'Charlotte Brontë', 'Emily Brontë', 'Willa Cather', 'Agatha Christie', 'Charles Dickens', 'Geogre Eliot', 'Jerome K. Jerome', 'Sinclair Lewis', 'Herman Melville', 'Pelman Grenville Wodehouse'])
        
    def test_authors_two_parameters_search_text_sort_by(self):
        self.assertEqual(self.booksDataSource.authors(search_text = 'an', sort_by = 'birth_year'), ['Jane Austen', 'Herman Melville', 'Ann Brontë', 'Salman Rushdie', 'Neil Gaiman'])
    
if __name__ == '__main__':
    unittest.main()
