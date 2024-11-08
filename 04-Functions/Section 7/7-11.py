amount_ast = int(input("Enter amount of aserisks : "))

def f(n) : 
     if n < 0:
          print("Error, incorrect input")
     
     elif n > 0 :
          result = "*/" * (n-1) + "*"
     
     else : 
          result = ""
     return result
print (f(amount_ast))