###
# A program that prints your height both in cm and in feet and inches.
#
cm = 170
feet = float(round((cm / 30.48), 2 ))
feet_rounded = int(feet)
inches = float(round(((feet % 1) * 12 ), 1 ) )
# calculate the number of feet

print(f'I am {cm}cm tall, i.e. {feet_rounded} feet and {inches} inches')
