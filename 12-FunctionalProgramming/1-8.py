name = input("Enter name : ")
surname = input("Enter surname : ")

initials = lambda name, surname : f"{name[0]}{surname[0]}"
result = initials(name, surname)
print(result)