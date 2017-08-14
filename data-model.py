class Polynomial:
    def __init__(self, *coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        return "Polynomial {}".format(self.coeffs)

    def __add__(self, other):
        return Polynomial(*[x + y for (x, y) in zip(self.coeffs, other.coeffs)])

    def __len__(self):
        return len(self.coeffs)


P1 = Polynomial(5, 4, 3)
P2 = Polynomial(4, 3, 2)
P3 = P1 + P2
print(P3)
print(len(P3))
