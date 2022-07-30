# calculate if a is quadric residue mod p for some y
from tinyec.ec import SubGroup, Curve


class ecurve:
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p


def y_for_z(z, p):
    y1 = (z**3) % p
    y2 = (-z**3) % p
    return y1, y2


def is_quadric_residue_for_x(z, p):
    # z is a quadric residue mod p iff z**(p-1)/2 = 1 mod p or z**(p+1)/2 = z mod p
    # z**(p-1)/2 = 1 mod p
    if pow(z, (p-1)//2, p) == 1:
        return True
    # z**(p+1)/2 = z mod p
    if pow(z, (p+1)//2, p) == z:
        return True
    return False


def roots(curve):
    roots = []
    print("-----------------------------------------------------")
    print("X\t", "z\t", "residue\t", "y\t", "(x,y)")
    print("-----------------------------------------------------")
    for x in range(curve.p):
        z = (x ** 3 + curve.a*x + curve.b) % curve.p
        if is_quadric_residue_for_x(z, curve.p):
            y1, y2 = y_for_z(z, curve.p)
            print(x, "\t", z, "\t", is_quadric_residue_for_x(
                z, curve.p), "\t\t", y1, y2, "\t", (x, y1), (x, y2))
            roots.append((x, y1))
            roots.append((x, y2))
        else:
            print(x, "\t", z, "\t", is_quadric_residue_for_x(
                z, curve.p), "\t\t", "-\t", "-  -")
        print("-----------------------------------------------------")
    return roots


def points(curve):
    print('curve:', curve)
    # how many i * P we need range 2 to i+1
    for k in range(2, 13):
        p = k * curve.g
        print(f"{k} * G = ({p.x}, {p.y})")


# First find roots from ecurve(a,b,p) and roots()
curve1 = ecurve(1, 6, 11)
# roots(curve1)

# Then select a root from the list above, set field and curve and call points()
P = (2, 7)
field = SubGroup(p=11, g=P, n=18, h=1)
curve = Curve(a=1, b=6, field=field, name='curve')
# points(curve)
