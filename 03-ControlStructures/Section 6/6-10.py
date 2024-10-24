##
# Write a program that calculates a dog's age in dog's years. 
# For the first two years, a dog's life is equal to 10.5 human years. 
# After that, each dog year is equal to 4 human years.
##

dog_age = int(input("Enter the dog's age in human years: "))
if dog_age < 0:
    print("Age cannot be negative.")
else:
    if dog_age <= 2:
        age = dog_age * 10.5
    else:
        age = 2 * 10.5 + (dog_age - 2) * 4
    print(f"The dog's age in dog's years is {age} year(s).")