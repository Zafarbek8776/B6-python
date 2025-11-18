class Employee:
    def __init__(self, name, salary):
        self.name = name
        self._salary = salary     

    def show_salary(self):
        print(f"{self.name}'s salary is {self._salary}")   


emp = Employee("Ali", 5000)


emp.show_salary()


