#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# PROJECT 1 
class oranges():
    def quantity(self):
        amount = int(input("Enter the number of oranges you want? "))
        if amount > stock_quanity:
                print(f"Please input a quantity less than {stock_quanity}")
                print("THANK YOU FOR YOUR PATRONAGE!")
        else:
            real_amount = 300 * amount
            print(f"The price of your oranges is {real_amount}")
            print("THANK YOU FOR YOUR PATRONAGE!")
print("THE ORANGE MARKET")
print("An orange costs 300 Naira")
stock_quanity = 20
market = oranges()
market.quantity()




# In[2]:


# PROJECT 2
class equations():
    def trapezium(self):
        height = int(input("Enter your height "))
        base1 = int(input("Enter your base 1  "))
        base2 = int(input("Enter your base 2 "))
        area = (height/2) * (base1 + base2)
        print(f"The area of the trapezium is : {area}")

    def rhombus(self):
        diagonal1 = int(input("Enter diagonal 1 "))
        diagonal2 = int(input("Enter diagonal 2 "))
        area2 = 0.5 * (diagonal1*diagonal2)
        print(f"The area of the rhombus is: {area2}")

    def parallelogram(self):
        base = int(input("Enter your base "))
        altitude = int(input("Enter your altitude" ))
        area3 = base * altitude
        print(f"The area of the parallelogram is {area3}")

    def cube(self):
        length = int(input("Enter the length "))
        area4 = 6 * (length **2)
        print(f"The area of the cube is: {area4}")

    def cylinder(self):
        radius = int(input("Enter the radius "))
        height = int(input("Enter the height "))
        volume = 3.14 * (radius **2)*height
        print(f"The volume of the cylinder is: {volume}")

calculation = equations()
print("WELCOME TO THE CALCULATOR")
print("ENTER 1 = Area of Trapezium"
      "2 = Area of Rhombus"
      "3 = Area of Parallelogram"
      "4 = Area of a Cube"
      "5 = Volume of a cylinder")
user_input = input("Enter the formula you want ")
if user_input == "1":
    calculation.trapezium()
elif user_input == "2":
    calculation.rhombus()
elif user_input == "3":
    calculation.parallelogram()
elif user_input == "4":
    calculation.cube()
elif user_input == "5":
    calculation.cylinder()
else:
    print("INPUT A VALID FORMULA")


# In[ ]:




