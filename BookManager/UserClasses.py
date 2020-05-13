import json,os
curdir = os.path.dirname(os.path.realpath(__file__))

class Person:
    def __init__(self,name,birthday,gender):
        self.Name = name
        self.Birthday = birthday
        self.Gender = gender


class Customer(Person):
    def __init__(self,name,birthday,gender,username,password,email):
        super.__init__(name,birthday,gender)
        self.Username = username
        self.Password = password
        self.Email = email

class Librarian(Person):
    def __init__(self,name,birthday,gender,username,password,email):
        super.__init__(name,birthday,gender)
        self.Username = username
        self.Password = password
        self.Email = email

class UserAdministration:
    def __init__(self):
        self.users = []
        with open(curdir + "/src/customers.json","r") as custread:
            data = json.load(custread)
            for c in data:
                self.users.append(Customer(*[c[f] for f in c]))
        

        self.librarians = []
        with open(curdir + "/src/librarians.json","r") as libread:
            data = json.load(libread)
            for l in data:
                self.librarians.append(Librarian(*[l[f] for f in l]))
    
    def ParseContents(self):
        cusdumper = []
        for c in self.users:
            cusdumper.append({
                "Name" : c.Name,
                "Birthday" : c.Birthday,
                "Gender" : c.Gender,
                "Username" : c.Username,
                "Password" : c.Password,
                "Email" : c.Email
            })
        with open(curdir + "/src/customers.json","w") as cuswrite:
            json.dump(cusdumper,cuswrite)

        libdumper = []
        for l in self.librarians:
            libdumper.append({
                "Name" : l.Name,
                "Birthday" : l.Birthday,
                "Gender" : l.Gender,
                "Username" : l.Username,
                "Password" : l.Password,
                "Email" : l.Email
            })
        with open(curdir + "/src/librarians.json","w") as libwrite:
            json.dump(libdumper,libwrite)
    def AddCustomer(self,name,birthday,gender,username,password,email):
        self.users.append(Customer(name,birthday,gender,username,password,email))
        self.ParseContents()
    def AddLibrarian(self,name,birthday,gender,username,password,email):
        self.librarians.append(Librarian(name,birthday,gender,username,password,email))
        self.ParseContents()
