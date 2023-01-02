class BaseEmployee:
    def __init__(self, name, eff_date):
        self.name = name
        self.effective_date = eff_date

    def print_info(self):
        print(f"employee name is {self.name}. Started working at {self.effective_date}")

class TaxesMixin:
    def salary_info(self):
        print("20% will be deducted from your salary")

class Employee(BaseEmployee, TaxesMixin):

    def __init__(self, department, payment, bonuses, name, eff_date):
        super().__init__(name, eff_date)
        self.department = department
        self.payment = payment
        self.bonuses = bonuses

    def get_salary(self):
        super().print_info()
        res = (self.payment*12)+self.bonuses
        return res



ivan = Employee('IT', 2200, 150, 'Ivan', '12/10/2010')
ivan.get_salary()
ivan.salary_info()




