def occurs(number, array) : 
    boolean = False
    for item in array : 
        if int(number) == item : 
            boolean = True
            return boolean
        else : 
            boolean = False
    return boolean

arar = [15, 38, 7, 23, 14]
entered_number = input("Number : ")
output = ""
for item in arar : 
    output += str(item) + " "

print("Array : ",output)
if occurs(entered_number, arar) == True : 
    print(f"Result : number {entered_number} appers in the array" )
else : 
    print(f"Result : number {entered_number} don't apper in the array" )