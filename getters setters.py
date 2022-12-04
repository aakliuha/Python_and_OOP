class Students:

    __School_name = 'Kalush school #5'

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def set_school_name(self, School_name):
        self.__School_name = School_name

    def get_school_name(self):
        print(self.__School_name)
        return self.__School_name

    def __getInfo(self):
        print(self.__School_name)
        return self.__School_name




alisa = Students('Alisa', 30)
alisa.set_school_name('Broshniv')
alisa.get_school_name()






