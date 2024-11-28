arr = [
    [0,0,0],
    [0,0,0],
    [0,0,0]
]
number_row = 0
number_column = 0
for row in arr : 
    arr[0+number_row][0+number_column] = 1
    number_column += 1
    number_row += 1
    print(row)
