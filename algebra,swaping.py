
# coding: utf-8

# In[11]:


#math fundamentals
a = float(input('Enter first side: '))
b = float(input('Enter second side: '))
c = float(input('Enter third side: '))
# calculate the semi-perimeter
s = (a + b + c) / 2
# calculate the area traingle
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
print('The area of the triangle is',round(area,2))


# In[25]:


#area of the circle
from math import *
R=float(input (' enter the value of radius '))
A=pi*R**2
print('the area of circle is',round(A,2))


# In[5]:


#calulate body mass index
a=float(input('enter your height in m '))
b=float(input('enter your weight in kg '))
#calulate body mass index
c=(b/a**2)
print('the value of body mass index is',round(c,2))


# In[30]:


# convertion of seconds into minutes and hours
s=int(input('Enter Number of seconds to convert'))
a=s/60
print('Number of Minitues: ',round(a,2))
b=s/360
print("Number of Hours :",round(b,3)) 


# In[33]:


#findind simple intrest
P=float(input('enter the principal amount'))
T=float(input('enter time'))
R=float(input('enter the rate of intrest'))
SI=(P*T*R)/100
print('simple intrest is',SI)


# In[9]:


#converting number into minutes and secs
x=int(input('enter the number'))
m=int(x/60)
print('minutes',m)
s=x%60
print('sec',s)


# In[10]:


#coverting secs into days,hours,minutes and secs
time = float(input("Input time in seconds"))
day = time // (24 * 3600)
time = time % (24 * 3600)
hour = time // 3600
time %= 3600
minutes = time // 60
time %= 60
seconds = time
print("d:h:m:s-> %d:%d:%d:%d" % (day, hour, minutes, seconds))


# In[14]:


# area of the rectangle
W=eval(input(' enter the value of width '))
L=eval(input(' enter the value of lenth '))
S=W*L
print(' area of the rectangle is: ',S)


# In[10]:


# The area of the circle 
from math import *
R=float(input (' the value of radius is '))
A=pi*R**2
print(' The area of the circle is:',round(A,2))


# In[18]:


# sum of 2 numbeers
a=eval(input(' enter the first value: '))
b=eval(input(' enter the second value: '))
c=a+b
print(' the sum of two values: ',c)


# In[2]:


#swapping of two numbers
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
x=x+y
y=x-y
#x=x-y
print('swapping of x and y values:',x,y)


# In[1]:


# swapping of two numbers by * /
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
x=x*y
y=x/y
x=x/y
print('swapping of x and y values:',x,y)


# In[35]:


# swapping of two numbers
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
x=x^y
y=x^y
x=x^y
print('swapping of x and y values:',x,y)


# In[5]:


#Evaluate expression - x=x^y:?
x=int(input('enter the value of x:'))
y=int(input('enter the value of y:'))
x=x^y #exclusive or
print(x)


# In[8]:


3^6 #coverting values to binary and apply "ex-or"


# In[34]:


# swapping of two numbers by using temparory value
x=int(input('enter value of x:'))
y=int(input('enter value of y:'))
temp=x
x=y
y=temp
print('the value of x after swapping',x)
print('the value of y after swapping',y)


# In[38]:


#fahrenheit to celsius 
a=int(input('enter the temperature in fahrenheit : '))
b=a-32
c=b*5
d=c/9
e=d
print('convertion of fahrenheit to celsius is',round(e,2))


# In[41]:


# celsius to fahrenheit 
a=float(input('enter the temperature in celsius : '))
b=a*9
c=b/5
e=c+32
f=e
print('convertion of celsius to fahrenheit is',round(f,2))


# In[46]:


from math import *
M=int(input('enter the value of mass of the body : '))
C=int(input('enter the value of speed of light : '))
E=M*C
print('the energy equivalent : ',round(e,3))


# In[3]:


#Evaluate compound intrest
p=float(input('enter the principle amount : '))
r=float(input('enter the rate of intrest : '))
t=float(input('enter the number of years : '))
CI=p*(pow((1+r/100),t))
print('compond intrest is : ',round(CI,2))


# In[6]:


#Evaluate e=mc^2 energy finding
m=int(input('enter the mass value : '))
c=int(input('enter the speed of light : '))
e=m*c**2
print('The value of energy is',e)

