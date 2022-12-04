from abc import ABC, abstractmethod

class Abstract(ABC):
    #__metaclass__ = ABCMeta

    @abstractmethod
    def print_info(self):
        pass


class School(Abstract):

    city = 'Kalush'

    def __init__(self, number, year):
        self.number = number
        self.year = year

    def print_info(self):
         print(f"city of {self.city}, school number {self.number}, found in {self.year}")


school1 = School(5, 1989)
school1.print_info()
