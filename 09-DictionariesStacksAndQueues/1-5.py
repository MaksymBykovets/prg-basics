countries = [
{"name":"Poland", "population":38000000},
{"name":"Ukraine", "population":37000000},
{"name":"Germany", "population":84000000},
{"name":"Russia", "population":144000000},
{"name":"Turkey", "population":85000000}
]
print("COUNTRY  POPULATION")
for country in countries : 
    print(f"{country["name"]}  {country["population"]}")