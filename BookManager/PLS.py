import os, time
import BookAdmin, UserClasses, helper
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

            username = input('\nUsername: ')

            #check for exit
            if username == 'EXIT':
                self.admin = None
                return

            passwd = input('Password: ')

            #check for exit
            if passwd == 'EXIT':
                self.admin = None
                return

            self.logged = self.librarians.getAccount(username, passwd)
            if self.logged == None:
                print('\nAccount not found! Please try again!')
                time.sleep(1.0)

        #function that will be able to make changes to customers
        def customerEditing():
            loggedIn()
            print('What do you wish to do?\n[1] Register customer\n[2] Remove customer\n[3] Edit customer\n[4] Back\n')
            choice = input('>>> ')
            while choice not in ['1', '2', '3', '4']:
                loggedIn()
                print('What do you wish to do?\n[1] Register customer\n[2] Remove customer\n[3] Edit customer\n[4] Back\n')
                choice = input('>>> ')

            if choice == '1':
                loggedIn()
                print('\nEnter EXIT to go back (NOTE: nothing will be saved)\nPlease enter all the fields below to register a new customer: \n')
                #all the questions to fill in
                ask = ['Please enter your name: ', 'Please enter your surname: ', 'Please enter a username: ', 'Please enter your preferred language: ','Please enter your address: ','Please enter your zipcode: ','Please enter your city: ','Please enter your email: ','Please enter your telephone number (mobile): ','Please enter your gender ( male / female ): ']
                
                data = []
                for x in ask:
                    if 'gender' in x:
                        temp = input(x)
                        while temp not in ['male','female']:
                            temp = input(x)
                    else:
                        temp = input(x)

                    if temp == 'EXIT':
                        return True
                    else:
                        data.append(temp)

            
                loggedIn()
                print('\nPlease confirm that the account below is correct: \n\nUsername: ' + data[2] + '\nFull Name: ' + data[0].title() + ' ' + data[1].title() + '\nNameSet(Language): ' + data[3].title() + '\nGender: ' + data[9].title() +'\nAddress (Combined): ' + data[6].title() + ' ' + data[4].title() + ' ' + data[5] + '\nEmail: ' + data[7] + '\nTelephonenumber: ' + data[8])

                confirm = input('\nEnter yes to save the account or no to discard and go back: ')
                while confirm not in 'yesno':
                    confirm = input('Enter yes to save the account or no to discard and go back: ')

                if confirm == 'yes':
                    self.customers.addUser(data[9], data[3].title(), data[0].title(), data[1].title(), data[4], data[5], data[6], data[7], data[2], data[8])
                    print('\nUser has been succesfully added to the system!')
                    time.sleep(1.0)
                else:
                    return True

                return True

            elif choice == '2':
                while True:
                    loggedIn()
                    helper.printAllCustomers(self.customers.customers)
                    print('Please enter which you user you would like to remove! Enter EXIT to go back!')
                    choice = input('>>> ')
                    while True:
                        if choice.isdigit():
                            if int(choice) - 1 < len(self.customers.customers):
                                break
                        elif choice == 'EXIT':
                            return True
                        else:
                            choice = input('Please enter a valid number or EXIT to go back >>> ')

                    loggedIn()
                    print('\nDo you wish to remove the customer: ' + self.customers.getUser(int(choice))['Username'] + '? (yes/no)')
                    temp = input('>>>')
                    while temp not in 'yesno':
                        temp = input('Please enter yes or no >>>')

                    if temp == 'yes':
                        self.customers.removeUser(int(choice))
                        print('\nCustomer has been removed succesfully from the system!')
                    else:
                        print('Customer has not been removed from the system!')
                        time.sleep(1.0)
                
            elif choice == '3':
                loggedIn()
                helper.printAllCustomers(self.customers.customers)
                print('Please enter which you user you would like to Change!')
                choice = input('>>> ')
                while True:
                    if choice.isdigit():
                        if int(choice) - 1 < len(self.customers.customers):
                            break
                    else:
                        choice = input('Please enter a valid number >>> ')
                
                names =['Gender','NameSet' ,'GivenName' ,'Surname' ,'StreetAddress' ,'ZipCode' ,'City' ,'EmailAddress' ,'Username','TelephoneNumber']
                toEdit = self.customers.getUser(int(choice))
                editCopy = toEdit.copy()

                while True:
                    loggedIn()
                    print('What attribute would you like to change?') 
                    nums = 1
                    for x in names:
                        print('[' + str(nums) + ']' + ' ' + x +': ' + editCopy[x])
                        nums += 1

                    #input check
                    print('\n\nEnter SAVE to save the changes\nEnter EXIT to exit (Changes will not be saved if not saved!)')
                    change = input('>>> ')
                    while True:
                        if change == 'SAVE':
                            self.customers.editUser(int(choice), editCopy)
                            break
                        elif change == 'EXIT':
                            return True

                        elif change.isdigit():
                            if int(change) - 1 < len(names):
                                break
                        else:
                            change = input('Please enter a valid number >>> ')
                    if change != 'SAVE':
                        if names[int(change) - 1] == 'Gender':
                            temp = input('Please enter your gender (male/female): ')
                            while temp not in ['male', 'female']:
                                temp = input('Please enter your gender (male/female): ')
                            editCopy[names[int(change) - 1]] = temp
                        else:
                            print('Change ' + names[int(change) - 1] + ': ' + toEdit[names[int(change) - 1]])
                            temp = input(names[int(change) - 1] + ': ')
                            editCopy[names[int(change) - 1]] = temp

            elif choice == '4':
                return False
            
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
                pass
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
            #go back || check if the admin has been resetted
            if(self.admin == None):
                return False

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
                    self.customer()

#this is the main you know where the system knows where to run the stuff
if __name__ == '__main__':
    system = PLS()
    system.system()