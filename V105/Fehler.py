from uncertainties import ufloat
import matplotlib.pyplot as plt
import numpy as np



def f(x):
    return (1.2566370621219 * 10**(-6) * x * (0.109**2))/((((0.109**2) + ((0.138/2)**2)))**(3/2)) *195

i1 = ufloat(2.7, 0.1)
i2 = ufloat(2.6, 0.1)
i3 = ufloat(2.3, 0.1)
i4 = ufloat(2.0, 0.1)
i5 = ufloat(1.8, 0.1)
i6 = ufloat(1.6, 0.1)
i7 = ufloat(1.5, 0.1)
i8 = ufloat(1.4, 0.1)
i9 = ufloat(1.35, 0.1)
i10 = ufloat(1.3, 0.1)

s1 = ufloat(0.5, 0.1)
s2 = ufloat(0.7, 0.1)
s3 = ufloat(0.9, 0.1)
s4 = ufloat(1, 0.1)
s5 = ufloat(1.3, 0.1)
s6 = ufloat(1.5, 0.1)
s7 = ufloat(1.8, 0.1)
s8 = ufloat(2.3, 0.1)
s9 = ufloat(3, 0.1)
s10 = ufloat(3.5, 0.1)

print(f(i1))
print(f(i2))
print(f(i3))
print(f(i4))
print(f(i5))
print(f(i6))
print(f(i7))
print(f(i8))
print(f(i9))
print(f(i10))

print("SCHWINGUNGGGGGGGGGGGGGGGGGGGGGG")
print(f(s1))
print(f(s2))
print(f(s3))
print(f(s4))
print(f(s5))
print(f(s6))
print(f(s7))
print(f(s8))
print(f(s9))
print(f(s10))

