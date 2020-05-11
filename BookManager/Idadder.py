import os,json
curdir = os.path.dirname(os.path.realpath(__file__))

with open(curdir + "/src/books.json","r") as bookread:
    data = json.load(bookread)
ID = 0
for book in data:
    book["id"] = ID
    ID += 1

with open(curdir + "/src/books.json","w") as bookwrite:
    json.dump(data,bookwrite)
