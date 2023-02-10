class PrintDT:
    def python_data(self, a):
        print(a)


p = PrintDT()
p.python_data(10)
p.python_data("Hello")
p.python_data([1, 2, 3])
p.python_data({"a": 1, "b": 2})
p.python_data((1, 2, 3))
p.python_data({1, 2, 3})
