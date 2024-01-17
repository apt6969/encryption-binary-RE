import math
import time
import sys
import random



class EllipticCurve:
    """
    Simple representation of an elliptic curve.
    y^2 = x^3 + ax + b over finite field of prime p.
    """
    def __init__(self, a, b, p):
        self.a = a
        self.b = b
        self.p = p

        self.discriminant = -16 * (4 * a**3 + 27 * b**2)
        if self.discriminant == 0:
            raise ValueError("The curve {} is not smooth!".format(self))

    def is_on_curve(self, point):
        if point is None:
            # None represents the point at infinity.
            return True

        x, y = point
        return (y**2 - x**3 - self.a * x - self.b) % self.p == 0

    def add_points(self, point1, point2):
        if point1 is None:
            # None represents the point at infinity.
            return point2
        if point2 is None:
            return point1

        x1, y1 = point1
        x2, y2 = point2

        if x1 == x2 and y1 != y2:
            return None  # Point at infinity

        if x1 == x2:
            m = (3 * x1**2 + self.a) * pow(2 * y1, -1, self.p)
        else:
            m = (y2 - y1) * pow(x2 - x1, -1, self.p)

        x3 = m**2 - x1 - x2
        y3 = y1 + m * (x3 - x1)
        result = (x3 % self.p, -y3 % self.p)

        return result


# def is_prime(n):
#     """
#     Simple primality test using elliptic curves.
#     """
#     if n <= 1:
#         return False

#     # Choose random elliptic curve parameters
#     a = random.randrange(0, n)
#     b = random.randrange(0, n)
#     curve = EllipticCurve(a, b, n)

#     # Choose a random point on the curve
#     x = random.randrange(0, n)
#     y = random.randrange(0, n)
#     point = (x, y)
#     if not curve.is_on_curve(point):
#         return False
    

A_LARGE_USELESS_INT = sys.maxsize // 69696696969699
mersenne_primes = [2, 3, 5, 7, 13, 17, 19, 31, 61, 89, 107, 127, 521, 607, 1279, 2203, 2281, 3217, 4253, 4423, 9689, 9941, 11213, 19937, 21701, 23209, 44497, 86243, 110503, 132049, 216091, 756839, 859433, 1257787, 1398269, 2976221, 3021377, 6972593, 13466917, 20996011, 24036583, 25964951, 30402457]
not_merseene = [69, 69696696969699, A_LARGE_USELESS_INT]

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    max_divisor = math.isqrt(n)
    for d in range(3, max_divisor + 1, 2):
        if n % d == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False

    mersenne_number = 2 ** p - 1
    s = 4
    for _ in range(p - 2):
        s = (s ** 2 - 2) % mersenne_number

    return s == 0


if __name__ == "__main__":
# Example usage
#p = 2203# 82589933
    for p in mersenne_primes:#not_merseene:
        start_time = time.time()
        print(f"Is 2^{p} - 1 a Mersenne prime? {is_mersenne_prime(p)}")
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"Elapsed Time: {elapsed_time} seconds")