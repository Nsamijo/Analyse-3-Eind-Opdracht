import json
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
    def __init__(self,id,author,country,imageLink,language,wikilink,pages,title,year):
        self.id = id
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
    def getString(self):
        return "" + self.author + self.language + self.title + self.year + self.country

class LoanItem:
    def __init__(self,bookItem,subscriber):
        self.subscriber = subscriber
        self.bookItem = bookItem

class BookItem:
    def __init__(self,movie,book):
        self.movie = movie
        self.book = book
        self.status = "available"
    
    def changeStatus(self,status):
        self.status = status

class Catalog:
    def __init__(self,name):
        self.name = name
        self.books = []
        with open('books.json','r') as bookRead:
            data = bookRead
            for i in range(len(data)):
                j = data[i]
                self.books.append(Book(j["id"],j["author"],j["country"],j["imageLink"],j["language"],j["link"],j["pages"],j["title"],j["year"]))
        self.bookItems = []
        with open('bookitems.json','r') as bookItemRead:
            data = bookItemRead
            for i in range(len(data)):
                j = data[i]
    def getResults(self,input):
        res = []
        for book in self.books:
            if input in book.getString:
                res.append(book)
        return res

        
    

    def addBook(self,author,country,imageLink,language,wikilink,pages,title,year):
        self.books.append(Book(self.pickId(),author,country,imageLink,language,wikilink,pages,title,year))
    
    
    def addBookItem(self,bookTitle):
        for i in self.books:
            if i.getTitle() == bookTitle:
                self.bookItems.append(BookItem)
            else:
                print("No book with title: {} found, please try again.".format(bookTitle))
    
    def parseCatalog(self):
        bookdumper = []
        bookitemdumper = []
        for i in self.books:
            bookdumper.append({
                "id" : i.id,
                "author" : i.author,
                "country" : i.country,
                "imageLink" : i.imageLink,
                "language" : i.language,
                "link" : i.wikiLink,
                "pages" : i.pages,
                "title" : i.title,
                "year" : i.year,
            })
        with open('books.json','w') as bookWrite:
            json.dump(bookdumper,bookWrite)
        for i in self.bookItems:
            bookitemdumper.append({
                "movieId" : i.movie.id
            })
        
        with open('bookitems.json','w') as bookItemWrite:
            json.dump(bookitemdumper,bookItemWrite)
    def pickId(self):
        res = 0
        i = 0
        while i < len(self.books):
            if self.books[i].id == res:
                res += 1
                i = 0
        return res

class LoanAdministration:
    def __init__(self,name):
        self.name = name
        self.loans = []
    
    

