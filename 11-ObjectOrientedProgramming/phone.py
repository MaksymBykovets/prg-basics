class Phone():
    def __init__(self, brand, model, battery=100):
        self.brand = brand
        self.model = model
        self.battery = battery
    
    def make_call(self, contact) : 
        if self.battery > 0 : 
            print(f"Calling to {contact} from {self.brand} {self.model} ...")
            self.battery -= 5 
        else : 
            print("Battery has gone. You cannot call to someone")

    