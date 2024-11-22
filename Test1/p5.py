def f(a, b) :
    sum = 0
    for char in range(a, (b+1)) : 
        if char % 3 == 0 :
            sum += char
    return sum



if __name__ == "__main__" : 
    print(f(2, 10))
