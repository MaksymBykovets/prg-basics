###
# Program for testing built-in functions
#
max_number = max(7,5,6,3,8,2)
print('Max number of 7,5,6,3,8,2 is', max_number)

min_number = min(4,7,2,3,9,8)
print('Min number of 4,7,2,3,9,8 is', min_number)

str_length = len("computer science")
print('The number of characters in "computer science" is', str_length)

read_key = input("Enter simething from the keyboard : ")
print("letters from the keyboard :", read_key)

string_number = "20303"
number = int(string_number)
print("The number representing the string is:", number)

decimal = 304
binary = bin(decimal)
print("representing decimal number 304 : ", binary)

hexadecimal = hex(decimal)
print("hexadecimal string representing decimal number 304 : ", hexadecimal)

sign = "€"
print("integer representing the Unicode code of the € sign", ord(sign))


print("absolute value of -17 is ", abs(-17))