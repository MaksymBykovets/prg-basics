car_fuel_consumption = [7.2, 6.8, 7.5, 7.0, 7.1, 6.9, 7.3]
bank_transactions = [-150, -20, 300, -45, -60, 500, -120]
###
# Bubble sort 
#
def bubble_sort(arr):
    indexing_length = len(arr)
    sorted = False

    while not sorted : 
        sorted = True
        for i in range(0, indexing_length) : 
            if arr(i) > arr(i + 1) : 
                sorted = False
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr








car_fuel_consumption = bubble_sort(car_fuel_consumption)
print(car_fuel_consumption)
sorted_car_fuel_consumption = bubble_sort(car_fuel_consumption) 
print(sorted_car_fuel_consumption)

bank_transactions = ...
...
...
...