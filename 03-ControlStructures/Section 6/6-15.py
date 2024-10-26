##
# Program that checks whether the EAN-13 number entered from the 
# keyboard consists of exactly 13 characters (digits)
##

ean_number = (input('Enter EAN-13 article number: '))

if len(ean_number) == 13 and ean_number.isdigit():
    print("Article number is correct")
else: 
    print("Invalid code")

if ean_number[0:3] == "590":
    print("Article manufactured in Poland")

else:
    print("Invalid EAN-13")