###
# Prints employees employed in a specified position.
#

# Employee List
file_name = 'it_company.csv'

# Position
job_title = 'Software Engineer'

with open(file_name) as file:
    number = 0
    for line in file :
        if job_title in line :
            print(number, job_title)
            number += 1
        elif job_title not in line : 
            number += 1 
            continue
