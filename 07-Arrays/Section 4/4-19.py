my_tuple = (50,20,40,50,30,50)
output = ""
for item in my_tuple : 
    output += str(item) + ","

print("Tuple : ", output)

value = input("Enter value : ")
result = my_tuple.count(int(value))
print("Number of occurences : ", result)
