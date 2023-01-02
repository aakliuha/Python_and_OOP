import random

lst1 = [x for x in range(-10, 10, 2)]

print(lst1)


lst2 = [round(random.uniform(-10, 10), 2) for x in range(10)]
print(lst2)

lst3 = lst1 + lst2
print(len(lst1), len(lst2), len(lst3))


res = sorted(lst3)
print(res)


print(sorted(lst3, key=lambda x: abs(x)))


