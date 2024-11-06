amount_ast = int(input("Enter amount of aserisks : "))

def f(n) : 
     return "*/*" * (n - 1) if n > 0  else ""

print (f(amount_ast))