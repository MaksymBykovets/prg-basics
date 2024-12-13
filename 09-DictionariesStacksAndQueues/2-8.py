import json
name = str(input("Enter the name of product : "))
price = float(input("Enter the price of product : "))
paid = input("Enter if it was paid (yes/no): ")
if paid == "yes" : 
    paid = True
elif paid == "no" : 
    paid = False

data = {
    "name": name,
    "price": price,
    "paid": paid
}

file_mame = "product.json"

with open(file_mame, "w") as file : 
    json.dump(data, file, indent=4)