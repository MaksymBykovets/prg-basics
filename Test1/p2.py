def f(x, y) : 
    if x == 0 or y == 0:
        return False
    if x > 0 and y > 0 : 
        return 1 
    elif x < 0 and y > 0 : 
        return 2
    elif x < 0 and y < 0 : 
        return 3
    elif x > 0 and y < 0 : 
        return 4
    
if __name__ == "__main__" : 
    print(f(-2,-2))