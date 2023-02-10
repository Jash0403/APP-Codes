# Calculate the derivative of log(x), 1/x, sin(x), cos(x) for x.

import sympy as sym

x = sym.Symbol('x')

print(sym.diff(sym.log(x), x))
print(sym.diff(1/x, x))
print(sym.diff(sym.sin(x), x))
print(sym.diff(sym.cos(x), x))
