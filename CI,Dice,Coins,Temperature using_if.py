
# coding: utf-8

# In[1]:


#this program calculates the compound intrest
print('calculate the compound intrest')
P = float(input('Enter the value of the principle amount : '))
r = float(input('Enter the rate of intrest: '))
R = float(r/100)
n = int(input('enter the coumpound intrest frequency :1 ,2 , 4, 12 :'))
T = float(input('enter time in years :'))
import math
A = float(P * math.pow((1 + (R/n)),n*T))        
print ('Total Amount is :', round(A,2)) 


# In[3]:


# Swapping numbers with out using temp variable
A = int(input('Enter 1st number A : '))
B = int(input('Enter 2nd number B : '))
A = A * B
B = A / B
A = A / B
print('A = ', int(A))
print('B = ', int(B))


# In[37]:


# E = mc^2

m = float(input('Enter weight of the object in KG : '))
c = float(input('Enter the speed of the object in meters per sec :'))
K = float(m*(c**2))
print('Kinetic Energy of the object with weight {0} KG with speed {1} m/sec in jouls is :'.format(m,c), K)


# In[12]:


#temperature convertor from c to f
c = int(input('the temperature in centigrade :'))
f = float((c*9/5)+32)
print('The temperature in Fahrenheit :', f)


# In[38]:


#Converting Farhen heat to celsius scale reading

x = int(input('Enter 1 for (C to F) or 2 for (F to C):'))

if x == 1:
    X1 = int(input('enter temperature in centigrade :'))
    F = ((X1*9)/5) + 32
    print('The temperature in Fahrenheit is :',F)
    
elif x == 2:
    X1 = int(input('enter temperature in Fahrenheit :'))
    C = ((5/9)*(X1-32))
    print('The temperature in Centigrade is :',C)
    
else:
    print('You entered wrong value')


# In[4]:


#****remind it
import random as r
a = r.randint(1,10)
b = r.randint(1,10)
c = int(input('what is the value of '+ str(a)+'+'+str(b)+': ')) #it shows what is the input that it has been randomly taken, according to that take the input
#print(c)
if c == a+b:
    print('congratulations .. you won')
else:
    print('sorry, try again')


# In[4]:


#rolling a dice and check you won or lost:
import random as r
a = r.randint(1,6)
b = int(input('Dice Rolled...guess your number from 1 to 6 :'))
if a == b:
        print('jackpot ..you won')
else:
    print('number on the dice is :',a)
    print('sorry ..you lost')


# In[65]:


#won or loss while rolling a coin and say its head or tails:
import random as r
a = ['h','t']
A = r.choice(a)
#print(A)   
B = input('coin tossed..heads(h) or tails(t) : ')
if B == A:
    print('congrats you won the toss its :', A)
else:    
    print('Sorry you lost the toss its :', A)


# In[47]:


import random

x = ['a', 'b', 'c', 'd', 'e']
print(random.choice(x))


# In[12]:


import random as r
a = ['t','h']
A = r.choice(a)
print(A)


# In[90]:


#Head and toss
import random as r
a = ['h','t']
A = r.choice(a)

if A == 'h':
    x = 'HEADS'
else:
    x = 'TAILS'
    
B = input('coin tossed..heads(h) or tails(t) : ')
if B == A:
    print('congrats you won the toss its :', x)
else:    
    print('Sorry you lost the toss its :', x)


# In[12]:


#guess either head or toss -if ur guess true:"you won" by using predefined fn @choice()
import random as r
a=['h','t']
c=r.choice(a)       # @choice() ok, @choice[] not predefined
#print('randon variable is:',c)
b=str(input("enter either t or h:"))
if c==b:
    print('You won')
    
else:
    print('You loss')


# In[11]:


#guess either head or toss -if ur guess true:"you won" by @randint()
import random as r

a = int(r.randint(1,2))
print(a)
if a == 1:
    A = 'HEADS'
else:
    A = 'TAILS'
    
b = input('coin tossed..heads(h) or tails(t) : ')

if b == 'h':
    B = 'HEADS'
else:
    B = 'TAILS'
    
    
if A == B:    
    print('CONGRATS you won the toss its :', A)
else:    
    print('SORRY you lost the toss its :', A)





# In[40]:


#guess either head or toss -if ur guess true:"you won" by @randint()

import random
a=random.randint(1,2)
print("the random variable:",a)
if a==1:
    a='h'
else:
    a='t'
b=str(input("enter toss(t) or heads(h)="))
if a==b:
    print('you won')
else:
    print('you loss')

