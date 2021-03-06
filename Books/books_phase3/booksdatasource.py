#!/usr/bin/env python3
'''
    booksdatasource.py
    Jeff Ondich, 18 September 2018
    Modified by Eric Alexander, April 2019

    For use in some assignments at the beginning of Carleton's
    CS 257 Software Design class.
'''
import csv 

class BooksDataSource:
    '''
    An author is represented as a dictionary with the keys
    'id', 'last_name', 'first_name', 'birth_year', and 'death_year'.
    For example, Jane Austen would be represented like this
    (assuming her database-internal ID number is 72):

        {'id': 72, 'last_name': 'Austen', 'first_name': 'Jane',
         'birth_year': 1775, 'death_year': 1817}

    For a living author, the death_year is represented in the author's
    Python dictionary as None.

        {'id': 77, 'last_name': 'Murakami', 'first_name': 'Haruki',
         'birth_year': 1949, 'death_year': None}

    Note that this is a simple-minded representation of a person in
    several ways. For example, how do you represent the birth year
    of Sophocles? What is the last name of Gabriel García Márquez?
    Should we refer to the author of "Tom Sawyer" as Samuel Clemens or
    Mark Twain? Are Voltaire and Molière first names or last names? etc.

    A book is represented as a dictionary with the keys 'id', 'title',
    and 'publication_year'. For example, "Pride and Prejudice"
    (assuming an ID of 132) would look like this:

        {'id': 193, 'title': 'A Wild Sheep Chase', 'publication_year': 1982}

    '''

    def __init__(self, books_filename, authors_filename, books_authors_link_filename):
        ''' Initializes this data source from the three specified  CSV files, whose
            CSV fields are:

                books: ID,title,publication-year
                  e.g. 6,Good Omens,1990
                       41,Middlemarch,1871


                authors: ID,last-name,first-name,birth-year,death-year
                  e.g. 5,Gaiman,Neil,1960,NULL
                       6,Pratchett,Terry,1948,2015
                       22,Eliot,George,1819,1880

                link between books and authors: book_id,author_id
                  e.g. 41,22
                       6,5
                       6,6

                  [that is, book 41 was written by author 22, while book 6
                    was written by both author 5 and author 6]

            Note that NULL is used to represent a non-existent (or rather, future and
            unknown) year in the cases of living authors.

            NOTE TO STUDENTS: I have not specified how you will store the books/authors
            data in a BooksDataSource object. That will be up to you, in Phase 3.
        '''
        
        with open(books_filename, newline = '') as csvfile:
            readerBooks = csv.reader(csvfile)
            self.bookDict = {}
            for row in readerBooks:
                bookInfo = {}
                bookInfo['id'] = int(row[0])
                bookInfo['title'] = row[1]
                bookInfo['publication_year'] = int(row[2])
                
                self.bookDict[int(row[0])] = bookInfo
        
        with open(authors_filename, newline = '') as csvfile:
            readerAuthors = csv.reader(csvfile)
            self.authorDict = {}
            for row in readerAuthors:
                authorInfo = {}
                authorInfo['id'] = int(row[0])
                authorInfo['last_name'] = row[1]
                authorInfo['first_name'] = row[2]
                authorInfo['birth_year'] = int(row[3])
                if row[4] == 'NULL':
                    authorInfo['death_year'] = None
                else:
                    authorInfo['death_year'] = int(row[4])
                
                self.authorDict[int(row[0])] = authorInfo
        
        '''
            Use bookID as the key and authorID as the value
        '''
        
        with open(books_authors_link_filename, newline = '') as csvfile:
            readerBooksAuthors = csv.reader(csvfile)
            self.bookKeyDict = {}
            for row in readerBooksAuthors:
                bookID = int(row[0])
                authorID = int(row[1])
                if bookID in self.bookKeyDict: 
                    currentAuthorIDList = self.bookKeyDict[bookID]
                    currentAuthorIDList.append(authorID)
                    self.bookKeyDict[bookID] = currentAuthorIDList
                else:

                    self.bookKeyDict[bookID] = [authorID]

        '''
            Use authorID as the key and bookID as the value
        '''
        with open(books_authors_link_filename, newline = '') as csvfile:
            readerBooksAuthors = csv.reader(csvfile)
            self.authorKeyDict = {}
            for row in readerBooksAuthors:
                bookID = int(row[0])
                authorID = int(row[1])
                if authorID in self.authorKeyDict: 
                    currentBookIDList = self.authorKeyDict[authorID]
                    currentBookIDList.append(bookID)
                    self.authorKeyDict[authorID] = currentBookIDList
                else:
                    self.authorKeyDict[authorID] = [bookID]
                
                
    def book(self, book_id):
        ''' Returns the book with the specified ID. (See the BooksDataSource comment for a description of how a book is represented.)
            Raises ValueError if book_id is not a valid book ID.
        '''
        if book_id not in self.bookDict and book_id > 0: 
            raise ValueError('Book ID is too big')
        elif book_id < 0:
            raise ValueError('Book ID cannot be negative')
        elif book_id in self.bookDict:
            return self.bookDict[book_id]
        
                
    def books(self, *, author_id=None, search_text=None, start_year=None, end_year=None, sort_by='title'):
        ''' Returns a list of all the books in this data source matching all of the specified non-None criteria.

                author_id - only returns books by the specified author
                search_text - only returns books whose titles contain (case-insensitively) the search text
                start_year - only returns books published during or after this year
                end_year - only returns books published during or before this year

            Note that parameters with value None do not affect the list of books returned.
            Thus, for example, calling books() with no parameters will return JSON for
            a list of all the books in the data source.

            The list of books is sorted in an order depending on the sort_by parameter:

                'year' -- sorts by publication_year, breaking ties with (case-insenstive) title
                default -- sorts by (case-insensitive) title, breaking ties with publication_year

            QUESTION: Should Python interfaces specify TypeError?
            Raises TypeError if author_id, start_year, or end_year is non-None but not an integer.
            Raises TypeError if search_text or sort_by is non-None, but not a string.
				OUR ANSWER: Not for this assignment.

            QUESTION: How about ValueError? And if so, for which parameters?
            Raises ValueError if author_id is non-None but is not a valid author ID.
				OUR ANSWER: Yes, but just for author_id.
        '''
        booksList = []
        bookIDList = []
        
        if author_id != None:     
            if author_id not in self.authorDict and author_id > 0: 
                raise ValueError('Author ID is too big')
            elif author_id < 0:
                raise ValueError('Author ID cannot be negative')
            else:
                bookIDList = self.authorKeyDict[author_id]
        
            if search_text != None:
                bookIDList = self.removeBooksThatDontMatchSearchText(bookIDList)
            
            if start_year != None: 
                bookIDList = self.removeBooksThatDontMatchStartYear(bookIDList, start_year)
                
            if end_year != None:
                bookIDList = self.removeBooksThatDontMatchEndYear(bookIDList, end_year)          
  
        elif search_text != None:
            searchText = search_text.lower()
            for bookID in self.bookDict: 
                bookName = self.bookDict[bookID]['title'].lower()
                if searchText in bookName: 
                    bookIDList.append(bookID)
            
            
            if start_year != None: 
                bookIDList = self.removeBooksThatDontMatchStartYear(bookIDList, start_year)
            
            if end_year != None:
                bookIDList = self.removeBooksThatDontMatchEndYear(bookIDList, end_year)
        
        elif start_year != None:
            for bookID in self.bookDict:
                bookPublicationYear = self.bookDict[bookID]['publication_year']
                if bookPublicationYear >= start_year:
                    bookIDList.append(bookID)
                    
            if end_year != None:
                bookIDList = self.removeBooksThatDontMatchEndYear(bookIDList, end_year)
        
        elif end_year != None: 
            for bookID in self.bookDict:
                bookPublicationYear = self.bookDict[bookID]['publication_year']
                if bookPublicationYear <= end_year:
                    bookIDList.append(bookID)
                     
        else: 
            for books in self.bookDict:
                booksList.append(self.bookDict[books])            
            
        for bookID in bookIDList: 
            bookEntry = self.bookDict[bookID]
            booksList.append(bookEntry)
                    
        if sort_by == 'title':
            newBookEntryList = sorted(booksList, key = self.getBookTitle)
        elif sort_by == 'year':
            newBookEntryList = sorted(booksList, key= self.getPublicationYear)    
        return newBookEntryList
    
    def getBookTitle(self, book): 
        return book.get('title')
    
    def getPublicationYear(self, book):
        return book.get('publication_year')
    
    
    def removeBooksThatDontMatchSearchText(self, bookIDList, search_text): 
        searchText = search_text.lower()
        bookIDListSearchText = []
        for bookID in bookIDList: 
            bookName = self.bookDict[bookID]['title'].lower()
            if search_text in bookName:
                bookIDListSearchText.append(bookID)
        return bookIDListSearchText
    
    def removeBooksThatDontMatchStartYear(self, bookIDList, start_year):
        bookIDListStartYear = [] 
        for bookID in bookIDList:
            bookPublicationYear = self.bookDict[bookID]['publication_year']
            if bookPublicationYear >= start_year:
                bookIDListStartYear.append(bookID)
        return bookIDListStartYear
    
    def removeBooksThatDontMatchEndYear(self, bookIDList, end_year):
        bookIDListEndYear = [] 
        for bookID in bookIDList:
            bookPublicationYear = self.bookDict[bookID]['publication_year']
            if bookPublicationYear <= end_year:
                bookIDListEndYear.append(bookID)
        return bookIDListEndYear
    
    
    def author(self, author_id):
        ''' Returns the author with the specified ID. (See the BooksDataSource comment for a
            description of how an author is represented.)
            Raises ValueError if author_id is not a valid author ID.
        '''
        if author_id not in self.authorDict and author_id > 0: 
            raise ValueError('Author ID is too big')
        elif author_id < 0:
            raise ValueError('Author ID cannot be negative')
        elif author_id in self.bookDict:
            return self.authorDict[author_id]
        

    def authors(self, *, book_id=None, search_text=None, start_year=None, end_year=None, sort_by='birth_year'):
        ''' Returns a list of all the authors in this data source matching all of the
            specified non-None criteria.

                book_id - only returns authors of the specified book
                search_text - only returns authors whose first or last names contain
                    (case-insensitively) the search text
                start_year - only returns authors who were alive during or after
                    the specified year
                end_year - only returns authors who were alive during or before
                    the specified year

            Note that parameters with value None do not affect the list of authors returned.
            Thus, for example, calling authors() with no parameters will return JSON for
            a list of all the authors in the data source.

            The list of authors is sorted in an order depending on the sort_by parameter:

                'birth_year' - sorts by birth_year, breaking ties with (case-insenstive) last_name,
                    then (case-insensitive) first_name
                any other value - sorts by (case-insensitive) last_name, breaking ties with
                    (case-insensitive) first_name, then birth_year

            See the BooksDataSource comment for a description of how an author is represented.
        '''
        
        authorsList = []
        authorIDList = []
        
        if book_id != None:     
            if book_id not in self.authorDict and book_id > 0: 
                raise ValueError('Author ID is too big')
            elif book_id < 0:
                raise ValueError('Author ID cannot be negative')
            else:
                authorIDList = self.bookKeyDict[book_id]
        
            if search_text != None:
                authorIDList = self.removeAuthorsThatDontMatchSearchText(authorIDList)
            
            if start_year != None: 
                authorIDList = self.removeAuthorsThatWerentAliveAfterStartYear(authorIDList, start_year)
                
            if end_year != None:
                authorIDList = self.removeAuthorsThatWerentAliveBeforeEndYear(authorIDList, end_year)          
  
        elif search_text != None:
            searchText = search_text.lower()
            for authorID in self.authorDict: 
                authorFirstName = self.authorDict[authorID]['first_name'].lower()
                authorLastName = self.authorDict[authorID]['last_name'].lower()
                if searchText in authorFirstName or searchText in authorLastName: 
                    authorIDList.append(authorID)
            
            
            if start_year != None: 
                authorIDList = self.removeAuthorsThatWerentAliveAfterStartYear(authorIDList, start_year)
            
            if end_year != None:
                authorIDList = self.removeAuthorsThatWerentAliveBeforeEndYear(authorIDList, end_year)
        
        elif start_year != None:
            for authorID in self.authorDict:
                authorDeathYear = self.authorDict[authorID]['death_year']
                if authorDeathYear == None:
                    authorIDList.append(authorID)
                elif authorDeathYear >= start_year:
                    authorIDList.append(authorID)
                    
            if end_year != None:
                authorIDList = self.removeAuthorsThatWerentAliveBeforeEndYear(authorIDList, end_year)
        
        elif end_year != None: 
            for authorID in self.authorDict:
                authorBirthYear = self.authorDict[authorID]['birth_year']
                if authorBirthYear <= end_year:
                    authorIDList.append(authorID)
                     
        else: 
            for authors in self.authorDict:
                authorsList.append(self.authorDict[authors])
            
        for authorID in authorIDList: 
            authorEntry = self.authorDict[authorID]
            authorsList.append(authorEntry)
        if sort_by == 'birth_year':
            newAuthorEntryList = sorted(authorsList, key=lambda k: (k['birth_year'], k['last_name'], k['first_name']))
        else:
            newAuthorEntryList = sorted(authorsList, key=lambda k: (k['last_name'], k['first_name'], k['birth_year'])) 
        return newAuthorEntryList
    
    
    def removeAuthorsThatDontMatchSearchText(self, authorIDList, search_text): 
        searchText = search_text.lower()
        authorIDListSearchText = []
        for authorID in self.authorDict: 
            authorFirstName = self.authorDict[authorID]['first_name'].lower()
            authorLastName = self.authorDict[authorID]['last_name'].lower()
            if search_text in authorFirstName or search_text in authorLastName: 
                authorIDList.append(authorID)
        return authorIDListSearchText
    
    def removeAuthorsThatWerentAliveAfterStartYear(self, authorIDList, start_year):
        authorIDListStartYear = [] 
        for authorID in authorIDList:
            authorDeathYear = self.authorDict[authorID]['death_year']
            if authorDeathYear == None:
                authorIDListStartYear.append(authorID)
            elif authorDeathYear >= start_year:
                authorIDListStartYear.append(authorID)
        return authorIDListStartYear
    
    def removeAuthorsThatWerentAliveBeforeEndYear(self, authorIDList, end_year):
        authorIDListEndYear = [] 
        for authorID in authorIDList:
            authorBirthYear = self.authorDict[authorID]['birth_year']
            if authorBirthYear <= end_year:
                authorIDListEndYear.append(authorID)
        return authorIDListEndYear
    
if __name__ == '__main__':
    books = BooksDataSource('books.csv', 'authors.csv', 'books_authors.csv')
