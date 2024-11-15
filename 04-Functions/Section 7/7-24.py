def func(x, y) : 
    sum = 0
    for digit in range(x, (y+1)) : 
        if digit % 2 == 0 and digit % 3 == 0 and digit % 4 != 0:
            sum += digit
    return sum

print(func(1,20)) 
