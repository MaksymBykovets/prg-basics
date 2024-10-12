##
# Write a program that, based on the circumference of the tree entered from the keyboard, 
# calculates and prints the value True if the tree can be cut down, or print the value False otherwise.
##

circumference = float(input("Enter tree circumference in cm: " ))
diameter = circumference / 3.14
cut_ok = diameter >= 50
print(f"A tree may be cut down: {cut_ok}" )

##
# If tree is 160 cm : It may be cut down
# If tree is 90 cm : Don't touch it
# If tree is 260 cm : It may be cut down
# If tree is 120 cm : Don't touch it 