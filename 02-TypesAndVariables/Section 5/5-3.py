###
# A program that calculates the volume
# and surface area of ​​a cuboid with sides a, b, and c.
# Read the dimensions of the cuboid from the keyboard.
#
a = input('a=')
b = input('b=')
c = input('c=')
a = int(a)
b = int(b)
c = int(c)
cuboid_volume = a * b * c
cuboid_surface_area = 2 * (a*b) + 2 * (a*c) + 2 * (b*c)
print(f'The volume of a cuboid with sides {a}, {b} and {c} is {cuboid_volume}')
print(f'The surface area of a cuboid with siddes {a}, {b} and {c} is {cuboid_surface_area}')