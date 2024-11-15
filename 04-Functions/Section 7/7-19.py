def func(n) : 
    def is_prime(num) :
        if n < 2 :
            return False
        for i in range(2, (num - 1)): 
            if num % i == 0  : 
                return False 
        return True
    prime_count = 0
    current_numb = 2

    while True : 
        if is_prime(current_numb) :
            prime_count += 1 
            if prime_count == n : 
                return current_numb 
        current_numb += 1 
        
print(func(5))