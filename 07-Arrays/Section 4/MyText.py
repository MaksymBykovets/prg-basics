text = "An apple a day keeps the doctor away"

def words(variable) : 
    arr = variable.split(" ")
    number = len(arr)
    return number

def ordered(variable) : 

    arr = sorted(variable.split(" "), key=len, reverse=True)
    n = 0
    for i in arr : 
        n += 1 
    output = ""
    i = 1
    for item in arr : 
        if i < n :
            output += str(item) + ", "
            i += 1 
        elif i == n : 
            output += str(item)
    return output

def alfa(variable) : 
    arr = sorted(variable.split(" "))
    n = 0
    for i in arr : 
        n += 1 
    output = ""
    i = 1
    for item in arr : 
        if i < n :
            output += str(item) + ", "
            i += 1 
        elif i == n : 
            output += str(item)
    return output

    return output


print("Text : ",text)
print("Number of words : ", words(text))
print("Words from the longest : ", ordered(text))
print("Words ordered alphabetically : ", alfa(text))


