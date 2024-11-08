digit1 = int(input("Enter first number : "))
digit2 = int(input("Enter second number : "))
oper = input("Enter operator : ")

def func(number1,number2,operator):
    if operator == "+":
        output = number1 + number2
    elif operator == "-" :
        output = number1 - number2
    elif operator == "*" :
        output = number1 * number2
    elif operator == "%" : 
        output = number1 % number2
    elif operator == "**" :
        output = number1 ** number2
    return output

print(func(digit1, digit2, oper))