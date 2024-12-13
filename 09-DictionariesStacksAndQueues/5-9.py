import csv
text_file = "vehicle.txt"
with open(text_file, "r", ) as file : 
    data = file.read()

province_file = "province.csv"
with open(province_file, "r",newline="", encoding="utf-8") as file : 
    data_province = csv.reader(file)

print(data_province)