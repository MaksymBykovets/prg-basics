goods = {
'Laptop': 15,
'Desktop PC': 10,
'Monitor': 25,
'Keyboard': 50,
'Mouse': 60,
'External Hard Drive': 30,
'Printer': 12,
'Router': 20,
'USB Flash Drive': 100,
'Graphics Card': 8
}

value = 0 
for item, number in goods.items() : 
    print(f"{item} : {number}")
    value += number

print(f"Total number of products in the store : {value}")
