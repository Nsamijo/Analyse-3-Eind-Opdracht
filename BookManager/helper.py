def getLongestBookLengths(lis):
    if len(lis) > 0:
        titles = [book.title for book in lis]
        authors = [book.author for book in lis]
        years = [str(book.year) for book in lis]
        links = [book.wikilink for book in lis]

        lengths = [len(max(titles,key=len)),len(max(authors,key=len)),len(max(years,key=len)),len(max(links,key=len))]
        return lengths    
    else: 
        return []


def printBookTable(lis):
    lens = getLongestBookLengths(lis)
    if(lens != []):
        i = 1
        print("No.    Title",(lens[0]-5)*" ","Author",(lens[1]-6)*" ","Year",(lens[2]-4)*" ","Wikilink",(lens[3]-8)*" ")
        for book in lis:
            print(str(i),".",(4-len(str(i)))*" ",book.title,(lens[0]-len(book.title))*" ",book.author,(lens[1]-len(book.author))*" ",str(book.year),(lens[2]-len(str(book.year)))*" ",book.wikilink,(lens[3]-len(book.wikilink))*" ")
            i += 1
    else:
        print("No books")

def printAllCustomers(lis):
    print ("{:<15} {:<15} {:<15} {:<15} {:<20}".format('Number','Gender', 'GivenName', 'Surname', 'Username'))
    for x in lis:
        print ("{:<15} {:<15} {:<15} {:<15} {:<20}".format(x['Number'],x['Gender'], x['GivenName'], x['Surname'], x['Username']))