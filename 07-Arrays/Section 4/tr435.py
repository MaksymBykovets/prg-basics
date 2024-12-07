array = [
    [-38, 19],
    [5, 40],
    [-7, 11],
    [29, 16]
]

# Initialize variables to track the smallest and largest values and their positions
min_value = float('inf')  # Start with a very large number for comparison
max_value = float('-inf')  # Start with a very small number for comparison
min_position = (-1, -1)  # Row and column of the smallest value
max_position = (-1, -1)  # Row and column of the largest value

# Iterate through the array to find the smallest and largest values and their locations
for row_index, row in enumerate(array):
    for col_index, value in enumerate(row):
        if value < min_value:
            min_value = value
            min_position = (row_index, col_index)
        if value > max_value:
            max_value = value
            max_position = (row_index, col_index)

# Print the results
print(f"Smallest value: {min_value} at row {min_position[0]}, column {min_position[1]}")
print(f"Largest value: {max_value} at row {max_position[0]}, column {max_position[1]}")