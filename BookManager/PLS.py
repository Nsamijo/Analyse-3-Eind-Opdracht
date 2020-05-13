import os, time
import BookAdmin, UserClasses
clear = lambda : os.system('cls')

class PLS:
    admin = None
    logged = None
    librarians = None
    customers = None

    def __init__(self):
        self.librarians = UserClasses.Librarians()
        self.customers = UserClasses.Customers()
    #title
    def printTitle(self):
        print('Public Libary System\n')
    
    #welcome screen
    def welcome(self):

        #welcome screen || check what the person wants to do
        def welcomeScreen(first=True):
            if first:
                #clear()
                print('Welcome to the Public Library System (PLS)\nAre you a:\n1. Customer\n2. Librarian\n\nEnter EXIT to exit\nPlease enter a number from one of the above!( 1 or 2 )\n')
            else:
                clear()
                print('Public Libary System\n\nPlease enter a valid input!\nAre you a:\n1. Customer\n2. Librarian\n\nEnter EXIT to exit\nPlease enter a number from one of the above! ( 1 or 2 )\n')
            return input('>>> ')

        #know where to redirect the user to
        def redirect():
            temp = welcomeScreen()
            #exit the application
            if temp == "EXIT":
                return False

            while temp not in ['1', '2']:
                temp = welcomeScreen(False)
                #check if for exit
                if temp == "EXIT":
                    return False

            #check if it's a librarian these are admins
            if temp == '1':
                self.admin = False
            else:
                self.admin = True
            return True
        #check where to redirect the user to
        return redirect()
        
    #customer redirection
    def customer(self):
        #loan a book
        #search for a book
        return

    #librarian redirection
    def librarian(self):

        #if login is succesfull
        def loggedIn():
            clear()
            self.printTitle()
            print('Logged in as: ' + self.logged.getName())

        #login with a librarian account
        def login():
            clear()
            self.printTitle()
            print('Login portal for Librarians')
            print('Enter EXIT to go back\n')
            print('Please enter your username and password')

            username = input('username: ')

            #check for exit
            if username == 'EXIT':
                self.admin = None
                return

            passwd = input('password: ')

            #check for exit
            if passwd == 'EXIT':
                self.admin = None
                return

            self.logged = self.librarians.getAccount(username, passwd)
            if self.logged == None:
                print('\nAccount not found! Please try again!')
                time.sleep(1.0)

            #handeling all the options that the librarian can and cannot do
            def options():
                loggedIn()
                print('Where do you wish to go?\n[1] Library\n[2] ')
                
        #while no one is logged on try logging in
        while self.logged == None:
            login()
            #go back || check if the admin has been resetted
            if(self.admin == None):
                return


    #all the logic for the PLS so it's basically the system
    def system(self):
        loop = True
        while loop: 

            while self.admin == None and loop != False:
                loop = self.welcome()

            if loop:
                if self.librarian:
                    self.librarian()
                else:
                    self.customer()

#this is the main you know where the system knows where to run the stuff
if __name__ == '__main__':
    system = PLS()
    system.system()