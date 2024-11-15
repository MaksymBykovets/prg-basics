def func(name) : 
    acronym = ""
    words = name.split()
    for char in words : 
        acronym += char[0].upper()
    return acronym

print(func("Internet of Things"))