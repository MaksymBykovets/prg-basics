def func(product_code) : 
    if len(product_code) != 4: 
        return False
    fourth_digit = (int(product_code[0]) + int(product_code[1]) + int(product_code[2])) % 7 
    
    fourth_digit = fourth_digit.__round__(1)
    if product_code[3] == str(fourth_digit):
        return True
    else : 
        return False
    
print(func("1114"))


