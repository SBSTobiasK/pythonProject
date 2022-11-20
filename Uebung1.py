user_input = int(input("Geben sie eine Zahl ein: "))

liste = [[i, i*i] for i in range(1, user_input)]

for a, b in liste:
    print(a, b)