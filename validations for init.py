class Persons:

    def __init__(self, age, passport, weight, name = dict.fromkeys(['firstName', 'lastName'])):

        self.__age = self.validate_age(age)
        self.__passport = self.validate_passport(passport)
        self.__weight = self.validate_weight(weight)
        self.__name = name

    def validate_age(self, age):
        if 14 <= age <= 120 and type(age) == int:
            return age
        raise ValueError('age should be int in range 14 to 120')

    def validate_passport(self, passport):
        if len(str(passport)) in range(0, 10):
            return passport
        raise ValueError('passport should be in range 0 to 9')

    def validate_weight(self, weight):
        if type(weight) == (int or float) and weight >= 20:
            return weight
        raise ValueError('weight cannot be less then 20 kg and should be a number')

andrii = Persons(31, 457784, 68)
print(andrii.__dict__)

