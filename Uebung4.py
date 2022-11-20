def add(a):
    return a+a

list1 = [i for i in range(1,101)]

#list2 = list(map(add, list1))
list2 = [i*4 for i in list1]

print(list1)
print(list2)