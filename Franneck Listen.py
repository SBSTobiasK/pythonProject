import random

range_Val = 10

data = [random.randint(1, range_Val) for _ in range(range_Val)]
smaller = []
bigger = []
equal = []

user_input = int(input("Gib eine Zahl ein: "))

for i in data:
    if i > user_input:
        bigger.append(i)
    elif i < user_input:
        smaller.append(i)
    elif i == user_input:
        equal.append(i)

print("kleiner: ", smaller)
print("größer: ", bigger)
print("gleich: ", equal)
