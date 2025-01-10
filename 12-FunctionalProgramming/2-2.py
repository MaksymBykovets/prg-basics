names = [
   'James',
   'Emily',
   'William',
   'Olivia',
   'Benjamin',
   'Sophia',
   'Henry']
sorted_names = lambda names : sorted(names, key=len)
new_list = sorted_names(names)

for item in new_list : 
    print(item)