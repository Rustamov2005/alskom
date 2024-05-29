class kalkolator():
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @staticmethod
    def kopaytirish():
        a = int(input("Birinchi sonni kiriting:"))
        b = int(input("Ikkinchi sonni kiriting:"))
        c = float(a * b)
        return c

    @staticmethod
    def bolish():
        a = int(input("Birinchi sonni kiriting:"))
        b = int(input("Ikkinchi sonni kiriting:"))
        c = float(a / b)
        return c

    @staticmethod
    def qoshish():
        a = int(input("Birinchi sonni kiriting:"))
        b = int(input("Ikkinchi sonni kiriting:"))
        c = float(a + b)
        return c

    @staticmethod
    def ayrish():
        a = int(input("Birinchi sonni kiriting:"))
        b = int(input("Ikkinchi sonni kiriting:"))
        c = float(a - b)
        return c

    def __str__(self):
        return f"({self.a} {self.b})"


calculator = kalkolator(12, 20)
print(calculator)
