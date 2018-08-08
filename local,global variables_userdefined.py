
# coding: utf-8

# In[3]:



# CALCULATING AREA OF THE CIRCLEby using define 'def' function 
from math import pi
def calculatearea(radius):
    area=pi*radius**2
    return area

z=calculatearea(5.6)
print('area of the circle=',z)


# In[8]:


#without arguments without return value:
def f1():
    x=10
    print(x)
f1()


# In[10]:


#userdefined functions - without return and without return type:
def f1():              #called function
    x=10               #passing values here
    print(x)
    
def f2():
    x=20
    print(x)
    
def f3():
    x=30
    print(x)
    
def f4():
    x=40
    print(x)
    
def f5():
    x=50
    print(x)
    

    
f1()            #caling function without passing values:
f2()
f3()
f4()
f5()
    
    


# In[12]:


#userdefined without arguments without return type with global variable:
y=111        #global variable accessed any where programme
def f1():
    x=10
    print(x,y)
    
def f2():
    x=20
    print(x,y)
    
def f3():
    x=30
    print(x,y)
    

f1()
f2()
f3()
print(x,y)         #x is a local variable cannot accessed out of the scope, y is global accessed any where in the programme
# x is local variable it cannot accessed outsidte remove x value from print


# In[13]:


#userdefined without arguments without return type with global variable:
y=111
def f1():
    x=10
    print(x,y)
    
def f2():
    x=20
    print(x,y)
    
def f3():
    x=30
    print(x,y)
    

f1()
f2()
f3()
print(y)
# no error


# In[17]:


#userdefined without arguments without return type with global variable, and make local variable as global then access outside also
y=111
def f1():
    global r
    r=10
    print(r,y)
    
def f2():
    x=20
    print(x,r)
    
def f3():
    x=30
    print(x,r,y)
    

f1()
f2()
f3()
print(r,y)
# if you want access x also in outside place global x in local varaible
# global variable is always place at top only see y=111 at top


# In[18]:


#default arguments in a function
def maxi(num1,num2,num3):
    print(max(num1,num2,num3))
    
maxi(10,20)
#TypeError: maxi() missing 1 required positional argument: 'num3'
# then place third number in calling function means maxi function


# In[19]:


#default arguments in a function
def maxi(num1,num2,num3):
    print(max(num1,num2,num3))
    
maxi(10,20,30)


# In[2]:


#default arguments in a function
def maxi(num1,num2,num3=40):
    print(max(num1,num2,num3))
    
maxi(10,50)


# In[1]:


#default arguments in a function
def maxi(num1,num2,num3=40):
    print(max(num1,num2,num3))
    
maxi(10,20)


# In[22]:


#default arguments in a function
def maxi(num1,num2=50,num3=40):
    print(max(num1,num2,num3))
    
maxi(10,20)
#means compulsery first place non default arguments then place default arguments


# In[23]:


#default arguments in a function
def maxi(num1=50,num2=60,num3):
    print(max(num1,num2,num3))
    
maxi(10,20)
# SyntaxError: non-default argument follows default argument
#means compulsery first place non default arguments then place default arguments like above example


# In[27]:


#default arguments in a function
def maxi(num1,num2=50,num3=40):
    print(max(num1,num2,num3))
    
maxi(10)
maxi(10,num2=90,num3=100)


# In[30]:


# returning multiple values
def calcgrade(num1,num2,num3):
    avavalue=(num1+num2+num3)/3
    if avavalue>=80:
        grade='A'
    elif avavalue>=60:
        grade='B'
    elif avavalue>=40:
        grade='C'
    else: 
        grade='f'
    return avavalue,grade

a,g=calcgrade(50,90,70)
print('avgscore=',a,'grade=',g)
#return both values 

