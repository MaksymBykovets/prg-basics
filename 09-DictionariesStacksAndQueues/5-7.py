hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    names = []
    for hotel in hotels:
        names.append(hotel["name"])
    return ", ".join(names)

def avg_price(hotels):
    total = 0
    for hotel in hotels:
        total += hotel["price"]
    return round(total / len(hotels))

krakow_names = hotel_list(hotels_in_Krakow)
price_krakow = avg_price(hotels_in_Krakow)
print("Hotels in Krakow: ", krakow_names)
print("Average hotel price in Krakow: ", price_krakow)

sopot_names = hotel_list(hotels_in_Sopot)
price_sopot = avg_price(hotels_in_Sopot)
print("Hotels in Sopot: ", sopot_names)
print("Average hotel price in Sopot: ",  price_sopot)

if price_krakow > price_sopot : 
    print("Cheaper hotels in Sopot")
elif price_krakow < price_sopot : 
    print("Cheaper hotels in Krakow")
else : 
    print("Prices are the same")
