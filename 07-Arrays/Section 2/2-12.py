categories = ["Food", "Transport", "Rent","Entertainment"]
expenses = [500, 150, 1000, 200]
most_exp_index = expenses.index(max(expenses)) 
most_exp_cat = categories[most_exp_index]

print((most_exp_index + 1), most_exp_cat)

