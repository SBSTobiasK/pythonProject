import matplotlib.pyplot as plt

def quadrat(param):
  return param*param

lst = range(-10, 11)

ergebnis=list(map(quadrat, lst))
print(ergebnis)

plt.plot(lst, ergebnis)
plt.show()
