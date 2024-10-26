###
# Calculates and prints the total washing time.
#
# A washing machine allows you to wash a jacket, which takes
# 40 minutes, wash underwear, which takes 70 minutes, and wash shoes,
# which takes 20 minutes. In addition, it is possible to program
# an additional rinse (15 minutes) and an additional spin (9 minutes).
#
total_washing_time = 0
program = input('Select washing program: (j)acket, (u)nderwear, (s)hoes:')
extra_rinse = input('Extra rinse? (y/n)')
extra_spin = input('Extra spin? (y/n)')

# Variables
time_jacket = 40
time_undewear = 70
time_shoes = 20
additional_rinse = 15
additional_spin = 9

if program == "j" : 
    total_washing_time = time_jacket
elif program == "u" :
    total_washing_time = time_undewear
elif program == "s" :
    total_washing_time = time_shoes
else :
    print("Invalid input")

if extra_rinse == "y" :
    total_washing_time += additional_rinse

if extra_spin == "y" :
    total_washing_time += additional_spin

print(f"Total washing time is {total_washing_time} min")