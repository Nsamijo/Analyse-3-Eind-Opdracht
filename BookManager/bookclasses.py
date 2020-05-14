import json
import os
import helper
#path to current directory, this variable is dynamic for different computers
curdir = os.path.dirname(os.path.realpath(__file__))
#Class for book
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
    #returns a string used for searching for a book
    def getString(self):
        return ("" + self.author + self.language + self.title + str(self.year) + self.country).lower()
#Bookitem class, only inherits a book
class BookItem:
    def __init__(self,id,book,status="available"):
        self.id = id
        self.book = book
        self.status = status
    #change the status of a book
    def changeStatus(self,status):
        self.status = status
#Catalog class, contains books and bookitems
class Catalog:
    #reads books and bookitems from jsons
    def __init__(self,name):
        self.name = name
        self.books = []
        with open(curdir + '/src/books.json','r') as bookRead:
            data = json.load(bookRead)
            for i in range(len(data)):
                j = data[i]
                self.books.append(Book(j["id"],j["author"],j["country"],j["imageLink"],j["language"],j["link"],j["pages"],j["title"],j["year"]))
        self.bookItems = []
        with open(curdir + '/src/bookitems.json','r') as bookItemRead:
            data = json.load(bookItemRead)
            for i in range(len(data)):
                j = data[i]
                self.bookItems.append(BookItem(j["id"],self.getBookbyId(j["BookId"]),j["Status"]))
    #returns an array with all the books where inp is in the getString() func
    def getResults(self,inp):
        res = []
        for book in self.books:
            if inp in book.getString():
                res.append(book)
        return res
        
    
    #adds a book to the self.books array
    def addBook(self,author,country,imageLink,language,wikilink,pages,title,year):
        self.books.append(Book(self.pickId(),author,country,imageLink,language,wikilink,pages,title,year))
        self.parseCatalog()
    
    #adds a bookitem to the self.bookitems array
    def addBookItem(self,ID):
        for i in self.books:
            if i.id == ID:
                self.bookItems.append(BookItem(self.pickItemId(),i))
                self.parseCatalog()
                return True
        return False
            
    #parses the catalog back to the jsons
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
                "link" : i.wikilink,
                "pages" : i.pages,
                "title" : i.title,
                "year" : i.year,
            })
        with open(curdir + '/src/books.json','w') as bookWrite:
            json.dump(bookdumper,bookWrite, indent=4, sort_keys=True)
        for i in self.bookItems:
            bookitemdumper.append({
                "id" : i.id,
                "BookId" : i.book.id,
                "Status" : i.status
            })
        
        with open(curdir +'/src/bookitems.json','w') as bookItemWrite:
            json.dump(bookitemdumper,bookItemWrite, indent=4, sort_keys=True)
    #picks a bookid based on what is already in the array
    def pickId(self):
        res = 0
        i = 0
        while i < len(self.books):
            if self.books[i].id == res:
                res += 1
                i = 0
            else:
                i += 1
        return res
    #same as pickid, just for bookitems
    def pickItemId(self):
        res = 0
        i = 0
        while i < len(self.bookItems):
            if self.bookItems[i].id == res:
                res += 1
                i = 0
            else:
                i += 1
        return res
    #removes a book at an index
    def removeBook(self,index):
        self.books.pop(index)
        self.parseCatalog()
    #Prints all books in self.books
    def printBooks(self,search):
        lis = self.getResults(search)
        helper.printBookTable(lis)
    #returns a book with Id
    def getBookbyId(self,ID):
        for book in self.books:
            if book.id == ID:
                return book
    #prints all bookitems
    def printBookItemTable(self,inp):
        booklis = self.getResults(inp.lower())
        lis = [item for item in self.bookItems if item.book in booklis]
        
        if(lis != []):
            booklen = len(max([item.book.title for item in lis],key=len))
            i = 1
            print("No.    ","Title",(booklen-5)*" ","status")
            for item in lis:
                
                print(str(i)+".",(5-len(str(i)))*" ",item.book.title,(booklen-len(item.book.title))*" ",item.status)
                i += 1