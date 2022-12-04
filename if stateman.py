def func():
    num = int(input("enter number"))
    if 0 < num < 10:
        print(f"{num} is a decent number")
    elif 11 < num < 100:
        print("try again")
    elif num >= 1000:
        print(num ** 0.5)

func()