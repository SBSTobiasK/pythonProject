liste_x = [i for i in range(-20, 21, 1)]

a = int(input("A: "))
b = int(input("B: "))

liste_y = list((a*i + b) for i in liste_x)

print(liste_x)
print(liste_y)