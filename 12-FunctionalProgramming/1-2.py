# takes two numbers from keyboard
n1 = int(input("Enter first digit : "))
n2 = int(input("Enter second digit : "))

# define an anonymous function
mean = lambda x,y: (x+y)//2


# calculates arightmtic mean and print result
result = mean(n1,n2)
print(f"The arithmetic mean of {n1} and {n2} is {result}")