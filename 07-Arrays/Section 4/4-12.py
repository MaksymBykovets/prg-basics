arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
output = []
for item in arr1 : 
    if item not in arr2 : 
        output.append(item)
print(output)