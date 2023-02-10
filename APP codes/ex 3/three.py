class Dept:
    def __init__(self, name="SCO"):
        self.name = name

    def __str__(self):
        return self.name


class Student:
    def __init__(self, name, dept):
        self.name = name
        self.dept = dept

    def __str__(self):
        return f"{self.name} {self.dept}"


s1 = Student("S1", Dept("CSE"))
s2 = Student("S4", Dept())

print(s1)
print(s2)
