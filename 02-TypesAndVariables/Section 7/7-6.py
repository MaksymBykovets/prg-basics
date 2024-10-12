##
# Write a program that checks whether the vehicle speed entered from the keyboard is correct. 
##

car_speed = int(input("Enter vehicle speed: " ))
speed_limit_ok = car_speed >= 40 and car_speed <= 140 
print(f"Speed is valid: {speed_limit_ok}")