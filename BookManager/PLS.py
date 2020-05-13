import bookclasses
import os
clear = lambda : os.system('cls')




def main():
    abort = False
    while not abort:
        print("[1] Book manager\n[2] Bookitem manager\n[3] Exit\n")

        no = input(">>> ")
        try:
            no = int(no)
        except:
            clear()
            print("Try again")
            no = ""
        if no != "" and 3 >= no >= 1:
            if(no == 1):
                clear()
                BookManager()
            if(no == 2):
                clear() 
                BookItemManager()
            if(no == 3):
                clear()
                print("Exitting...")
                abort = True
        

    

def BookItemManager():
    abort = False
    while not abort:
        print("[1] Add bookitem\n[2] Remove bookitem\n[3] View bookitems\n[4] Back")
        no = input(">>> ")
        try:
            no = int(no)
        except:
            clear()
            print("Invalid input")
        else:
            if no == 1:
                clear()
                addBookItem()
            if no == 2:
                clear()
                removeBookItem()
            if no == 3:
                clear()
                viewBookItems()
            if no == 4:
                clear()
                abort = True
def addBookItem():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    message = ""
    while not abort:
        clear()
        print("Type \"EXIT\" to exit\nOr type anything else to search for a book")
        
        
        if message != "":
            print("\n" + message + "\n")
        command = input(">>> ")
        if command == "e":
            clear()
            abort = True
        else:
            catalog.printBooks(command)
            print("\nType de number of the book you'd like to make a bookitem of")
            command = input(">>> ")
            try:
                command = int(command)
                catalog.addBookItem(catalog.books[command-1].id)
                message = "Bookitem added"
            
            except IndexError:
                clear()
                message = "Not in the list"
            except ValueError:
                clear()
                message = "Invalid input"
            except:
                message = "Whao"
            else:
                message = ""
            

def viewBookItems():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    while not abort:
        print("\nType \"EXIT\" to exit\nOr type anything else to search\n")
        command = input(">>> ")
        
        if command == "e":
            abort = True
            clear()
        else:
            clear()
            catalog.printBookItemTable(input)

def removeBookItem():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    message = ""
    while not abort:
        print("\nType \"EXIT\" to exit\nOr type anything else to search\n")
        command = input(">>> ")
        if command == "EXIT":
            abort = True
        else:
            lis = [item for item in catalog.bookItems if command in item.book.getString()]
            catalog.printBookItemTable(command)
            print("Type the number of the book you'd like to delete\nOr type \"EXIT\" if you want to leave\n")
            command = input(">>> ")
            if command != "EXIT":
                try:
                    command = int(command)
                    catalog.bookItems.remove(lis[command-1])
                    clear()
                    message = "Bookitem deleted"
                except IndexError:
                    clear()
                    message = "Not in list"
                except ValueError:
                    clear()
                    message = "Invalid input"

            else:
                abort = True

        

    

def BookManager(): 
    abort = False
    while not abort:
        print("[1] Add book \n[2] View books \n[3] Remove book \n[4] Change book\n[5] Back\n")
        no = input(">>> ")
        try:
            no = int(no)
        except:
            no = ""
        if no != "" and 1 <= no <= 5:
            if no == 1:
                clear()
                addBook()
            if no == 2:
                clear()
                printBooks()
            if no == 3:
                clear()
                removeBook()
            if no == 4:
                clear()
                changeBook()
            if no == 5:
                clear()
                abort = True
        else:
            clear()
            print("Try again")
