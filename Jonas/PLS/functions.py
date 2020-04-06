import json
import classes

#input bookcatalog and book parameters, and returns the catalog with an extra book added
def addBooktoCatalog(catalog,author,country,imageLink,language,link,pages,title,year):
    catalog.addBook(author,country,imageLink,language,link,pages,title,year)
    return catalog

#retrieves books from 'books.json' file and returns an array containing book objects
def retrieveBooks():
    catalog = classes.Catalog("main")
    with open('books.json','r') as bookRead:
        data = json.load(bookRead)
    
    for i in data:
        catalog.addBook(i["author"],i["country"],i["imageLink"],i["language"],i["link"],i["pages"],i["title"],i["year"])
        for _ in range(i["amount"]):
            catalog.addBookItem(i.title)
    return catalog

#puts the data of the book objects into a
def parseCatalog(catalog):
    dumper = []
    
    for i in catalog.books:
        amount = 0
        for j in catalog.bookItems:
            if j.book == i:
                amount += 1

        dumper.append({
            "author" : i.author,
            "country" : i.country,
            "imageLink" : i.imageLink,
            "language" : i.language,
            "link" : i.wikiLink,
            "pages" : i.pages,
            "title" : i.title,
            "year" : i.year,
            "amount" : amount
        })
    with open('books.json','w') as bookWrite:
        json.dump(dumper,bookWrite)



        