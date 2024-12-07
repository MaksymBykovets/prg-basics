arr = [1,2,3,4,5,6,7,8,9,10]
output = ""
for item in arr : 
    if item % 2 == 0 : 
        output += str(item) + " "
for item in arr : 
    if item % 2 != 0 : 
        output += str(item) + " "
print(output)