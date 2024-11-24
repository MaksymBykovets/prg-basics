# Prices of 10 products in the computer store (in currency units)
product_prices = [2999.99, 149.99, 499.99, 89.99, 1199.99, 349.99, 189.99, 99.99, 249.99, 999.99]

# Number of units available for each product
product_quantities = [5, 20, 10, 15, 7, 12, 25, 18, 9, 4]

number_price = 0 
number_quant = 0 
summa = 0
for prod in product_prices : 
    summa += product_prices[number_price] * product_quantities[number_quant]
    number_quant += 1
    number_price += 1 

print(summa.__round__(2))