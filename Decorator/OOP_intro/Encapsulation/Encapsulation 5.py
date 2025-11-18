class Employee:
    def __init__ (self, name, salary):
        self.name = name
        self.salary = salary

class Manager(Employee):
    def show_salary(self):
        print(f"self.name' s salary {self.salary}") 
m = Manager ("Ali", 8000)
m.show_salary()

print(m.salary)