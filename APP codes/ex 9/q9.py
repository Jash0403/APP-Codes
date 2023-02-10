# Solve f''(x) + 9f(x) = 1


import sympy as sym


f = sym.Function('f')
x = sym.Symbol('x')

fdd = sym.diff(sym.diff(f(x), x), x)

print(sym.solve(fdd + 9*f(x) - 1, f(x)))
