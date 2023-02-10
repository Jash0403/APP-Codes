import functools


def mult(x, y):
    print('x=', x, 'y=', y)
    return x * y


fact = functools.reduce(mult, range(1, 4))
print('Factoral of 3:', fact)
