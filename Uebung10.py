def verdoppeln(a):
    return a*2

list1 = [i*3 for i in range(1, 21)]

list2 = list(map(verdoppeln, list1))

print(list1)
print(list2)