arr =[1,2,3,4,5]

arr[0] -= arr[0]
print(arr)

arr[-1] += 4
print(arr)

mid = len(arr) // 2 
arr[mid] *= 2
print(arr)
