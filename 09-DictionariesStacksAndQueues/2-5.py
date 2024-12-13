import json
with open("reservations.json", 'r', encoding='utf-8') as file : 
    data = json.load(file)

def number_rooms(data) : 
    reservations = data["reservations"]
    numbers = ""
    for item in reservations : 
        numbers += str(item["room_number"]) + " "
    return numbers

def paid(data) : 
    reservations = data["reservations"]
    numbers = 0
    for item in reservations : 
        if item["paid"] == True : 
            numbers += 1
    return numbers

def unpaid(data) : 
    reservations = data["reservations"]
    numbers = 0
    for item in reservations : 
        if item["paid"] != True : 
            numbers += 1
    return numbers

def total_paid(data) : 
    reservations = data["reservations"]
    numbers = 0
    for item in reservations : 
        if item["paid"] == True : 
            numbers += (item["price_per_night"] * item["nights"])
    return numbers

def total_unpaid(data) : 
    reservations = data["reservations"]
    numbers = 0
    for item in reservations : 
        if item["paid"] != True : 
            numbers += (item["price_per_night"] * item["nights"])
    return numbers


print(number_rooms(data))
print(paid(data))
print(unpaid(data))
print(total_paid(data))
print(total_unpaid(data))
