class Student:
    def __init__(self, name, grades):
        self.name = name
        self._grades = grades   

    def display_grades(self):
        print(f"{self.name}'s grades: {self._grades}")


s1 = Student("Ali", [90, 85, 88])


s1.display_grades()


