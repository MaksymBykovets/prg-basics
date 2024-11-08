from collections import Counter

number = str(input("Enter number : "))

def func(number): 
    digit_counter = Counter(number)
    
    total_repeats = sum(count for count in digit_counter.values() if count > 1)   
    return total_repeats
print(func(number))