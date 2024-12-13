import json

data = {
    "type": "book",
    "name": "Witcher",
    "author": "Andrzej Sapkowski",
    "pages": 382,
    "genre": "fantasy",
    "year": 1992

}

file_name = "favourite.json"

with open(file_name, "w") as file : 
    json.dump(data, file, indent=4)
    