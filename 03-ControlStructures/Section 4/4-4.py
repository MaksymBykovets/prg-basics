university = 'Krakow University of Economics'
university_expanded = ''

for char in university:
    university_expanded += char + ' '

# Remove the trailing space
university_expanded = university_expanded.strip()

print(university_expanded)