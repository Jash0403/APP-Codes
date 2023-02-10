class SRMIST:

    def __init__(self, school, dept1, dept2, dept3):
        self.school = school
        self.dept1 = dept1
        self.dept2 = dept2
        self.dept3 = dept3

    def __str__(self):
        return f"{self.school} {self.dept1} {self.dept2} {self.dept3}"

    def add_specialization(self, specialization):
        self.specialization = specialization
        return "added specialization"

    def show1(self):
        return f"{self.school} {self.dept1} {self.dept2} {self.dept3} {self.specialization}"

    def remove_dept(self):
        del self.dept1
        del self.dept2
        return "removed dept1 and dept2"

    def show2(self):
        return f"{self.school} {self.dept3} {self.specialization}"


srmist = SRMIST("SRMIST", "CSE", "ECE", "EEE")
print(srmist)
print(srmist.add_specialization("Computer Science"))
print(srmist.show1())
print(srmist.remove_dept())
print(srmist.show2())
