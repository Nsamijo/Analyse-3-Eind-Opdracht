import json
with open("j.json","r") as jsonread:
    data = json.load(jsonread)

data["sjaak"] = "kees"

with open("j.json","w") as jsonwrite:
    json.dump(data, jsonwrite)