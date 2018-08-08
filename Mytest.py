
# coding: utf-8

# In[1]:


#Arithemetic operations by passing variables directly
a=10 
b=20
print(a+b, a*b, a/b, a//b, a%b) #addition,multiplication,division,persantile


# In[2]:


#print 1 to 10 numbers using while loop
i=1
while i<=10:                       #run the loop from 1 to 10 times
    print(i, end=" ")
    i+=1                           #incrementing "i" by 1


# In[3]:


#To print even numbers using for loop

for i in range(10):
    if i%2==0:
        print(i, end=" ")


# In[4]:


#Multiplication table using "for-loop" ex:- to print like 5x1=5, 5x2=10,...

n=int(input("enter a number"))              # input while execution of type integer
for i in range(1,13):
        print(n,'x',i,'=', n*i)


# In[12]:


#loop within the loop by using for, to run the program as like the below:  

n=int(input("enter a number"))           
for i in range(1, n):
    for j in range(1,i+1):             '''first run the inner loop, upto the condition satisfy'''
        print('*', end=" ")    
    print()


# In[13]:


#To run the program as like the below output:

n=int(input("enter a number"))
for i in range(1, n):
    for j in range(1,n+1):
        print('*', end=" ")    
    print()


# In[27]:


#To run the program as like the below output:

n=int(input("enter a number:"))
i=n
while i>=1:
    for j in range(1,(i+1)):
        print('*', end=" ")    
    print()
    i-=1


# In[1]:


#print the numbers like -3 -2 -1 0 1 2 3:

n=int(input("enter a number:"))
for i in range(-n,n+1):
    print(i, end=" ")
    i+=n


# In[34]:


#To neglect some values within the range, done by @continue statement:

n=int(input("enter a number:"))
for i in range(1,n):
    if i==5:
        continue
    print(i, end=" ")


# In[35]:


#Check the use of @break statement to the below loop:

n=int(input("enter a number:"))
for i in range(1,n):
    if i==5:
        break
    print(i, end=" ")


# In[40]:


#get what value want by user within the range:

n=int(input("enter a number:"))
for i in range(1,n):
    if i==5:
#     break or continue continue not given, while enter a number lessthan 5 it doesnt shows o/p but if u enter morethan 5 value it prints 5

        print(i, end=" ")


# In[22]:


#To find factorial number, ex:- 5!= 5x4x3x2x1=120
i=1
f=1
n=int(input("Enter a number: "))
while i<=n:
    f=f*i
    i=i+1
    print("facorial value=",f)


# In[45]:


#To find factorial number, ex:- 5!= 5x4x3x2x1=120 n*(n-1)(n-2)...

def fact(n):                             #user defined function # called function 
    if n==1:
        return 1
    else:
        return n*fact(n-1)
n=int(input("Enter a number: "))
ans=fact(n)                        #calling function - to pass values to called function # having return type with arguments
print("factorial value", ans)


# In[33]:


#To find Sum of n natural numbers "with arguments with returntype" ex:- 1+2+3+,...n
def sum_natural(n):     #Userdefined function - called function #formal parameters/arguments
    if n==1:
        return 1
    else:
        return n+sum_natural(n-1)                              #returntype
    
n=int(input("enter a number"))
print("sum of natural numbers",sum_natural(n), end=" ")        #calling function passing value #actual arguments


# In[10]:


#To find the number is in fabonacci series - 0 1 1 2 3 5 8 13 21 like: fib(n)=fibo(n-1)+fibo(n-2)
def fibo(n):
    if n<=1:            #loop stops while n=1
        return n
    else:
        return(fibo(n-1)+fibo(n-2))
        
n=int(input("Enter a number:"))
print("fibo(n):", fibo(n), end=" ")
   


# In[41]:


# Exercises to print 0 to 20

for i in range(0,21):
    print(i, end=" ")


# In[55]:


#To print random integer within the including range

import random                 
print(random.randint(20,40))


# In[48]:


dir(random)


# In[11]:


#evaluate the expression x=y*y+2*y+1: 

import random
x=1
y=random.randint(-10,10)
print('enter a random number', y)                        #for the sake of to know the value of "y", i put print()
if y>0:
    x=y**2+2*y+1                 #x=y^2+2y+1
    print('x=y^2+2y+1:',x)
else:
    print(x)


# In[93]:


dir()


# In[94]:


import math
print(math.sqrt(4))


# In[95]:


dir(math)


# In[1]:


a=10
b=20
c=a+b
print(c)


# In[27]:


#***check out of passing three numbers which two numbers is a factor of third number:

num1 = int(input('Enter num1 :'))
num2 = int(input('Enter num2 :'))
num3 = int(input('Enter num3 :'))
if (num1>=num2 and num1>=num3) or (num2>=num3 and num2>=num1) or (num3>=num2 and num3>=num1):
    if num1%num2 == 0 and num1%num3 ==0: 
        print('{1},{2} is factor of {0}'.format(num1,num2,num3))
    else:
        print('{1},{2} is not a factor of {0}'.format(num1,num2,num3))

    if num2%num3 == 0 and num2%num1 ==0:
        print('{0},{2} is factor of {1}'.format(num1,num2,num3))
    else:
        print('{0},{2} is not a factor of {1}'.format(num1,num2,num3))

    if num3%num2 == 0 and num3%num1 ==0:
        print('{0},{1} is factor of {2}'.format(num1,num2,num3))
    else:
        print('{0},{1} is not factor of {2}'.format(num1,num2,num3))


# In[25]:


#program to calculate the given year is LEAP year or not
a = int(input('enter the year : '))
if (a%4 == 0 and a%100 != 0) or a%400 == 0:
    print('LEAP YEAR')
else:
    print('NOT LEAP YEAR')


# In[12]:


#palindrome for string ex:- 1)madam 2)mohan

s=input('Enter name :')                                  #s=  m a d a m
#print(s)                                                 s[] 0 1 2 3 4
n=len(s)
print(n)
i=0
#print(s[n-1])
if s[i]==s[n-1]:
    i+=1
    n-=1
    print('The name entered is a palindrome')
else:
    print('The name entered was not a palindrome')


# In[4]:


i=bool(0)
print(i)


# In[6]:


j=bool(4)
print(j)


# In[72]:


#rough work while reverse a palidrome, but it may compares the address, so alert: 
s=input('Enter a name or word :')
r=reversed(s)
#print(r)
if s==reversed(s):
    print('your entered name is a palindrome')
else:
    print('your entered name is not a palindrome')


# In[70]:


n=reversed("madam")
print(n)

