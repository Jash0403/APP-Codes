# Simplify the trigonometric expression sin(x)/cos(x).


import sympy as sym


x = sym.Symbol('x')


sin_x = sym.sin(x)
cos_x = sym.cos(x)

print(sym.simplify(sin_x/cos_x))
