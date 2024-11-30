arr = [34,7,19,4,21,8]
count = 0 
lenght = len(arr)
while lenght != 0 : 
    for item in arr : 
        if item % 2 != 0 : 
            count += 1 
        lenght -= 1
    
print(count)

