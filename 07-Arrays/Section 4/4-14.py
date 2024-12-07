arr = [2, 3, 2, 5, 8, 1, 9, 8,]
used_elements = []

freq = {}
for item in arr : 
    if item in freq : 
        freq[item] += 1 
    else : 
        freq[item] = 1 
output = []
for item, count in freq.items() :
    if count == 1 :
        output.append(item)

    

print(output)
    