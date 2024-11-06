##
# define a function month(n) 
# that returns a month name based on the month number
##

def month(n):
    months = ["January", "Fabruary", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    if 1<= n <= 12 : 
        return months[n-1]