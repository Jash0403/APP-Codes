# Integrate x^2, sin(x), cos(x) in terms of x and y


import sympy as sym


x = sym.Symbol('x')
y = sym.Symbol('y')


eqn1 = x**2
eqn2 = sym.sin(x)
eqn3 = sym.cos(x)

print(sym.integrate(eqn1, x))
print(sym.integrate(eqn2, x))
print(sym.integrate(eqn3, x))
print(sym.integrate(eqn1, y))
print(sym.integrate(eqn2, y))
print(sym.integrate(eqn3, y))
