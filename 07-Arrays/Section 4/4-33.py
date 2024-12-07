arr = [[-38, 19], 
       [5,40],
       [-7,11],
       [29,16]
    ]
col_index = -1
row_index = -1
smallest = 0
largest = 0
for row in arr : 
    for item in row : 
        if item < smallest : 
            smallest = item
        if item > largest : 
            largest = item
        col_index += 1 
    row_index += 1 

print(col_index, row_index)