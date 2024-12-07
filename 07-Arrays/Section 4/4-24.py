import random
def rand_elem(array) : 
    output_numb = random.randint(0,(len(array)-1))
    output = array[output_numb]
    return output

arr = [1,2,3,4,5,6,7,8,9,10]
print(rand_elem(arr))