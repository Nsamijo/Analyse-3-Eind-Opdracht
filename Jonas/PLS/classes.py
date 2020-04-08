class Person:
    def __init__(self,name,birthday,gender):
        self.name = name
        self.birthday = birthday
        self.gender = gender
#bday in format "dd/mm/yyyy"
class Subscriber(Person):
    def __init__(self,name,birthday,gender,username,email):
        super.__init__(name,birthday,gender)
        self.username = username
        self.email = email
    
    def getUsername(self):
        return self.username
    def getName(self):
        return self.name
    def getBirthday(self):
        return self.birthday
    def getEmail(self):
        return self.email
class Librarian(Person):
    def __init__(self,name,birthday,gender,username,password,email):
        super.__init__(name,birthday,gender)
        self.username = username
        self.password = password
        self.email = email

class Book:
    def __init__(self,author,country,imageLink,language,wikilink,pages,title,year):
        self.author = author
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.wikilink = wikilink
        self.pages = pages
        self.title = title
        self.year = year
    
    def getAuthor(self):
        return self.author
    
    def getCountry(self):
        return self.country
    
    def getImageLink(self):
        return self.imageLink
    
    def getLanguage(self):
        return self.language
    
    def getWikiLink(self):
        return self.wikilink
    
    def getPages(self):
        return self.pages
    def getTitle(self):
        return self.title

    def getYear(self):
        return self.year
class LoanItem:
    def __init__(self,bookItem,subscriber):
        self.subscriber = subscriber
        self.bookItem = bookItem

class BookItem:
    def __init__(self,book):
        self.book = book
        self.status = "a"

class Catalog:
    def __init__(self,name):
        self.name = name
        self.books = []
        self.bookItems = []
    def addBook(self,author,country,imageLink,language,wikilink,pages,title,year):
        self.books.append(Book(author,country,imageLink,language,wikilink,pages,title,year))
    def addBookItem(self,bookTitle):
        for i in self.books:
            if i.getTitle() == bookTitle:
                self.bookItems.append(BookItem(i))
            else:
                print("No book with title: {} found, please try again.".format(bookTitle))

class LoanAdministration:
    def __init__(self,name):
        self.name = name
        self.loans = []
    
    def createLoan(self,catalog,bookItem,username):
        if bookItem in catalog.bookItems:
            self.loans.append(LoanItem(bookItem,username))
        else:
            print("No such item in catalog")