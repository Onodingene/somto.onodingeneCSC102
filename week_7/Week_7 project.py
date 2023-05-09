#!/usr/bin/env python
# coding: utf-8

# In[1]:


# PYTHON PROJECT 1; WEEK_7

# print("J-T VENTURES EMPLOYEE VERIFICATION")
first_name = input("Please, input your first name ").lower()
department = input("Please input your department ").lower()
employee_names = ["oluwatamilore","ayomide","oshim","chukwunonye","chiemeziem","oluwatimilehin","osose","daniel","onyekachi","shalom","nedi","stephanie","jason","edward","otu","onyinyechi","makuochukwu","moyosore","ayonete","eche","michael","oluwadamilola","chijindu","joseph","daisy","samuel","betha","boluwatife","mary","rapahel","victor","derek","aakorede","rasheed","daniel","mary-cynthia","owoede","oluwafikunmi","uchenna","ejike"]
employee_department = ['logistics','accounting','delivery','accounting','logistics','accounting','logistics','delivery','delivery','delivery','logistics','accounting','administration','delivery','administration','administration','logistics','accounting','accounting','accounting','logistics','logistics','delivery','delivery','administration']

if first_name in employee_names and department in employee_department:
    print("WELCOME TO JT DELIVERY VENTURE!")
    print(f"{first_name}, you are a verified employee in the {department} department")
    import pandas as pd
    data = pd.read_csv('jt-ventures.csv')
    print(data)
else:
    print("VERIFICATION FAILED!")
    print(f"{first_name} does not exist on the employee verification page")


# In[ ]:


# PROJECT 2
print("WELCOME TO YEGA SERVICES!!!")
location = input("Which location do you want your package to be delivered to? ").lower()
weight = int(input("How much does your package weigh in kg? "))

if location == 'ibeju-lekki' and weight >= 10:
    print("Your delivery fee is 2000 Naira")
elif location == 'ibeju-lekki' and weight < 10:
    print("Your delivery fee is 1500 Naira")
elif location == 'epe' and weight >= 10:
    print("Your delivery fee is 5000 Naira ")
elif location == 'epe' and weight < 10:
    print("Your delivery location is 4000 Naira")
else:
     print("Please tye in a valid location and weight ")


# In[1]:





# In[ ]:


import pandas as pd
print("WELCOME TO PAU ADMISSIONS FOR COMPUTER SCIENCE AND MASS COMMMUNICATION")
print()
name = input("Input your full name ")
print()
print("Do you intend to study computer science or Mass communication")
y_n = input("Input 'C' for Computer science and 'M' for mass communication ").upper()
computer_science = "C"
mass_communication = "M"
if y_n == "C":
    jamb = int(input("Input your JAMB score"))
    print("Input your grade for the following POST UTME subjects ")
    print()

    physics = input("Physics - ").lower()
    chemistry = input("Chemistry - ").lower()
    math = input("Mathematics - ").lower()
    english = input("English - ").lower()
    biology = input("Biology - ").lower()
    subjects = physics,chemistry,math,english,biology
    print()
    print("Did you pass the interview? ")
    y = "yes"
    n = "no"
    interview = input("Input Y for YES and N for NO ").lower()

    if jamb < 230 or interview == "n" or subjects == "d7" or subjects == "e8" or subjects == "f9":
        print(f"Sorry,{name} you do not meet the requirements to be a computer scientist")
        cap = {'NAME': [",","","",""],
                   'JAMB SCORE': ["", "", "", ""],
                   'POST UTME': ["", "", "", ""]}
        df = pd.DataFrame(cap)
        df.to_csv('not_admitted.csv')
        rat = pd.read_csv('not_admitted.csv')
        print(rat)
    else:
        print(f"Congratulations,{name},you are eligible to study computer science")
        records = {'NAME': ["", "", "", ""],
                   'JAMB SCORE': ["", "", "", ""],
                   'POST UTME': ["", "", "", ""]}
        df = pd.DataFrame(records)
        df.to_csv('admitted.csv')
        data = pd.read_csv('admitted.csv')
        print(data)
elif y_n == "M":

    jamb = int(input("Input your JAMB score"))
    print("Input your grade for the following POST UTME subjects ")
    print()

    government = input("Government - ").lower()
    literature = input("Literature - ").lower()
    math = input("Mathematics - ").lower()
    english = input("English - ").lower()
    history = input("History - ").lower()
    subjects = government, literature, math, english, history
    print()
    print("Did you pass the interview? ")
    y = "yes"
    n = "no"
    interview = input("Input Y for YES and N for NO ").lower()

    if jamb < 220 or interview == "n" or subjects == "d7" or subjects == "e8" or subjects == "f9":
        print(f"Sorry,{name} you do not meet the requirements to be a mass communication")
    else:
        print(f"Congratulations,{name},you are eligible to study mass communication")
else:
    print("please input a valid course")


# In[ ]:




