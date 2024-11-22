def f(student1, student2) : 
    import math
    student1 = student1.split(",")
    student2 = student2.split(",")
    n1 = 0
    sum1 = 0
    n2 = 0
    sum2 = 0
    for grade in student1 : 
        n1 += 1
        sum1 += int(grade)
    average_st1 = sum1 / n1
    
    for grade in student2 : 
        n2 += 1
        sum2 += int(grade)
    average_st2 = sum2 / n2
    
    if average_st1 > average_st2 : 
        return 1 
    elif average_st1 < average_st2 : 
        return 2
    elif average_st2 == average_st1 : 
        return 0 
    
    return 

if __name__ == "__main__" : 
    print(f("4,4,1,4", "4,4,4,4"))


