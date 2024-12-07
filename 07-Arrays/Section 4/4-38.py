def convert(arr) :
    new_arr = []
    for row in arr : 
        for i in row : 
            new_arr.append(i)
    return new_arr

arr = [
    [5, 0, 3, 7, 5],
    [9, 0, 9, 1, 2]
]
output = ""
for item in convert(arr) : 
    output += str(item) + " "
print(output)
    