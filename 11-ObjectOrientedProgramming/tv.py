class TV:
    def __init__(self):
        self.is_on = False
        self.channel_no = 1
        
    def turn_off(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def show_status(self) : 
        if self.is_on : 
            print("TV is on")  
            print(f"Channel number is {self.channel_no}")
        else : 
            print("TV is off")
    def set_channel(self, new_channel_no) : 
        if self.is_on : 
            self.channel_no = new_channel_no
        else : 
            print("Cannot change channel while the TV is off")