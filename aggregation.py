class Salary:
    def __init__(self, payment, bonuses):
        self.payment = payment
        self.bonuses = bonuses

    def get_salary(self):
        return (self.payment*12)+self.bonuses


class Employee:
    def __init__(self, name, department, salary):
        self.name = name
        self.department = department
        self.salary = salary

    def show_salary(self):
        print(salary.get_salary())

salary = Salary(1250, 300)

ira = Employee('Ira', 'Management', salary)
ira.show_salary()

del ira
print(id(salary))


