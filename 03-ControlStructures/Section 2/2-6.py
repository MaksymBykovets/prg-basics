##
# Write a program that checks what number was entered from the keyboard and prints 
# one of the messages below. Then run the program and check the following numbers:

number = int(input("Enter number : "))

if number == 0 : 
    print("Number is 0")

elif number > 0 :
    print(f"Number {number} is positive")

elif number < 0 :
    print(f"Number {number} is negative")