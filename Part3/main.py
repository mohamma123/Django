class Employee:
    salary = 3000 # class variable

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def get_full_name(self):
        return self.first_name + " " + self.last_name

    def get_salary(self):
        return self.salary

employee = Employee("Ali", "Rezaie")
print(employee.get_full_name())
print(employee.get_salary())

Employee.salary = 3500
print(employee.get_salary())