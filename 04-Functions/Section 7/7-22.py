def func(password) : 
    if len(password) < 6 : 
        return False 
    seen_words = set()
    for char in password : 
        if char in seen_words : 
            return False 
        else : 
            seen_words.add(char)
    return True

print(func("A2water3"))