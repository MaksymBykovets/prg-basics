number = (input("Enter number : "))
boolean = (input("Enter parameter (y/n):"))
if boolean == "n":
    boolean = False
elif boolean == "y":
    boolean = True
    
def f(number, boolean): 
    summa = 0
    if boolean == True: 
        for char in number:
            char = int(char)
            if char % 2 == 0: 
                summa += char
    elif boolean == False: 
        for char in number:
            char = int(char)    
            if char % 2 != 0: 
                summa += char
    return summa

if boolean == True:
    print("Sum of even digits is ", f(number, boolean))
elif boolean == False:
    print("Sum of odd digits is ", f(number, boolean))