basic_data = {
   "name":"Barbara",
   "age":21
}

advanced_data = {
   "status":"student",
   "married":False,
   "interest":["reading","swimming"]
}

# Combine the two dictionaries
person = {**basic_data, **advanced_data}

# Print the contents of the 'person' dictionary
for key, value in person.items():
    print(f"{key}: {value}")
