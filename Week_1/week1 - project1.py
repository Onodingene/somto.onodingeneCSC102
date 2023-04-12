#!/usr/bin/env python
# coding: utf-8

# In[1]:


print("Program to compute the simple Interest")
principal = int(input("Input the principal "))
rate = int(input("Input the rate "))
time = int(input("Input the time in years "))
simple_interest = principal * (1+(rate/100) *(time))
print(f"The simple interest is {simple_interest}")


# In[2]:


print("Program to compute the compound interest")
principal = int(input("Input the principal "))
rate = int(input("Input the rate "))
time = int(input("Input the time in years "))
number = int(input("Input the number of times in a year that the principal is paid "))
compound_interest = principal * (1 + (rate / number)**number * time)
print(f"The compound interest is {compound_interest}")


# In[3]:


print("Program to compute An annuity plan")
principal = int(input("Input the principal "))
rate = int(input("Input the rate "))
time = int(input("Input the time in years "))
number = int(input("Input the number of times in a year that the principal is paid "))
annuity_plan = principal * (1 + rate/number ** number * time ) - 1)/ rate/number
print(f"The annual payment is {annuity_plan}")


# In[ ]:




