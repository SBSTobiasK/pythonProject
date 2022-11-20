def cube(a):
    return a*a

list1 = [i for i in range(1, 100, 2)]
list2 = list(map(cube, list1))

print(list1)
print(list2)

list_ges = list(zip(list1,list2))
print(list_ges)

for a, b in list_ges:
    print(a, b)

