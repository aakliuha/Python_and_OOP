lst1 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
lst2 = [35, 44, 56]
lst3 = (8, 6, 7, -85, 0)
lst4 = {'cash', 8}

def prog(*args):
    lst = []
    for i in args:
        lst.append(i)
    mylist = [j for i in lst for j in i]
    return mylist

print(prog(lst1, lst2, lst3, lst4))
