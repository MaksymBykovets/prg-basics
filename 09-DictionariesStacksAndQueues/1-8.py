price_list = {
   'T-shirt': 19.99,
   'Jeans': 49.99,
   'Jacket': 89.99,
   'Sneakers': 59.99,
   'Hat': 15.99
}
print("Prices before the discount : ")
total_old = 0 
for item, price in price_list.items() : 
    print(f"{item} : {price}")
    total_old += price
print(f"Total value of the products before the discount : {total_old.__round__(2)}") 

for item, price in price_list.items() : 
    price = price * 0.9
    new = {item: price.__round__(2)}
    price_list.update(new)

print("Prices after the discount : ")
total_new = 0 
for item, price in price_list.items() : 
    print(f"{item} : {price}")
    total_new += price
print(f"Total value of the products after the discount : {total_new.__round__(2)}") 