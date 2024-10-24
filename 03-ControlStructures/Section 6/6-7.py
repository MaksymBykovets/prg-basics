##
# Write a program that asks the user for their age and then checks which age group they belong to:
#
# Child: under 13
# Teen: 13 to 19
# Adult: 20 to 64
# Senior: 65 or older
##

age = int(input("Enter your age : "))
if age >= 65 :
    print(f"If you age is {age}, you belong to Senior age group")
elif age >= 20 :
    print(f"If you age is {age}, you belong to Adult age group")
elif age >= 13 :
    print(f"If you age is {age}, you belong to Teen age group")
elif age > 0 :
    print(f"If you age is {age}, you belong to Child age group")
else :
    print("You haven't born yet, lil bro")
