class SomeData:

    __slots__ = 'name', 'price', 'year'

    def __init__(self, name, price, year):
        self.name = name
        self.price = price
        self.year = year


#exm = SomeData('coin', 2650, 1890)
#print(exm.__slots__)
#exm.price = 3900
#print(exm.price)
#exm.country = 'USA'  # this will error out

class ChildData(SomeData):
    __slots__ = ()

cd = ChildData('car', 1000000, 1969)
print(cd.__slots__)
#print(cd.__dict__)
cd.country = 'England'   # this will error out
print(cd.__slots__)
#print(cd.__dict__)