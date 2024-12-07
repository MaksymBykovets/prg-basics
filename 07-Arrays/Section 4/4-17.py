my_tuple = (10,20,30,40,50)
output = ""
for item in my_tuple : 
    output += str(item) + " "

revee = ""
for item in my_tuple[::-1] : 
    revee += str(item) + " "

print("Tuple : ", output)
print("Reverse order : ",revee)