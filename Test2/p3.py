def f(array2D) : 
    n = len(array2D)
    for item in range(n) : 
        row_sum = sum(array2D[item])
        col_sum = sum(array2D[j][item] for j in range(n))
        if row_sum != col_sum : 
            return False 
    return True 







print(f([[3,7,2],[4,2,5],[5,2,1]]))