from decimal import *
import math


def calc():
    getcontext().prec = 800

    k1 = (Decimal(2).sqrt() * 2)
    k2 = Decimal(k1 / 9801)
    pi = Decimal(0)

    # at 100 iterations, the accuracy is about 800 decimals
    for i in range(100):
        f1 = Decimal(math.factorial(4 * i))
        f2 = Decimal(1103 + 26390 * i)
        ff1 = Decimal(f1 * f2)
        f3 = Decimal((math.factorial(i)) ** 4)
        f4 = Decimal(396 ** (4 * i))
        ff3 = Decimal(f3 * f4)
        ff4 = Decimal(ff1 / ff3)
        pi = pi + ff4

    pi = 1 / (pi * k2)

    print(pi)


if __name__ == "__main__":
    calc()
