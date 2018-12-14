from decimal import *
import math

getcontext().prec = 1000

k2 = Decimal(426880) * Decimal(10005).sqrt()
k3 = Decimal(1/(k2))

pi = 0
for i in range(70):
    f1 = Decimal(math.factorial(6*i))
    f2 = Decimal(13591409 + 545140134*i)
    f3 = f1 * f2
    f4 = Decimal(math.factorial(3*i))
    f5 = Decimal((math.factorial(i))**3)
    f6 = Decimal((-640320)**(3*i))
    f7 = f4 * f5 * f6
    f8 = f3 / f7
    pi = pi + f8

pi = 1/(pi * k3)

print(pi)
