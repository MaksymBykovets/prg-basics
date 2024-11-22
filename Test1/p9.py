def f(size1, size2) : 
    if size1 == "S":
        valuue1 = 1
    elif size1 == "M":
        valuue1 = 2
    elif size1 == "L":
        valuue1 = 3

    if size2 == "S":
        valuue2 = 1
    elif size2 == "M":
        valuue2 = 2
    elif size2 == "L":
        valuue2 = 3

    if valuue1 > valuue2 :
        return 1 
    elif valuue1 < valuue2 : 
        return 2
    elif valuue1 == valuue2 : 
        return 0
    

if __name__ == "__main__" : 
    print(f("M", "M"))