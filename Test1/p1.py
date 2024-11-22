def f(tree_circumference) : 
    diametr = tree_circumference / 3.14
    if diametr >= 50: 
        return True
    return False

if __name__ == "__main__" : 
    print(f(100))
