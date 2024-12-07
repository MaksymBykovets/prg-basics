def compare(array1, array2) : 
    def values(arr1, arr2) : 
        index = 0
        for item in arr1 : 
            if arr1[index] == arr2[index] :
                index += 1  
                boolean = True
            else : 
                return False
        return boolean
            


    if len(array1) == len(array2) and values(array1, array2) == True : 
        value = True
    else : 
        value = False

    return value


arar1 = ["water","book","sky"]
arar2 = ["water","book","sky"]

print("Array1 : ", arar1)
print("Array2 : ", arar2)
if compare(arar1, arar2) == True : 
    print("Comparison: arrays are the same")
elif compare(arar1, arar2) == False :
    print("Comparison: arrays are not the same")
    