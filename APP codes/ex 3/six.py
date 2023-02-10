class Banks_SRMIST:
    def getBalance():
        return 0

    class CUB:
        def __init__(self, deposit):
            self.deposit = deposit

        def getBalance(self):
            return self.deposit

    class HDFC:
        def __init__(self, deposit):
            self.deposit = deposit

        def getBalance(self):
            return self.deposit

    class Indian_Bank:
        def __init__(self, deposit):
            self.deposit = deposit

        def getBalance(self):
            return self.deposit


b1 = Banks_SRMIST.CUB(15000)
b2 = Banks_SRMIST.HDFC(30000)
b3 = Banks_SRMIST.Indian_Bank(40000)

print(b1.getBalance())
print(b2.getBalance())
print(b3.getBalance())
