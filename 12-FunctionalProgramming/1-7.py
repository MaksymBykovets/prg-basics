num = int(input("Enter number : "))

is_even = lambda number : number % 2 == 0 

result = is_even(num)
print(f"For number {num} it is {result}")