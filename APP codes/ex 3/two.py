class CTECH:
    pass


class CINTEL:
    pass


class NWC:
    pass


class DSBS:
    pass


ctech1 = CTECH()
cintel1 = CINTEL()
nws1 = NWC()
dsbs1 = DSBS()
print(isinstance(ctech1, CTECH))
print(isinstance(cintel1, CINTEL))
print(isinstance(nws1, NWC))
print(isinstance(dsbs1, DSBS))
print(isinstance(ctech1, NWC))
print(isinstance(nws1, DSBS))

print(issubclass(CTECH, object))
print(issubclass(CINTEL, object))
print(issubclass(NWC, object))
print(issubclass(DSBS, object))
