def f(n) : 
    
    if n < 0 :
        return False
    
    if n == 0 :
        res = "" 
        return res
    
    res = ""
    for digit in range(1, (n+1)): 
        digit = str(digit)
        res += digit
        
        
    return res
    
    
    
if __name__ == "__main__" : 
    print(f(11))

