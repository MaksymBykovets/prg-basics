distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

avg_speed = lambda distance, hours, minutes : distance / (hours + (minutes / 60))

result = round(avg_speed(distance,hours,minutes), 1)

print(f"Average speed: {result}")