
# coding: utf-8

# In[8]:



# finding BMI IN DIFFERENT STAGES by if, elif and else statements 
a=float(input('enter your height in meters'))
b=float(input('enter your weight in kgs'))
c=(b/a**2)
print('the value of BMI is:',round(c,2))
if c>=17.5 and c<=18.5:
    print('you are under weight')
elif c>18.5 and c<=25:
    print('you are normal weight')
elif c>25 and c<=30:
    print('you are over weigght')
elif c>30 and c<=35:
    print('you are in obese class I')
elif c>35 and c<=40:
    print('you are in obese class II')
elif c>40 and c<=45:
    print('you are in obese class III')
else :
    print('you are in dangerous zone its time for run')


# In[2]:


#looping statement 
i=1
while i<=10:
    print(i)
    i+=1


# In[33]:


# finding prime numbers using while loop
num=int(input('enter a number'))
i=1
factorcount=0
while i<=num:
    if num%i==0:
        factorcount+=1
    i+=1
if factorcount==2:
    print('prime')
else:
    print('not prime')


# In[41]:


# finding armstrong numbers using while loop
num=int(input('enter a number'))
num1=num
s=0
while num>0:
    r=num%10
    s+=(r**3)
    num=num//10
if s==num1:
    print('armstrong number')
else:
    print('not a armstrong number')
    


# In[3]:


# finding palindrome numbers using while loop
num=int(input('enter a number : '))
num1=num
s=0
while num>0:
    r=num%10
    s=s*10+r
    num=num//10
if s==num1:
    print('palindrome number ')
else:
    print('not a palindrome number ')


# In[2]:


# definig function using def and finding maximum of two numbers
def max(num1,num2):
    if(num1>num2):
        result = num1
    else:
        result = num2
    return result


# In[3]:


#calling above function for finding maximum of two numbers
num1=int(input('enter a first number'))
num2=int(input('enter a second number'))
y=max(num1,num2)
print('maximum value is',y)


# In[2]:


# definig my own function for finding given number is even or odd number by true and false statements
def iseven(num):
    if num%2==0:
        return True
    else:
        return False
    
iseven(47)


# In[5]:


# definig my own function for finding given number is even or odd
n=int(input('enter a number'))
if iseven(n):
    print('given number is even')
else:
    print('given number is odd')

