import json, os
import UserClasses, bookclasses
curdir = os.path.dirname(os.path.realpath(__file__))
catalog = bookclasses.Catalog("")
customers = UserClasses.Customers() 
class Loan:
    def __init__(self,b,u,d):
        self.book = b
        self.user = u
        self.date = d


class LoanAdministration:
    def __init__(self):
        self.loans = []
        with open(curdir + "/src/loans.json","r") as loanread:
            data = json.load(loanread)
        for d in data:
            user = None
            for u in customers.customers:
                if d["userid"] == u["id"]:
                    user = u
            self.loans.append(Loan(catalog.getBookbyId(d["bookid"]),user,d["date"]))
    
    def addloan(self,b,u,d):
        self.loans.append(Loan(b,u,d))
        self.parse()
    
    def parse(self):
        loandump = [{
            "BookId" : l.book.id,
            "User" : l.user["Number"],
            "Date" : l.date
        } for l in self.loans]
        
        with open(curdir + "/src/loans.json","w") as loanwrite:
            json.dump(loandump, loanwrite)