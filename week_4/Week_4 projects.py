#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PROJECT 1
print("WELCOME TO SOMTO'S SCHOOL!")

girls = ['Samantha','Jada','Jane','Claire','Elizabeth','Mary','Susan','Waje','Taibat','Lilian']
girls_age = [17,16,17,18,16,18,17,20,19,17]
girls_height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
girls_scores = [80,85,70,60,76,66,87,95,50,49]

print("Name    |Age  | Height | score")
for i in range(len(girls)):
    print(girls[i] ,"|",girls_age[i],"|",girls_height[i],"|",girls_scores[i])

boys= ['Charles','Jude','James','Kelvin','Blodun','Wale','Kunle','Matthew','Tom','Kayode']
boys_age = [19,16,18,17,20,19,16,18,17,19]
boys_height = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
boys_score = [74,87,75,68,66,78,87,98,54,60]

for i in range(len(boys)):
    print(boys[i],boys_age[i],boys_height[i],boys_score[i])


# In[ ]:


# PROJECT 2 
print("WELCOME TO SOMTO'S SCHOOL!")

girls = ['Samantha','Jada','Jane','Claire','Elizabeth','Mary','Susan','Waje','Taibat','Lilian']
girls_age = [17,16,17,18,16,18,17,20,19,17]
girls_height = [5.5,6.0,5.4,5.9,5.6,5.5,6.1,6.0,5.7,5.5]
girls_scores = [80,85,70,60,76,66,87,95,50,49]

print("Name    |Age  | Height | score")
for i in range(len(girls)):
    print(girls[i] ,"|",girls_age[i],"|",girls_height[i],"|",girls_scores[i])

boys= ['Charles','Jude','James','Kelvin','Blodun','Wale','Kunle','Matthew','Tom','Kayode']
boys_age = [19,16,18,17,20,19,16,18,17,19]
boys_height = [5.7,5.9,5.8,6.1,5.9,5.5,6.1,5.4,5.8,5.7]
boys_score = [74,87,75,68,66,78,87,98,54,60]

for i in range(len(boys)):
    print(boys[i],boys_age[i],boys_height[i],boys_score[i])

# PROJECT 2
# import numpy as pd
# arr1 = pd.array([5,6,7,8,9])
# print(arr1)
# arr2 = pd.delete(arr1,[0,1])
# print(arr2)

print("WELCOME TO SOMIES $ CO")
name = input("Enter your name ")
age = int(input("Enter your age "))
experience = int(input("Enter your years of experience "))
if age >= 55 and experience > 25:
    print(f"{name}, your annual tax revenue is 5,600,000 naira")
elif age >= 45 and experience > 20:
    print(f"{name}, your annual tax revenue is 4,480,000 naira")
elif age >= 35 and experience > 10 :
    print(f"{name}, your annual tax revenue is 1,500,000 naira")
else:
    print(f"{name}, your annual tax revenue is 500,000 naira")


