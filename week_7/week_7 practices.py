#!/usr/bin/env python
# coding: utf-8

# In[1]:


# practice 1
def printme(str):
    print(str);
    return;
printme("Im first call to user defined function!")
printme("Again second call to the same function")


# In[2]:


# practice 2
def changeme (mylist):
    mylist.append([1,2,3,4])
    print("Values inside the function: ",mylist)
    return
mylist = [10,20,30]
changeme(mylist)
print("Values outside the function: ",mylist)


# In[7]:


# practice 3
def changme(mylist):
    mylist = [1,2,3,4];
    print("Values inisde the function: ",mylist)
    return
mylist = [10,20,30];
changme(mylist);
print("Values outsude the function: ", mylist)


# In[10]:


# practice 4
def printme(str):
    print(str);
    return;
printme(str);


# In[11]:


# practice 5
def printme(str):
    print(str);
    return;
printme(str = "My string")


# In[14]:


# practice 6
def printinfo(name,age):
    print("Name:",name);
    print("Age", age);
    return;
printinfo(age=50,name="miki");    


# In[16]:


# practice 7
def printinfo(name, age = 35):
    print("Name: ",name);
    print("Age: ",age);
    return;
printinfo(age = 50, name="Miki");
printinfo(name ="Miki");


# In[21]:


# practice 8
def printinfo(arg1, *vartuple):
    print("Outpus is: ")
    print(arg1)
    for var in vartuple:
        print(var)
        return;
printinfo( 10 );
printinfo(70,60,50);


# In[22]:


# practice 9
total = 50;
def sum(arg1,arg2):
    total = arg1 + arg2;
    print("Inside the function local total :  ",total)
    return total;
sum(10,20);
print("Outside the function global total : ",total)
    


# In[23]:


# practice 10
def swap(x,y):
    global a
    a = "Lawal"
    x,y = y,x

    b = "Chris"
    b = "Edward"
    c= "Lola"
    print(a,b,x,y)
    a = "Mary"
swap("Tina","Tolu")
print(a)


# In[ ]:




