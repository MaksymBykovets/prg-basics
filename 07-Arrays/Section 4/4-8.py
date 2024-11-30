arr = [15, 8, 31, 47, 2, 19]
length = len(arr)
count = 0 
summa = 0

while length != 0 :
    digit = arr[count] 
    summa += digit
    count += 1 
    length -= 1 
    
value = summa / count
print("Array : ", arr)
print("AVG : ", value.__round__(2))
