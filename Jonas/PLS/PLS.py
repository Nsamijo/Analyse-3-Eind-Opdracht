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
            if no == 1:
                clear()
                addBookItem()
        except:
            clear()
            print("Invalid input")
def addBookItem():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    while not abort:
        pass
    
def BookManager(): 
    abort = False
    while not abort:
        print("[1] Add book [2] View books [3] Remove book [4] Back")
        no = input(">>> ")
        try:
            no = int(no)
        except:
            no = ""
        if no != "" and 1 <= no <= 4:
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
                abort = True
        else:
            clear()
            print("Try again")
def addBook():
    catalog = bookclasses.Catalog("catalog")
    inputs = {
        "author" : "",
        "country" : "",
        "imagelink" : "",
        "language" : "",
        "wikilink" : "",
        "pages" : "",
        "title" : "",
        "year" : ""
    }
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
def printBooks():
    catalog = bookclasses.Catalog("catalog")
    while True:
        catalog.printBooks()
        print("Type \"e\" to leave")
        command = input(">>> ")
        if command == "e":
            clear()
            break
        else:
            clear()
def removeBook():
    catalog = bookclasses.Catalog("catalog")
    abort = False
    while not abort:
        catalog.printBooks()
        print("\nType the number of the book you would like to delete")
        print("\nWhen you want to leave type \"e\"\n")
        command = input(">>> ")
        if command != "e":
            try:
                command = int(command)
                catalog.removeBook(command-1)
            except:
                clear()
                print("Invalid input")
        else:
            abort = True
            clear()
            
if __name__ == "__main__":
    main()
