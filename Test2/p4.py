def f(subjects) : 
    maximum_grade = float()
    best_sub = None
    for subject, grades in subjects.items() : 
        avg = sum(grades) / len(grades)
        if avg > maximum_grade : 
            maximum_grade = avg
            best_sub = subject
    return best_sub 

subj = {"Math":[3,4,4], "geo":[5,5,5,4], "comp":[5,4]}

print(f(subj))