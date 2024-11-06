import in_range

number = int(input("Enter number : "))

boolean = in_range.chack(number)

if boolean == True:
    boolean = "yes"
elif boolean == False:
    boolean = "no"
print(f"Number {number} in the range <2,15>: {boolean}")