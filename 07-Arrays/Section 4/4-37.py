def transpose_matrix(m) : 
    return [[row[i] for row in m] for i in range(len(m[0]))]

arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
for row in transpose_matrix(arr) : 
    print(" ".join(map(str, row)))