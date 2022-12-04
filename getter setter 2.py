class Students:

    __School_name = 'Kalush school #5'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, age):
        self.__age = age

    def __getInfo(self):
        print(self.__School_name)
        return self.__School_name

    @age.deleter
    def age(self):
        del self.__age

    #age = property(get_age, set_age, delete_age)

    def __del__(self):
        print("object has been deleted")


olya = Students('Olya', 28)
print(olya.__dict__)

olya.age = 40
print(olya.__dict__)
print(olya.age)
del olya.age









