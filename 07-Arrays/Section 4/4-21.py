arr = [2.3,4.2,1.8,4.7,2.5,1.6]
number = float(input("Enter number : "))
n = 0
for item in arr : 
    if item > number : 
        n += 1
print(n)