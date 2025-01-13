grades = [3.0,5.0,2.0,3.5,4.0,4.0,3.5,2.0,4.0,2,0]

without_2 = list(filter(lambda e : e > 2.0, grades))

mean = lambda list : sum(list) / len(list)

print(f"Arithmetic mean for grades <> 2.0 is ", mean(without_2).__round__(2))
