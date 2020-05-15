import json, os
import UserClasses, bookclasses
curdir = os.path.dirname(os.path.realpath(__file__))

catalog = bookclasses.Catalog("")
customers = UserClasses.Customers() 

class Loan:
    def __init__(self,b,u,d):
        #bookitem
        self.bookItem = b
        #username
        self.user = u
        #date
        self.date = d


class LoanAdministration:

    def __init__(self):
        self.loans = []
        customers.Load()
        if os.stat(curdir + "/src/loans.json").st_size > 0:
            with open(curdir + "/src/loans.json","r") as loanread:
                data = json.load(loanread)
            for d in data:
                user = None
                for u in customers.customers:
                    if d["Number"] == u["Number"]:
                        user = u
                self.loans.append(Loan(catalog.getBookbyId(d["bookid"]),user,d["date"]))
        else:
            print('\nNo loans in the system')
    
    def addloan(self,b,u,d):
        self.loans.append(Loan(b,u,d))
        self.parse()

    def seeLoans(self, u):
        temps = []
        for x in self.loans:
            if u["Number"] == x.user["Number"]:
                temps.append(x)
        return temps
        
    def parse(self):
        loandump = [{
            "BookId" : l.bookItem.id,
            "User" : l.user["Number"],
            "Date" : l.date
        } for l in self.loans]
        
        with open(curdir + "/src/loans.json","w") as loanwrite:
            json.dump(loandump, loanwrite, indent=4, sort_keys=True)