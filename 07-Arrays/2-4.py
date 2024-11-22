###
# Prints some array elements
#
arr = [2, 3, 7, 5, 4]

print(arr)
print('Number of elements', len(arr))
print('First value', arr[0])
print('Second value', arr[1])
print("Last value", arr[4])
print("last but one value", len(arr)/2)
print("sum of the first and last value", (arr[0]+arr[-1]))

for item in arr :
    print(item)

for i in range(len(arr)): 
    arr[1] = arr[1] + 1
    