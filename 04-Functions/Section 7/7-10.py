number_1 = int(input("Enter first number : "))
number_2 = int(input("Enter second number : "))
number_3 = int(input("Enter third number : "))

def f(n1, n2, n3) : 
    if n1 < 0 or n2 < 0 or n3 < 0 : 
        boolean = True
    else :
        boolean = False
    return boolean

print("There at least one negative number : ", f(number_1, number_2, number_3))