number_x = int(input("Enter number x : "))
number_y = int(input("Enter number y : "))

def f(x,y): 
    summa = 0
    numbers = list(range(x, y + 1))
    for char in numbers :
        char = int(char)
        if char % 2 == 0 and char < 0: 
                summa += 1
    return summa

print(f"Sum of negative even numbers ({number_x},{number_y}) is ", f(number_x, number_y))
        