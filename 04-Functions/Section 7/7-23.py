def func(expression) : 
    sum = 0 
    terms = expression.replace("-", "+-").split("+")
    for char in terms : 
        sum += int(char)
    return sum

print(func("2+3-4+5-0"))