speed_metr = int(input("Enter speed in meters per second : "))

def ms_to_kmh(ms) : 
    result = ms * 3.6
    return result

result =int(ms_to_kmh(speed_metr))
print(f"{speed_metr} m/s = {result} km/h")