##
# Write a program that reads an amount from the keyboard.
# Then, it calculates and prints both the amount and its VAT. 
# Apply formatting with two decimal places.

amount = input('Insert amount: ' )
amount = float(amount)
amount_rounded = round(amount, 2)
vat = amount_rounded * (23 / 100)
vat_rounded = round(vat, 2)
print(f'Amount : {amount_rounded}' )
print(f'VAT 23% : {vat_rounded}' )