def func_generator(num):
    for i in range(num):
        yield i

def get_list(fun):
    a = []
    for y in fun:
        a.append(y)
    return a


a = get_list(func_generator(10))
print(a)
