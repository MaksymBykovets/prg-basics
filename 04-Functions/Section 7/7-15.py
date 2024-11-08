number = int(input("Enter number : "))
def func(n):
    if n == 2 : 
        value = 1
        return value
    first_value = 0 
    second_value = 1 
    value = 0
    if n >= 2 :
        for i in range(n-2): 
            value = first_value + second_value
            first_value = second_value
            second_value = value
    return value
print(func(number))
            