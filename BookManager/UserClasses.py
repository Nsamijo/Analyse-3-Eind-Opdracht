import csv, os, json
import collections

curdir = os.path.dirname(os.path.realpath(__file__))

#customers handeling
class Customers:

    customers = []

    def __init__(self):
        with open(curdir + '/src/customers.csv', 'r') as File:
            reader = csv.DictReader(File)
            for row in reader:
                self.customers.append(row)

    def UpdateCSV(self):
            temp = []
            for i in self.customers:
                temp.append(dict(i))

            names =['Number', 'Gender','NameSet' ,'GivenName' ,'Surname' ,'StreetAddress' ,'ZipCode' ,'City' ,'EmailAddress' ,'Username','TelephoneNumber']

            with open(curdir + '/src/customers.csv', 'w') as File:
                writer = csv.DictWriter(File, fieldnames=names)
                writer.writeheader()
                writer.writerows(temp)

    def getUser(self, user):
        return self.customers[user - 1]
        
    def removeUser(self, user):
        self.customers.remove(self.customers[user - 1])
        self.UpdateCSV()

    def editUser(self, user, data):
        self.customers[user - 1] = data
        self.UpdateCSV()

    def addUser(self, gender, nameset, givennam, surnam, adres, zipcode, city, email, usernam, telephon):
        """make another user and update the file"""

        user = {}
        user['Number'] = str(int(self.customers[-1]['Number']) + 1)
        user['Gender'] = gender
        user['NameSet'] = nameset
        user['GivenName'] = givennam
        user['Surname'] = surnam
        user['StreetAddress'] = adres
        user['ZipCode'] = zipcode
        user['City'] = city
        user['EmailAddress'] = email
        user['Username'] = usernam
        user['TelephoneNumber'] = telephon

        self.customers.append(user)

        self.UpdateCSV()

#blueprint for a librarian
class Librarian:

    def __init__(self, name, surnam, usernam, gender, email, passwd):
        self.Name = name
        self.SurName = surnam
        self.UserName = usernam
        self.Gender = gender
        self.Email = email
        self.Password = passwd

    def checkPass(self, passwd):
        return set(self.Password) == set(passwd)

    def getName(self):
        return self.Name + ' ' + self.SurName

#this class will do the reading and writing for to the librarians json
class Librarians:

    librarians = []

    #load the librarians in
    def __init__(self):
        with open(curdir + '/src/librarians.json', 'r') as File:
            data = json.load(File)
            for i in range(len(data)):
                j = data[i]
                #convert from json to Librarian
                self.librarians.append(Librarian(j['Name'], j['SurName'], j['UserName'], j['Gender'], j['Email'], j['Password']))

#update the json
    def updateLibrarians(self):
    #sort the data in json format
        data = []
        for i in self.librarians:
            data.append(
                {
                    'Name': i.Name,
                    'SurName': i.SurName,
                    'UserName': i.UserName,
                    'Gender': i.Gender,
                    'Email': i.Email,
                    'Password': i.Password
                }
            )

        #store the data
        with open(curdir + '/src/librarians.json', 'w') as File:
            #dump the data to the file in a formatted fashion || pretty neat
            json.dump(data, File, indent=4, sort_keys=True)


#add a new librarian to the system
    def addLibrarian(self, name, surnam, username, gender, email, passwd):
        #data new librarian
        self.librarians.append(Librarian(name, surnam, username, gender, email, passwd))
        #update the json
        self.updateLibrarians()
    
#remove the librarian || yeet him/her away
    def removeLibrarian(self, index):
        #do the delete
        self.librarians.remove(index)
        #update the json
        self.updateLibrarians()

#check if the user exits and get the account to log in
    def getAccount(self, usern, passwd):
        for i in self.librarians:
            if i.UserName == usern:
                if i.Password == passwd:
                    return i
        return None