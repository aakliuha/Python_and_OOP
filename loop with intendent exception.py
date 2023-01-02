def div(num):
    try:
        x = 100/num
        print(x)
    except ZeroDivisionError:
        print("Can not divide by zero")
    finally:
        print('run finished successfully')


for i in range(-10, 10):
    div(i)




