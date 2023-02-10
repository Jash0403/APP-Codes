'''Calculate lim (sin(x)-x)/x^3
            x→0
'''
import sympy as sym


x = sym.Symbol('x')
sin_x = sym.sin(x)
x3 = sym.simplify(x**3)

eqn = sym.simplify((sin_x-x)/x3)

print(sym.limit(eqn, x, 0))
