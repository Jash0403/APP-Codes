# Solve the system of equations x+y=2, 2x+y=0


import sympy as sym


x = sym.Symbol('x')
y = sym.Symbol('y')


eqn1 = x + y - 2
eqn2 = 2*x + y


soln = sym.solve([eqn1, eqn2], [x, y])
print(soln)
