###
# A program that reads temperature in degrees Celsius from the keyboard.
# Use comments to briefly describe the program's algorithm.
#
print("Welcome to temperature converter!")
    
# Declare variable temperature_celsius
temperature_celsius = float(input('Enter temperature in degrees Celsius : '))
temperature_celsius = round(temperature_celsius, 2 )

# Convert temperature in degrees Celsius to the temperature in Kelvin and Fahrenheit.
temperature_kelvin = temperature_celsius + 273.15 
temperature_celsius_x2 = temperature_celsius * 2
temperature_fahrenheit = temperature_celsius_x2 - (temperature_celsius_x2 * 0.1) + 32 

# Print results 
print(f"temperature of {temperature_celsius} degrees Celsius will be converted into Kelvins as {temperature_kelvin}K")
print(f"temperature of {temperature_celsius} degrees Celsius will be converted into Fahrenheit as {temperature_fahrenheit}°F")
