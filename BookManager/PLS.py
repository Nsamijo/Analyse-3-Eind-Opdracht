#import os used to clear the terminal and time to make the thread sleep
import os, time, copy
from datetime import date as date
#self made "modules" to separate it a bit
import BookAdmin, UserClasses, helper, LoanClasses, bookclasses
#this lambda is used to clear the terminal #science
clear = lambda : os.system('cls')

class PLS:
    #variables which are very much needed
    #admin to know if it's a customer or not
    admin = None
    #logged to hold the logged in libarian
    logged = None
    #librarians to hold the librarians
    librarians = None
    #customers to hold all the customers
    customers = None
    #when it's a customer
    user = None

    def __init__(self):
        #initiate the files with the data || read the data in
        self.librarians = UserClasses.Librarians()
        self.customers = UserClasses.Customers()
        self.customers.Load()
        self.loans = LoanClasses.LoanAdministration()
        self.logout = False

    #title
    def printTitle(self):
        print('Public Libary System\n')
    
    #welcome screen
    def welcome(self):

        #welcome screen || check what the person wants to do
        def welcomeScreen(first=True):
            if first:
                clear()
                print('Welcome to the Public Library System (PLS)\nAre you a:\n[1] Customer\n[2] Librarian\n[3] Exiting (to exit)\nPlease enter a number from one of the above!( 1 or 2 )\n')
            else:
                clear()
                print('Public Libary System\n\nPlease enter a valid input!\nAre you a:\n[1] Customer\n[2] Librarian\n[3] EXIT (to exit)\nPlease enter a number from one of the above! ( 1 or 2 )\n')
            return input('>>> ')

        #know where to redirect the user to
        def redirect():
            temp = welcomeScreen()
            #exit the application
            if temp == "3":
                clear()
                print('Exiting Program...')
                time.sleep(0.5)
                clear()
                return False

            #find out if the person is a customer or a librarian
            while temp not in ['1', '2']:
                temp = welcomeScreen(False)
                #check if for exit
                if temp == "3":
                    clear()
                    print('Exiting Program...')
                    time.sleep(0.5)
                    clear()
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
        
        
        def loggedIn():
            clear()
            print("Logged in as:",self.user["GivenName"], self.user["Surname"], '\n')

        def login():
            message = ""
            while True:
                clear()
                self.printTitle()
                print("Login for customers")
                print("Enter EXIT to go back")
                print("Please enter your username or email")
                if message != "":
                    print(message)
                    print()
                usernames = list({d["Username"] : d["Number"] for d in self.customers.customers})
                emails = list({d["EmailAddress"] : d["Number"] for d in self.customers.customers})
                account = input("Username: ")
                if account == "EXIT":
                    self.logout = True
                    self.user = None
                    self.admin = None
                    return True
                else:
                    if account in usernames:
                        self.user = self.customers.getUser(usernames.index(account) + 1)
                        return
                    elif account in emails:
                        self.user = self.customers.getUser(emails.index(account) + 1)
                        return
                    else:
                        message = "Invalid Username"
            
                    
        def options():
            message = ""
            while True:
                loggedIn()
                print("\n[1] See your current loans\n[2] Create a loan\n[3] Exit")
                if message != "":
                    print(message,"\n")
                command = input(">>> ")
                while command not in ['1', '2', '3']:
                    command = input(">>> ")

                if command == '3':
                    self.user = None
                    self.logout = True
                    return True
                elif command == '1':
                    seeloans()
                elif command == '2':
                    createloan()
                


        #loan a book
        def createloan():
            catalog = bookclasses.Catalog("")
            
            abort = False
            message = ""
            while not abort:
                loggedIn()
                command = ""
                
                catalog.printBookItemTable(command)
                booklis = catalog.getResults(command)
                bookitemlis = [item for item in catalog.bookItems if item.book in booklis]
                print('\nEnter which book item you would like to loan!\nEnter EXIT if you wish to leave!\n')
                
                command = input(">>> ")
                if command == "EXIT":
                    abort = True
                else:
                    try:
                        command = int(command)
                        self.loans.addloan(bookitemlis[command-1],self.user["Number"], str(date.today()))
                        print("\nBook loaned Succesfully!")
                        time.sleep(0.5)
                    except ValueError:
                        print("Invalid input")
                    except IndexError: 
                        print("Number not in list of bookitems")
                                
        #search for a book
        def seeloans():

            loans = self.loans.seeLoans(self.user)
            if len(loans) == 0:
                loggedIn()
                print('\nNo loans\nPress enter to return to the menu!')
                input()
            else:
                loggedIn()
                print('\nYou currently have loaned: \n')
                nums = 1
                for x in loans:
                    print(str(nums) + '. ' + "%s"%(x.bookitem.book.title))
                    nums += 1
                print('\nPress enter to go back')
                input()



        #check if the user is logged out or not
        if self.logout == True:
            self.logout = False
            return True

        #while no one is logged on try logging in
        while self.user == None:
            login()
            #go back || check if the user has been reset
            if(self.user == None):
                return True

        options()
        return True
            
    #librarian redirection
    def librarian(self):

        #if login is succesfull
        def loggedIn():
            clear()
            self.printTitle()
            print('Logged in as: ' + self.logged.getName() + '\n')
            
        #login with a librarian account
        def login():
            if self.admin == False:
                self.user = True
            clear()
            self.printTitle()
            print('Login portal for Librarians')
            print('Enter EXIT to go back\n')
            print('Please enter your username and password')

            username = input('\nUsername: ')

            #check for exit
            if username == 'EXIT':
                self.admin = None
                return True

            passwd = input('Password: ')

            #check for exit
            if passwd == 'EXIT':
                self.admin = None
                return True

            self.logged = self.librarians.getAccount(username, passwd)
            if self.logged == None:
                print('\nAccount not found! Please try again!')
                time.sleep(1.0)

        #function that will be able to make changes to customers
        def customerEditing():
            #check what the librarian wants to do
            loggedIn()
            print('What do you wish to do?\n[1] Register customer\n[2] Remove customer\n[3] Edit customer\n[4] Back\n')
            choice = input('>>> ')
            while choice not in ['1', '2', '3', '4']:
                loggedIn()
                print('What do you wish to do?\n[1] Register customer\n[2] Remove customer\n[3] Edit customer\n[4] Back\n')
                choice = input('>>> ')

            #librarian wants to add a new customer
            if choice == '1':
                loggedIn()
                print('\nEnter EXIT to go back (NOTE: nothing will be saved)\nPlease enter all the fields below to register a new customer: \n')
                #all the questions to fill in
                ask = ['Please enter your name: ', 'Please enter your surname: ', 'Please enter a username: ', 'Please enter your preferred language: ','Please enter your address: ','Please enter your zipcode: ','Please enter your city: ','Please enter your email: ','Please enter your telephone number (mobile): ','Please enter your gender ( male / female ): ']
                
                #print all the questions and get the input
                data = []
                for x in ask:
                    #check if there is asked for gender
                    if 'gender' in x:
                        temp = input(x)
                        #there are only 2 genders
                        while temp not in ['male','female']:
                            #re-ask question
                            temp = input(x)
                    else:
                        #ask question normally
                        temp = input(x)

                    #check if the librarian wish to cancel
                    if temp == 'EXIT':
                        #exit
                        return True
                    else:
                        #add the data to the  data list
                        data.append(temp)

            
                loggedIn()
                #print all the data t4o double check
                print('\nPlease confirm that the account below is correct: \n\nUsername: ' + data[2] + '\nFull Name: ' + data[0].title() + ' ' + data[1].title() + '\nNameSet(Language): ' + data[3].title() + '\nGender: ' + data[9].title() +'\nAddress (Combined): ' + data[6].title() + ' ' + data[4].title() + ' ' + data[5] + '\nEmail: ' + data[7] + '\nTelephonenumber: ' + data[8])
                #confirm that all is as should be
                confirm = input('\nEnter yes to save the account or no to discard and go back: ')
                #there all only 2 answers dont stray from the path
                while confirm not in 'yesno':
                    confirm = input('Enter yes to save the account or no to discard and go back: ')
                #everything is cool so the new customer gets saved
                if confirm == 'yes':
                    #update the file with customers
                    self.customers.addUser(data[9], data[3].title(), data[0].title(), data[1].title(), data[4], data[5], data[6], data[7], data[2], data[8])
                    #confirmation
                    print('\Customer has been succesfully added to the system!')
                    time.sleep(1.0)
                else:
                    #exit if it is no
                    print('\Customer has not been added to the system!')
                    time.sleep(0.5)
                    return True

                return True
            #remove customer
            elif choice == '2':
                while True:
                    #ingelogd
                    loggedIn()
                    #print the customers yeet
                    helper.printAllCustomers(self.customers.customers)
                    print('Please enter which you customer you would like to remove! Enter EXIT to go back!')
                    user = input('>>> ')
                    while True:

                        while True:
                            if user.isdigit():
                                if int(user) <= len(self.customers.customers) and int(user) > 0:
                                    break
                            elif user == 'EXIT':
                                return True
                            else:
                                user = input('Please enter a valid number or EXIT to go back >>> ')

                        loggedIn()
                        #prompt if the customer has to be deleted
                        print('\nDo you wish to remove the customer: ' + self.customers.getUser(int(user))['Username'] + '? (yes/no)')
                        temp = input('>>>')
                        while temp not in ['yes', 'no']:
                            temp = input('Please enter yes or no >>> ')

                        #yeet the customer away with the might of ZEUS
                        if temp == 'yes':
                            self.customers.removeUser(int(user))
                            user = None
                            print('\nCustomer has been removed succesfully from the system!')
                            time.sleep(1.0)
                            break
                        #keep the customer
                        else:
                            print('Customer has not been removed from the system!')
                            time.sleep(1.0)
                            break
                
            elif choice == '3':
                loggedIn()
                #print all the customers in the system
                helper.printAllCustomers(self.customers.customers)
                print('Please enter which you customer you would like to modify!')
                #check if the input is valid
                choice = input('>>> ')
                while True:
                    if choice.isdigit():
                        if int(choice) - 1 < len(self.customers.customers) and int(choice) > 0:
                            break
                    else:
                        choice = input('Please enter a valid number >>> ')
                
                #get the customer from the file and store the attributes in a list
                names =['Gender','NameSet' ,'GivenName' ,'Surname' ,'StreetAddress' ,'ZipCode' ,'City' ,'EmailAddress' ,'Username','TelephoneNumber']
                toEdit = self.customers.getUser(int(choice))
                editCopy = toEdit.copy()

                #when already selected a customer
                #stay in this loop till the librarian exits
                #variable to check if the librarian saved
                saved = False
                while True:
                    loggedIn()
                    nums = 1
                    for x in names:
                        print('[' + str(nums) + ']' + ' ' + x +': ' + editCopy[x])
                        nums += 1

                    #input check
                    print('\n\nEnter SAVE to save the changes (Saved: ' + str(saved) + ')\nEnter EXIT to exit (Changes will not be saved if not saved!)')
                    print('What would you like to modify?') 
                    change = input('>>> ')
                    while True:
                        #save the changes made
                        if change == 'SAVE':
                            self.customers.editUser(int(choice), editCopy)
                            saved = True
                            break
                        #exit back to the customer menu going back to the main menu
                        elif change == 'EXIT':
                            return True
                        #check if it;s a number representing one of the customer's attributes
                        elif change.isdigit():
                            if int(change) - 1 < len(names):
                                break
                        #input does not match anything
                        else:
                            change = input('Please enter a valid option >>> ')
                    
                    #check if the librarian saved
                    if change != 'SAVE':
                        #if not then prompt the librarian to make a change
                        if names[int(change) - 1] == 'Gender':
                            #change the gender
                            temp = input('Please enter your gender (male/female): ')
                            while temp not in ['male', 'female']:
                                temp = input('Please enter your gender (male/female): ')
                            editCopy[names[int(change) - 1]] = temp
                            saved = False
                        else:
                            #change everything except gender
                            print('Change ' + names[int(change) - 1] + ': ' + toEdit[names[int(change) - 1]])
                            temp = input( 'New ' + names[int(change) - 1] + ': ')
                            editCopy[names[int(change) - 1]] = temp
                            saved = False

            elif choice == '4':
                #exit the menu
                return False
            
            #stay in this menu
            return True

        def editStaff():
            loggedIn()
            #print the options
            print('What would you like to do?\n[1] Add Librarian\n[2] Remove Librarian Account\n[3] Back (Go back to the menu)')
            choice = input('>>> ')
            while choice not in ['1', '2', '3', '4']:
                choice = input('Please enter a valid number >>> ')
            
            #go back to the menu
            if choice == '3':
                return False
            #add a librarian to the book club
            elif choice == '1':
                loggedIn()
                print('\nEnter EXIT to exit\n')
                #holder for the data
                data =[]
                #holder for question
                holder = 'Please enter '
                #questions
                questions = ['a name: ', 'a surname: ', 'a username: ', 'your gender (M/F): ', 'a email: ', 'a password: ']
                #interrogation jk just asking for the data of the librarian
                for x in questions:
                    temp = input(holder + x)
                    #exit
                    if 'EXIT' == temp:
                        return True
                    #if the gender part is reached only 2 answers are allowed
                    elif 'gender' in temp:
                        #check if the answer given is allowed
                        while temp not in ['M', 'F']:
                            #reask to enter gender
                            temp = input(holder + x)
                    else:
                        #add data to the list
                        data.append(temp)
                loggedIn()
                print('Enter yes or no if the data is correct\nEntering yes will automatically save the data\nEntering no will discard all\n')
                print('\nFull Name: ' + data[0].title() + ' ' + data[1].title() + '\nUsername: ' + data[2] + '\nGender: ' + data[3] + '\nEmailAddress: ' + data[4] + '\nPassword: ' + data[5])

                save = input('>>> ')
                while save not in ['yes', 'no']:
                    save = input('Please enter yes or no >>> ')

                if save == 'yes':
                    #add a new librarian to the system
                    self.librarians.addLibrarian(data[0].title(), data[1].title(), data[2], data[3], data[4], data[5])
                    print('Succesfully added a new Librarian to the system! You will be redirected...')
                    time.sleep(1.0)
                    return True
                else:
                    #do not add the user. you will be redirected to the menu
                    print('Librarian has not been added to the system! You will be redirected...')
                    time.sleep(1.0)
                    return True
            #change a certain user
            elif choice == '2':
                loggedIn()
                #index of the logged account
                indexL = self.librarians.librarians.index(self.logged)
                #print the librarians except the current
                helper.printAllLibrarians(self.librarians.librarians, self.logged)
                #instructions
                print('\nPlease enter which Librarian you wish to remove!\n NOTE: You will not be able to remove the account that you are logged in with currently\nEnter EXIT to go back\n')
                #input
                choice = input('>>> ')
                account = None
                indexA = None
                while account == None:
                    if choice.isdigit():
                        if int(choice)< len(self.librarians.librarians) and int(choice) > 0:
                            ind = int(choice) - 1
                            if ind >= indexL:
                                ind += 2
                            account = self.librarians.getLib(ind)
                            indexA = ind
                            break
                        else:
                            choice = input('Please enter a valid option >>> ') 
                        
                    elif choice == "EXIT":
                        return True

                loggedIn()
                print('\n Do you wish to delete Librarian: ' + account.Name + ' ' + account.SurName + '?(yes/no)')
                answer = input('>>> ')
                while answer not in 'yesno':
                    answer = input('Please enter yes or no >>> ')
                
                if answer == 'yes':
                    self.librarians.removeLibrarian(account)
                    print('\nLibrarian has been removed succesfully!\n')
                    time.sleep(0.5)
                else:
                    print('\nLibrarian has not been removed!\n')
                    time.sleep(0.5)
                
            #keep the loop running till the librarian exits
            return True

        #handeling all the options that the librarian can and cannot do
        def options():
            loggedIn()
            print('Where do you wish to go?\n[1] Library\n[2] Customers\n[3] Staff\n[4] Log out\nPlease enter an number\n')
            choice = input('>>> ')
            while choice not in ['1', '2', '3', '4']:
                clear()
                loggedIn()
                print('Where do you wish to go?\n[1] Library\n[2] Customers\n[3] Staff\n[4] Log out\nPlease enter a number that is part of the selection\n')
                choice = input('>>> ')

            #books
            if choice == '1':
                BookAdmin.main(self.logged)
            #customers
            elif choice == '2':
                loop = True
                while loop:
                    loop = customerEditing()
            #staff
            elif choice == '3':
                loop = True
                while loop:
                    loop = editStaff()
            #logging out
            elif choice == '4':
                loggedIn()
                print('\nAre you sure you wish to log out? ( yes / no )')
                temp = input('>>> ')
                while temp.lower() not in ['yes', 'no']:
                    temp = input('Please enter yes or no >>> ')
                if temp == 'yes':
                    self.admin = None
                    self.logged = None

        #check if the user is logged out or not
        if self.admin == None:
            return False

        #while no one is logged on try logging in
        while self.logged == None:
            login()
            #go back || check if the admin has been reset
            if(self.admin == None):
                return True

        options()
        return True

    #all the logic for the PLS so it's basically the system
    def system(self):
        loop = True
        while loop: 

            while self.admin == None and loop != False:
                loop = self.welcome()

            if loop:
                if self.admin:
                    loop = self.librarian()
                else:
                    loop = self.customer()

#this is the main you know where the system knows where to run the stuff
if __name__ == '__main__':
    system = PLS()
    system.system()