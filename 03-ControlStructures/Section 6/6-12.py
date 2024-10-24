##
#In one of the online stores, a 25% discount is charged for each product purchased over two. 
# Write a program that calculates the amount to be paid. 
# Read the number of purchased products and the product price from the keyboard.
##

number_of_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))
total_price = number_of_products * product_price
if number_of_products > 2:
    discount = total_price * 0.25
    total_price -= discount
print(f"Amount to pay: {total_price}")