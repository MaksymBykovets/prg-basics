## 
# A computer program analyses the price of a product in an online store. 
# If the product price decreases by at least 10%, the program prints a recommendation
##

current_price = float(input("Enter current price : ") )
previous_price = float(input("Enter previous price : ") )
diff = (previous_price - current_price) / (previous_price / 100)
print(f"Current product price : {current_price}") 
print(f"Previous product price : {previous_price}")
if diff >= 10 : 
    print("Buy the product!!")
    print(f"Product price reduced by {round(diff, 2)}%")