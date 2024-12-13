def f(arr) :
    count = {}
    for num in arr : 
        count[num] = count.get(num, 0) + 1 
    for num, frequency in count.items() : 
        if frequency == 1 : 
                return num
            
print(f([7,7,7,7,7,5,7,7]))