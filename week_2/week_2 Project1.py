#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Program to calculate the roots of a cubic equation 
import random
print("CODE TO FIND THE ROOTS OF A CUBIC EQUATION")
print("The co-efficient of x raised to the power of 3 is A")
A = int(input("Input the value of A "))
print("The co-efficient of x raised to the power of 2 is B")
B = int(input("Input the value of B "))
print("The co-efficient of x  is C")
C = int(input("Input the value of C "))
print("The constant term that has no coefficient is D")
D = int(input("Input the value of D "))
x= random.randint(-1,1)
print(x)
equation = (A* x^3) - (B * x** 2) + (C*x) - (D)
if equation == 0:
    print(f"This is one of the roots of the equation{x}")
else:
    print("Run again to get the correct root of equation")

if A > 1:
    new = A/A
    new2 = B/A
    new3 = C/A
    new4 = D/A
    equation = print(f'Your new equation is {new}x^3 +{new2}x^2 + {new3}X + {new4}')
else:
    x = random.randint(-3, 3)
    equation = (A * x ^ 3) - (B * x ** 2) + (C * x) - (D)



# In[ ]:




