## 
# The price of the product on the price tag is given before and after the discount is applied.
# Write a program that allows you to enter the product price and discount.
# Print the product price, discount, discounted product price, and the 
# difference between the product price before and after the discount.
# Print all prices with two decimal places.


product_price = input('Enter price: ' )
discount = input('Enter discount %: ' )
product_price = float(product_price)
discount = float(discount)
product_price_discounted = product_price - (product_price * (discount / 100))
difference = product_price - product_price_discounted
product_price_rounded = round(product_price, 2)
product_price_discounted_rounded = round(product_price_discounted, 2)
difference_rounded = round(difference, 2)
print(f"Price with discount: {product_price_discounted_rounded}")
print(f"Reduction: {difference_rounded}")