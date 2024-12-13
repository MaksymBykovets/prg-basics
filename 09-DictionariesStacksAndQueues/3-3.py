number = int(input("Enter natural number : "))
stack = []
while number > 0 : 
    remainder = number % 2 
    stack.append(remainder)
    number //= 2

output = "" 
for item in range(len(stack)) : 
    output += str(stack.pop())

print("Binary number : ", output)