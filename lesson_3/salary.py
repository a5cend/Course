class Salary:
    def __init__(self, pay):
        self.pay = pay

    def get_total(self):
        return self.pay * 12


class Employee:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus
        self.salary = Salary(pay)

    def annual_salary(self):
        return print(f'Total: {self.salary.get_total() + self.bonus}')


obj1 = Employee(10, 25)
obj1.annual_salary()
