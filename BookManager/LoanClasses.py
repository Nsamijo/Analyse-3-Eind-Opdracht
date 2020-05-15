import json, os
import UserClasses, bookclasses
curdir = os.path.dirname(os.path.realpath(__file__))

catalog = bookclasses.Catalog("")
customers = UserClasses.Customers() 

class Loan:
    def __init__(self,b,u,d):
        #bookitem
        self.bookitem = b
        #id || contains the id of the customer
        self.user = u
        #date
        self.date = d


class LoanAdministration:

    def __init__(self):
        self.loans = []
        customers.Load()
        with open(curdir + "/src/loans.json","r") as loanread:
            data = json.load(loanread)
            for d in data:
                
                self.loans.append(Loan(catalog.getBookitembyId(d["bookitem"]),d["user"],d["date"]))

    def addloan(self,b,u,d):
        self.loans.append(Loan(b,u,d))
        self.parse()

    def seeLoans(self, u):
        temps = []
        for x in self.loans:
            if u["Number"] == x.user:
                temps.append(x)
        return temps

    def parse(self):
        loandump = [{
            "bookitem" : l.bookitem.id,
            "user" : l.user,
            "date" : l.date
        } for l in self.loans]
        
        with open(curdir + "/src/loans.json","w") as loanwrite:
            json.dump(loandump, loanwrite, indent=4, sort_keys=True)