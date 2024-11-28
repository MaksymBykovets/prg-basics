# Weekly expenses for different categories
# [Food, Transport, Utilities]
monthly_expenses = [
   [200, 50, 100],  # Week 1
   [180, 60, 110],  # Week 2
   [220, 55, 105],  # Week 3
   [210, 65, 95]    # Week 4
]

# Calculates expenses
# Use loop statements
# Calculating of total food expences
total_expences_food = 0 
n_row_food = 0 
for row in monthly_expenses : 
    total_expences_food += monthly_expenses[n_row_food][0]
    n_row_food += 1

# Calculatin of total transport expences
total_expences_transport = 0 
n_row_transport = 0 
for row in monthly_expenses : 
    total_expences_transport += monthly_expenses[n_row_transport][1]
    n_row_transport += 1 

# Calculating of total utilities expences
total_expences_utilities = 0 
n_row_utilities = 0 
for row in monthly_expenses : 
    total_expences_utilities += monthly_expenses[n_row_utilities][2]
    n_row_utilities += 1

# Calculating of expences every week 
week1_exp = 0 
n_column1 = 0 
for item in row : 
    week1_exp += monthly_expenses[0][n_column1]
    n_column1 += 1

week2_exp = 0 
n_column2 = 0 
for item in row : 
    week2_exp += monthly_expenses[1][n_column2]
    n_column2 += 1

week3_exp = 0 
n_column3 = 0 
for item in row : 
    week3_exp += monthly_expenses[2][n_column3]
    n_column3 += 1

week4_exp = 0 
n_column4 = 0 
for item in row : 
    week4_exp += monthly_expenses[3][n_column4]
    n_column4 += 1

total_general = week1_exp + week2_exp + week3_exp + week4_exp





# Print expenses
print('MONTHLY EXPENSES')
print('----------------')
print('Food:',total_expences_food)
print('Transport:',total_expences_transport)
print('Utilities:',total_expences_utilities)
print('Week 1:',week1_exp)
print('Week 2:',week2_exp)
print('Week 3:',week3_exp)
print('Week 4:',week4_exp)
print('---------------')
print('TOTAL:',total_general)