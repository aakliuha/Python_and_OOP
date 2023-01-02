class SalaryMixin:
    def __init__(self, payment, bonuses):
        self.payment = payment
        self.bonuses = bonuses

    def get_salary(self):
        return (self.payment*12)+self.bonuses

class Employee(SalaryMixin):
    def __init__(self, name, department, payment, bonuses):
        super().__init__(payment, bonuses)
        self.name = name
        self.department = department

    def show_salary(self):
        print(self.get_salary())


oleh = Employee('Oleh', 'Security', 800, 710)
oleh.show_salary()

