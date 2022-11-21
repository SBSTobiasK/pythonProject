list1 = [i for i in range(1,101)]

teiler = []

for i in list1:
    if i % 3 == 0:
        teiler.append(i)

print(teiler)