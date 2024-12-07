def identity_matrix(n) : 
    number = 0
    arr = []
    for i in range(n) : 
        add = [0 for j in range(n)]
        add[number] = 1
        arr.append(add)
        number += 1 
    
    
    return arr

for row in identity_matrix(8) : 
    print(" ".join(map(str, row)))