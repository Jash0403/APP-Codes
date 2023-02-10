class Rectangle:
    def __init__(self, *inp):

        # when no argument is passed
        if len(inp) == 0:
            self.length = 0
            self.breadth = 0

        # when 1 arguments are passed
        elif len(inp) == 1:
            self.length = inp[0]
            self.breadth = inp[0]

        # when 2 arguments are passed
        elif len(inp) == 2:
            self.length = inp[0]
            self.breadth = inp[1]

    def area(self):
        return self.length * self.breadth


r1 = Rectangle()
r2 = Rectangle(3)
r3 = Rectangle(3, 4)
print(r1.area())
print(r2.area())
print(r3.area())
