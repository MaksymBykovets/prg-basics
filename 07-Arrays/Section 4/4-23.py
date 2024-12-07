arr1 = [1,2,3,4,5,6,7]
arr2 = [1,2,3,4,5,6,7,8,9,10]
def appear(arr1, arr2) : 
    value = False
    for item in arr1 : 
        if item in arr2 : 
            value = True
        elif item not in arr2 : 
            return False
    return value

print(appear(arr1, arr2))
