#import os used to clear the terminal and time to make the thread sleep
import os, time
#self made "modules" to separate it a bit
import BookAdmin, UserClasses, helper
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

    def __init__(self):
        #initiate the files with the data || read the data in
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
                    print('\nUser has been succesfully added to the system!')
                    time.sleep(1.0)
                else:
                    #exit if it is no
                    return True

                return True

            elif choice == '2':
                while True:
                    loggedIn()
                    #print all customers from the system
                    helper.printAllCustomers(self.customers.customers)
                    #check which customer to yeet away (delete)
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
                    #prompt if the customer has to be deleted
                    print('\nDo you wish to remove the customer: ' + self.customers.getUser(int(choice))['Username'] + '? (yes/no)')
                    temp = input('>>>')
                    while temp not in 'yesno':
                        temp = input('Please enter yes or no >>>')

                    #yeet the customer away with the might of ZEUS
                    if temp == 'yes':
                        self.customers.removeUser(int(choice))
                        print('\nCustomer has been removed succesfully from the system!')
                    #keep the customer
                    else:
                        print('Customer has not been removed from the system!')
                        time.sleep(1.0)
                
            elif choice == '3':
                loggedIn()
                #print all the customers in the system
                helper.printAllCustomers(self.customers.customers)
                print('Please enter which you user you would like to Change!')
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
                        #save the changes made
                        if change == 'SAVE':
                            self.customers.editUser(int(choice), editCopy)
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
                        else:
                            #change everything except gender
                            print('Change ' + names[int(change) - 1] + ': ' + toEdit[names[int(change) - 1]])
                            temp = input(names[int(change) - 1] + ': ')
                            editCopy[names[int(change) - 1]] = temp

            elif choice == '4':
                #exit the menu
                return False
            
            #stay in this menu
            return True

        def editStaff():

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
                    loop = self.customer()

#this is the main you know where the system knows where to run the stuff
if __name__ == '__main__':
    system = PLS()
    system.system()