km_h = lambda ms : (ms * 3.6)

ms = int(input("Enter speed in m/s : "))
result = int(km_h(ms))
print(f"{ms} m/s = {result} km/h")