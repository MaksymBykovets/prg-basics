###
# Reads from file, line by line
#
with open('countries.txt', 'r') as file:
    number = 1
    count = ""
    for line in file:
        count = str(number) + "."
        print(count, line, end="")
        number += 1

        
