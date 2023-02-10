# Calculate the expanded form of (x+y)^6.
import sympy as sym

x = sym.Symbol('x')
y = sym.Symbol('y')
expanded = sym.expand((x + y)**6)
print(expanded)
