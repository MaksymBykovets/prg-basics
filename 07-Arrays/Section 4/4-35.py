arr = [
    [1,2,3,4,5],
    [6,7,8,9,10],
    [11,12,13,14,15]
]
n_row = 0
for row in arr : 
    arr[n_row][0], arr[n_row][-1] = arr[n_row][-1], arr[n_row][0]
    n_row += 1 
for row in arr : 
    print(row)