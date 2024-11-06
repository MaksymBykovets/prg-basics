price = int(input("Enter price : "))
def f(price): 
    coins = 0 
    coins += price // 5 
    price %= 5 

    coins += price // 2 
    price %= 2 

    coins += price
    return coins

print(f"minimum number of coins : ", f(price))
