from time import *

def outer(seconds=2):
    def decor(func):
        def wrapper(*args, **kwargs):
            res = func(*args, **kwargs)
            sleep(seconds)
            print('decorating complete')
            return res
        return wrapper
    return decor


@outer()
def getKeys():
    print("getting keys from DB...")
    return None

getKeys()

# second way to hang decorator on function
#keys = decor(getKeys)
#keys()

