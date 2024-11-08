numder = int(input("Enter number : "))
if numder < 1 : 
    print ("Incorrect input!")

def func(n) : 
    output = ""
    for i in range(1, n+1) :
      i = str(i)
      output += i
    return output

print(func(numder))