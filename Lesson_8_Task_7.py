class ComplexNumber:
    def __init__(self, a, b, j=-1):
        self.a = a
        self.b = b
        self.j = j

    def __add__(self, other):
        return ComplexNumber(self.a + other.a, self.b + other.b)


    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a}i'

    def __str__(self):
        return f'{self.a}, {self.b}i'


z_1 = ComplexNumber(1, 2)  # self.a, self.b
z_2 = ComplexNumber(4, 3)  # other.a, other.b
print(z_1)
print(z_2)
print(z_1 + z_2)
print(z_1 * z_2)






