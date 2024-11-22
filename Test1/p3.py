def f(product_code) : 
    if len(product_code) != 4:
        return False
    
    
    sum = 0
    product_code = product_code
    for char in str(product_code[0:3]) : 
        sum += int(char)
    
    remainder = float(sum % 7)
    fourth_digit = remainder.__round__(1) 
    fourth_digit = int(fourth_digit)
    if int(product_code[3]) != fourth_digit :
        return False
    return True
   




if __name__ == "__main__" : 
    print(f("1028"))


    