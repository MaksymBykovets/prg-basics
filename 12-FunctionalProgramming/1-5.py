distance = int(input("Enter distance in km: "))
hours = int(input("Enter number of travel hours: "))
minutes = int(input("Enter number of travel minutes: "))

def avg_speed(distance,hours,minutes) : 
    time = hours + (minutes / 60)
    speed = distance / time
    return speed

speed = avg_speed(distance, hours, minutes).__round__(1)
print(f"Average speed: {speed}")