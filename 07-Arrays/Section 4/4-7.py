arr = [15, 8, 31, 47, 2, 19]
count = 0 
summa = 0
for item in arr : 
    count += 1 
    summa += item
value = summa / count
print(value.__round__(2))
