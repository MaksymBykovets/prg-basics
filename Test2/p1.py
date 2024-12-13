def f(player1, player2) : 
    value1 = 0
    value2 = 0
    for item in player1 : 
        if item in ["A", "K", "Q", "J", "T"] : 
            value1 += 10
        else : 
            value1 += int(item)
    
    for item in player2 : 
        if item in ["A", "K", "Q", "J", "T"] : 
            value2 += 10
        else : 
            value2 += int(item)
    if value1 >= value2 : 
        return True
    else : 
        return False
    
print (f("9532", "K8"))