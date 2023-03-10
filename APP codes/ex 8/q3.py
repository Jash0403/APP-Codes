from pyDatalog import pyDatalog

pyDatalog.create_terms(
    "brother,father,cousin,grandson,descendent,X,Y,Z,W,a,b,c,d,e,f")

+father('a', 'b')
+father('a', 'c')
+father('b', 'd')
+father('b', 'e')
+father('c', 'f')

brother(X, Y) <= (father(Z, X)) & (father(Z, Y)) & ~(X == Y)
cousin(X, Y) <= (father(Z, X)) & (father(W, Y)) & (brother(Z, W))
grandson(X, Y) <= (father(Y, Z)) & (father(Z, X))
descendent(X, Y) <= (father(Y, X))
descendent(X, Y) <= (father(Z, X)) & (descendent(Z, X))

print(brother(X, Y))
print(cousin(X, Y))
print(grandson(X, Y))
print(descendent(X, Y))
