def func(number):
    num_str = str(number)
    repeated_sum = 0 
    seen_digits = set()
    for digit in num_str :
        if digit in seen_digits : 
            repeated_sum += int(digit)
        else : 
            if num_str.count(digit) > 1 : 
                repeated_sum += int(digit)
                seen_digits.add(digit)
    return repeated_sum 

print(func("33336"))