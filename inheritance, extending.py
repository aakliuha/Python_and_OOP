class People:

    __country_of_origin = 'USA'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def __call(self):
        print(f'Hey {self.__name}! Let"s go play outside')

    def callPrivateMethods(self):
        self.__call()

    @property
    def name(self):
        print(self.__name)
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @name.deleter
    def name(self):
        del self.__name

    @property
    def getAge(self):
        print(self.__age)
        return self.__age


class Man(People):
    def __init__(self, name, age, martialStatus = 'single'):
        super().__init__(name, age)
        self.martialStatus = martialStatus

    def callPrivateMethods(self):
        print("Hi the pretty stranger. I'm so lonely. Be my friend")
        super().callPrivateMethods()


    def go(self):
        if self.martialStatus == 'single' or self.martialStatus == 'lonely as fuck':
            self.callPrivateMethods()
        else:
            print('This person can not play with you!!!')


anton = Man('Anton', 30, 'lonely as fuck')
oleg = Man('Oleg', 12, 'not decided yet')
anton.name
anton.getAge
anton.go()

oleg.name
oleg.getAge
print(oleg.martialStatus)
oleg.go()








