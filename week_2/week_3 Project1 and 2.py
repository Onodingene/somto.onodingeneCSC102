#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Program to calculate the roots of a cubic equation 
import cmath
print("CODE TO FIND THE ROOTS OF A CUBIC EQUATION")

print("The co-efficient of x raised to the power of 3 is A")
A = int(input("Input the value of A "))
print("The co-efficient of x raised to the power of 2 is B")
B = int(input("Input the value of B "))
print("The co-efficient of x  is C")
C = int(input("Input the value of C "))
print("The constant term that has no coefficient is D")
D = int(input("Input the value of D "))

E = int(3 * C - B*B / 9)
# print(E)
F = 9 * B * C - 27 * A - 2 * B*B*B
# print(F)
G_F = cmath.sqrt(E^3 + F^2)
# print(G_F)
H = (F + G_F) ** (1/3)
# print(H)
H_G = cmath.sqrt(E^3 + F^2)
# print(H_G)
I = (F - G_F) ** (1/3)
# print(I)

x1 = H + I - 1/3 * B
print(f"The first root is {x1}")

x2 = -1/2*(H + I) - 1/3*B + 1/2*cmath.sqrt(3)*(H - I)
print(f"The second root is {x2}")

x3 = -1/2 *(H +I )- 1/3 *B - 1/2 *cmath.sqrt(3)*(H -I)
print(f"The second root is {x3}")






# In[ ]:


#PROJECT 2
#Program to get the roots of a quadratic equation
from math import sqrt
a = float(input("The value of a ="))
b = float(input("The value of b ="))
c = float(input("The value of c ="))
d = b * b -4 *a*c
if d > 0:
    x1 = (-b + sqrt(d)) / (2*a)
    x2 = (-b -sqrt(d)) / (2*a)
    print(f"The first root is {x1} and the second root is {x2}")

elif d == 0:
    x1 = -b / (2*a)
    print(f"The first root is {x1}")

else:
    print("No root")

