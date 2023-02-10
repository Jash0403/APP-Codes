'''
Using matrices solve the linear equations
3x+7y=12z
4x-2y=5z
'''


import sympy as sym


x = sym.Symbol('x')
y = sym.Symbol('y')
z = sym.Symbol('z')


# solve the system of equations using matrices
A = sym.Matrix([[3, 7], [4, -2]])
B = sym.Matrix([12, 5])


soln = A.inv() * B
print(soln)
