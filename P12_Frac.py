class Frac:
    def __init__(self, div, der=1):
        g = gcd(div, der)
        self.div = div // g
        self.der = der // g

    def __repr__(self):
        return '%s/%s' % (self.div, self.der)

    def __add__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(self.div * other.der + self.der * other.div,
                    self.der * other.der)

    def __radd__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(self.der * other.div + self.div * other.der,
                    self.der * other.der)

    def __sub__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(self.div * other.der - self.der * other.div,
                    self.der * other.der)

    def __rsub__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(self.der * other.div - self.div * other.der,
                    self.der * other.der)

    def __mul__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(self.div * other.div,
                    self.der * other.der)

    def __rmul__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(other.div * self.div,
                    other.der * self.der)

    def __truediv__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(self.div * other.der,
                    self.der * other.div)

    def __rtruediv__(self, other):
        if type(other) == int:
            other = Frac(other)
        return Frac(other.div * self.der,
                    other.der * self.div)

def gcd(a,b):
    a = abs(a)
    b = abs(b)
    if a<b:
        a, b = b, a
    while a!=b and b!=0:
        a, b = b, a%b
    return a


if __name__ == '__main__':
    a = Frac(3, 4)
    b = Frac(4, 5)
    print(a, b)

    print(a+b)
    print(a-b)
    print(a*b)
    print(a/b)

    print(b+a)
    print(b-a)
    print(b*a)
    print(b/a)
