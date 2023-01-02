class Animal:

    came_from = 'USA'
    certificate = '2022/05/11'

    def __init__(self, name, weight):
        self.name = name
        self.weight = weight

    def print_info(self):
        print(f"came_from: {self.came_from} - {Animal.came_from}, name is: {self.name} and its weight is: {self.weight}")

    @classmethod
    def print_class_info(cls):
        print(cls.came_from)

    @staticmethod
    def print_certificate():
        print("certificate #125484512")
        print(Animal.certificate)




cat = Animal('Okko', 6)
dog = Animal('Neo', 15)


cat.came_from = 'German'
cat.print_info()
dog.print_info()
Animal.print_class_info()

Animal.came_from = 'France'

cat.print_info()
dog.print_info()

print(cat.__dict__)
print(dog.__dict__)

cat.print_class_info()

Animal.print_certificate()
cat.print_certificate()




