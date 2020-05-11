def getLongestLengths(lis):
    titles = [book.title for book in lis]
    authors = [book.author for book in lis]
    years = [book.year for book in lis]
    links = [book.wikilink for book in lis]

    lengths = [len(max(titles,key=len)),len(max(authors,key=len)),len(max(years,key=len)),len(max(links,key=len))]
    return lengths    

    


def printBookTable(lis):
    lens = getLongestLengths(lis)
    i = 1
    print("No.    Title",(lens[0]-5)*" ","Author",(lens[1]-6)*" ","Year",(lens[2]-4)*" ","Wikilink",(lens[3]-8)*" ")
    for book in lis:
        print(str(i),".",(4-len(str(i)))*" ",book.title,(lens[0]-len(book.title))*" ",book.author,(lens[1]-len(book.author))*" ",book.year,(lens[2]-len(book.year))*" ",book.wikilink,(lens[3]-len(book.wikilink))*" ")