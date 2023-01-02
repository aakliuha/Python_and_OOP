class Salary:
    def __init__(self, payment, bonuses):
        self.payment = payment
        self.bonuses = bonuses

    def get_salary(self):
        return (self.payment*12)+self.bonuses


class Employee:
    def __init__(self, name, department, payment, bonuses):
        self.name = name
        self.department = department
        self.salary = Salary(payment, bonuses)


vasya = Employee('Vasya', 'IT', 1300, 650)
print(vasya.salary.get_salary())