def addBook(inputs = {
        "author" : "",
        "country" : "",
        "imagelink" : "",
        "language" : "",
        "wikilink" : "",
        "pages" : "",
        "title" : "",
        "year" : ""}):
    catalog = bookclasses.Catalog("catalog")
    
    error = ""

    

    abort = False
    while not abort:
        print("To assign a value, type: variable=value")
        print("For example: author=J.K. Rowling")
        print("When you're done and want to save the book, type \"s\"")
        print("Else if you want to exit, type \"e\"\n")
        print("Author: %s"%(inputs["author"]))
        print("Country: %s"%(inputs["country"]))
        print("Imagelink: %s"%(inputs["imagelink"]))
        print("Language: %s"%(inputs["language"]))
        print("Wikilink: %s"%(inputs["wikilink"]))
        print("Pages: %s"%(inputs["pages"]))
        print("Title: %s"%(inputs["title"]))
        print("Year: %s"%(inputs["year"]))
        print(error + "\n")
        command = input(">>> ")
        if command != 'e' and command != 's':
            command = command.split("=")
            if len(command) >= 2:
                try:
                    inputs[command[0]] = command[1]
                except:
                    clear()
                    error = "No variable with that name"
            elif len(command) == 1:
                for var in inputs:
                    if inputs[var] == "":
                        inputs[var] = command[0]
                        break
        else:
            abort = True
            clear()

    if command == "s":
        catalog.addBook(*[inputs[k] for k in inputs])
def changeBook():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    message = ""
    while not abort:
        print("Search for the book you'd like to edit\nType \"EXIT\" if you want to leave")
        if message != "":
            print("\n",message,"\n")

        command = input(">>> ")
        if command != "EXIT":
            lis = catalog.getResults(command)
            catalog.printBooks(command)
            print("\nType the number of the book you'd like to edit\n")
            command = input(">>> ")
            if command != "EXIT":
                try:
                    command = int(command)
                    book = lis[command-1]
                    error = ""
                    inputs = {
                        "author" : book.author,
                        "country" : book.country,
                        "imagelink" : book.imageLink,
                        "language" : book.language,
                        "wikilink" : book.wikilink,
                        "pages" : book.pages,
                        "title" : book.title,
                        "year" : book.year}
                    abort = False
                    while not abort:
                        print("To assign a value, type: variable=value")
                        print("For example: author=J.K. Rowling")
                        print("When you're done and want to save the book, type \"s\"")
                        print("Else if you want to exit, type \"e\"\n")
                        print("Author: %s"%(inputs["author"]))
                        print("Country: %s"%(inputs["country"]))
                        print("Imagelink: %s"%(inputs["imagelink"]))
                        print("Language: %s"%(inputs["language"]))
                        print("Wikilink: %s"%(inputs["wikilink"]))
                        print("Pages: %s"%(inputs["pages"]))
                        print("Title: %s"%(inputs["title"]))
                        print("Year: %s"%(inputs["year"]))
                        print(error + "\n")
                        command = input(">>> ")
                        if command != 'e' and command != 's':
                            command = command.split("=")
                            if len(command) >= 2:
                                try:
                                    inputs[command[0]] = command[1]
                                except:
                                    clear()
                                    error = "No variable with that name"
                            elif len(command) == 1:
                                for var in inputs:
                                    if inputs[var] == "":
                                        inputs[var] = command[0]
                                        break
                        else:
                            abort = True
                            clear()

                    if command == "s":
                        catalog.books.remove(book)
                        catalog.addBook(*[inputs[k] for k in inputs])
                except ValueError:
                    clear()
                    message = "Invalid input"
                except IndexError:
                    clear()
                    message = "Wrong number"
                except:
                    clear()
                    message = "whoa"
            else:
                clear()
                abort = True

                
        else:
            abort = True
    
def printBooks():
    catalog = bookclasses.Catalog("catalog")
    while True:
        
        print("Type \"EXIT\" to leave\nOr type anything else to search for a book\n")
        command = input(">>> ")
        if command == "EXIT":
            clear()
            break
        else:
            clear()
            catalog.printBooks(command.lower())

def removeBook():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    while not abort:
        
        print("\nType the number of the book you would like to delete")
        print("\nWhen you want to leave type \"EXIT\"\n")
        command = input(">>> ")
        if command != "EXIT":
            catalog.printBooks(command)
            lis = catalog.getResults(command)
            command = input(">>> ")
            if(command != "EXIT"):
                try:
                    Print("Type the number of the book you'd like to remove")
                    command = int(command)
                    catalog.books.remove(lis[command-1])
                    catalog.parseCatalog()
                except:
                    clear()
                    print("Invalid input")
                else:
                    abort = True
                    clear()
        else:
            abort = True
            clear()
            
if __name__ == "__main__":
    main()
