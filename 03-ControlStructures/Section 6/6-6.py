##
# Write a program that asks for the number of hours of parking, 
# then calculates and prints the correct fee.
#
# 1-2 hours: 5 PLN
# 3-6 hours: 15 PLN
# Over 6 hours: 20 PLN
##

print("Welcome to Parking Meter")

hours = int(input("Enter the number of parking hours : "))
if hours > 6 :
    print(f"You have to pay 20 PLN for {hours} parking hours")
elif hours >= 3 : 
    print(f"You have to pay 15 PLN for {hours} parking hours")
elif hours >= 1 :
    print(f"You have to pay 5 PLN for {hours} parking hour(s)")
else :
    print('Something goes wrong :(')