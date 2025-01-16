def f(word) : 
    wawe = []
    for i in range(len(word)) : 
        one_item = [word[:i].lower() + word[i].upper() + word[(i+1):].lower()]
        wawe.append(one_item)
    output = ""
    for item in wawe : 
        output += item[0] + "-"
    output = output[:-1]
    return output
        
            
    

print(f("hello"))
