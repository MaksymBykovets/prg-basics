arr = ["Genowefa", "Onufry", "Celestyna", "Alojzy", "Pankracy"]
length = 0
name = ""
names = ""
for item in arr : 
    if len(item) > length : 
        length = len(item)
        name = item
    names += item + " "
        
print("Names : ",names )
print("Longest name : ", name)