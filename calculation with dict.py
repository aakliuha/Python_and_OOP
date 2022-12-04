
def add(num):
    return num + 10

def minus(num):
    return num - 2

def divide(num):
    return num / num

def multiple(num):
    return num * num

def processOperation(num, operator):
    operations = {
        "+": lambda num: num + 10,
        "-": lambda num: num - 2,
        "/": lambda num: num / num,
        "*": lambda num: num * num
    }
    op = operations[operator]
    return op(num)

print(processOperation(10, '*'))



