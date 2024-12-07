def second_largest(arr) : 
    first_max = max(arr)
    arr.remove(first_max)
    second_largest = max(arr)
    return  second_largest
    
def diff(arr) : 
    bigger = max(arr)
    smaller = min(arr)
    result = bigger - smaller
    return result

def median(arr) : 
    if len(arr) % 2 != 0 :
        index = len(arr) / 2
        index = index.__round__(0) 
        index = int(index)
        output = arr[index]
    else : 
        index = len(arr) / 2 
        index.__round__(0)
        index = int(index)
        output = arr[(index-1) : (index+1)]
    return output

def arra(arr) : 
    new_arr = []
    new_arr.append(min(arr))
    new_arr.append(max(arr))
    return new_arr

def separ(arr) :
    n = 0
    for i in arr : 
        n += 1 
    output = ""
    i = 1
    for item in arr : 
        if i < n :
            output += str(item) + "-"
            i += 1 
        elif i == n : 
            output += str(item)

        
    return output

def seque(arr) : 
    n = 0
    for i in arr : 
        n += 1 
    output = ""
    i = 1
    for item in arr : 
        if i < n :
            output += str(item) + ","
            i += 1 
        elif i == n : 
            output += str(item)

        
    return output


arrrara = [7,3,6,8,5,2]
print("Nubmers : ",seque(arrrara))
print("Second largest number : ", second_largest(arrrara))
print("Median : ", median(arrrara))
print("Smallest and largest number : ", arra(arrrara))
print("Numbers as a string : ", separ(arrrara))