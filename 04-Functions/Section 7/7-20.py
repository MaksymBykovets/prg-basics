def func(number1, number2, number3) : 
    largest = max(number1, number2, number3)
    smallest = min(number1, number2, number3)
    diff = int(largest) - int(smallest)
    return diff 

print(func(7,4,9))