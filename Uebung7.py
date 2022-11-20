import matplotlib.pyplot as plt
import math

list_x = [i*0.1 for i in range(0, 1000+1)]
list_y = [math.sin(i) for i in list_x]

plt.plot(list_x, list_y)
plt.show()