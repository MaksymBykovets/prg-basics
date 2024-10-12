##
# Write a program that prints the number of dice rolled and the value True if the number rolled is 1 or 6. 
##

import random
number = random.randint(1,6)
correct = number == 1 or number == 6 
print(f"Dice rolled : {number}")
print(f'Special number (1 or 6) : {correct}')