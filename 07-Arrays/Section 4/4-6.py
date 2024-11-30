arr = [-15, 8, -31, 47, -2, 19]

def maximum(arr) :
    
    digit = arr[0]
    for item in arr : 
        if item > digit : 
            digit = item
        else : 
            digit = digit
    return digit

def minimum(arr) : 
    digit = arr[0]
    for item in arr : 
        if item < digit : 
            digit = item
        else : 
            digit = digit
    return digit

print("Maximum : ",maximum(arr))
print("Minimum : ",minimum(arr))
            
            