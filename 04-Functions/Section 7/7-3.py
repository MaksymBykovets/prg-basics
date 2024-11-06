import calculations

entering = "You never get a second chance to make a first impression"
letter = input("Enter letter : ")

calculations.calculation(entering, letter)

count = calculations.calculation(entering, letter)
print(entering)
print(f"The number of letter '{letter}': {count}")

