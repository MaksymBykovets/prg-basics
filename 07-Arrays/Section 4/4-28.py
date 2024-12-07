import matplotlib.pyplot as plt
import math

x = []
y = []

# create x values
for n in range(361):
   x.append(n)

# create y values
for n in x:
   y.append(math.sin(n))

# print chart
plt.plot(x, y)
plt.show()