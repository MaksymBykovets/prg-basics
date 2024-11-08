word = input("Enter word : ")

def func(palindrome) : 
    transformed = ""
    for char in reversed(palindrome) : 
        transformed += char
    
    if palindrome == transformed : 
        return True
    
    return False

print(func(word))