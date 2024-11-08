value = input("Enter signals from detector : ")

def func(detector) : 
    count = 0
    max_count = 0 
    for sign in detector : 
        if sign == "+" :  
            count += 1
        elif sign == "-" : 
            count -= 1

        max_count = max(max_count, count)

    if max_count >= 3 : 
        return True
    return False

print(func(value))