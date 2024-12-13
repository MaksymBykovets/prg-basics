import re  # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r') as file:
    email = file.read()

# regular expression pattern for amounts in euros (e.g., "€102", "€30")
pattern = '[€\d+]'

# extract all amounts from the email
amounts = re.findall(pattern, email)

# remove the euro symbol and convert amounts to integers
total = 0 
for amount in amounts : 
    total += int(amount[1:])




# print the result
print(f"Total value of money spent: €{total}")
