record = [48,47,54,50,42,68,39,46]

speeding = list(filter(lambda e : e>50 , record))

output1 = ""
for item in record : 
    output1 += str(item) + ", "
output1 = output1[:-2] 


output2 = ""
for item in speeding : 
    output2 += str(item) + ", "
output2 = output2[:-2]

print(f"Recorded values : ",output1)
print(f"Speed too high : ", output2)