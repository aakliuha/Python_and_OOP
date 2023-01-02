
count = 0

def func():
    global count
    count += 1
    print(count)
    print('this is recursion')
    func()


func()