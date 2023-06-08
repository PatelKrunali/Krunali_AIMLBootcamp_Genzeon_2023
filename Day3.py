#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#functions
def greet(name):
    '''this is function greets a person'''
    print("hello \t"+name+"\t Good Morning")
    
greet("Krunali")


# In[ ]:


#default
def A(a,b=1,c=2):
    return a+b+c
print(A(3))
print(A(4,4,4))
print(A(2,2))


# In[ ]:


#keyword
def A(a,b=1,c=2):
    return a+b+c
print(A(a=2,b=3))
print(A(c=3,a=1,b=8))


# In[ ]:


#positional
def A(a,b,c):
    return a+b+c
print(A(10,20,30))


# In[ ]:


#arbitrary keyword
def key_arg(**kwargs):
    return kwargs
my_dict=key_arg(Apples=10,Banana=20,Chiku=30)
print(my_dict['Apples'])
print(my_dict)


# In[ ]:


#arbitrary positional
def add_num(*m):
    print(m)
    print(sum(m))
add_num(1,2,3,4,5,6)


# In[ ]:


def shout(text):
    return text.upper()
def whisper(text):
    return text.lower()
def explain(func):
    greet=func("Higher order function")
    print(greet)
    
explain(shout)
explain(whisper)


# In[ ]:


#lambda function not applicable for list
def incr(x):
    x=x+1
    return x
print(incr(4))

print((lambda x:x+1)(4))
print((lambda x,y:x+y)(4,2))


# In[ ]:


li=[1,2,34,4,5]
def inc(num):
    return num+2
res_list=list(map(inc,li))
print(res_list)

print(list(map(lambda x:x+2,li)))


# In[ ]:


def eor(num):
    if num%2==0:
        print("even")
    else:
        print("odd")
eor(99)



# In[ ]:


l=[22,45,34,77,89,90]
list(map(eor,l))


# In[ ]:


#filter

def odd_num(n):
    if n%2!=0:
        return n
myl=[1,2,3,4,5]
print(list(filter(odd_num,myl)))


l6=[1,23,4,5,6,2]
temp=list(filter(lambda x:x%2==0,l6))
print(temp)


# In[ ]:


#modules
import os
os.mkdir("hi")
os.chdir("hi")
os.getcwd()
os.listdir()
#os.rmdir()


# In[ ]:


import math as m
print(m.pi)
print(m.e)
print(m.sqrt(4))


# In[ ]:


import sys 
print(sys.path)
print(sys.version)
print(sys.maxsize)


# In[ ]:


import statistics as st
print(st.mean([23,45,65,45]))
print(st.median([1,2,4,3,5,6]))
print(st.mode([1,2,3,1,1]))


# In[ ]:


import random as r
print(r.randrange(1,50))
print(r.randint(1,100))
print(r.random())


# In[ ]:


import random
gn=random.randint(1,10)
gn2=int(input("guess the number"))
if gn2==gn:
    print("party")
else:
    print("hello")


# In[ ]:


class co:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
obj=co()
print(obj.add(2,3))
print(obj.sub(5,6))


# In[ ]:


#inheritance
class Animal:
    def animal_sounds(self):
        return "makes sound"
    def animal_eat(self):
        return "and eats"
class cat(Animal):
    def cat_sounds(self):
        return self.animal_sounds()+"\tmeow"
    def __str__(self):
        return "CAT"
    def cat_eat(self):
        return self.animal_eat()+"\tmouse"
catobj=cat()
print(catobj,catobj.cat_sounds(),catobj.cat_eat())


# In[ ]:


#exception
print(x)


# In[ ]:


try:
    print(x)
except NameError as ne:
    print("exception occured",ne)


# In[ ]:


class INVALIDAGE(Exception):
    pass
age=int(input("enter voter age"))

try:
    if age<18:
        raise INVALIDAGE
except INVALIDAGE:
    print("error due to invalid age")


# In[ ]:


#file management
f=open("sample.txt",'x')


# In[ ]:


f=open("sample.txt","w")
f.write("welcome to python")
f.close()


# In[ ]:


f=open("sample.txt","r")
print(f.read())
f.close()


# In[ ]:


f=open("sample.txt","r")
print(f.read(3))
print(f.tell())
print(f.seek(3))
print(f.seek(0))
print(f.readline())
print(f.readlines())


# In[ ]:


f=open("sample1.txt",'x')


# In[ ]:





# In[ ]:


import shutil
sfile="sample.txt"
dfile="sample1.txt"
shutil.copy(sfile,dfile)
f=open("sample1.txt","r")
print(f.read())
f.close()


# In[1]:


f1=open("file1.txt","x")
f2=open("file2.txt","x")
f1=open("file1.txt","w")
f1.write("Learning python")
f1.close()

f1=open("file1.txt","r")
temp=f1.read()
f1.close()

f2=open("file2.txt","w")
f2.write(temp)
f2.close()

f2=open("file1.txt","r")
temp=f2.read()
print(temp)
f2.close()


# In[ ]:


import pickle
myl=['a','b','c','d','e']
f3=open("f3.txt","wb")
pickle.dump(myl,f3)
f3.close()

#unpickle
pickle_off=open("f3.txt",'rb')
e=pickle.load(pickle_off)
print(e)


# In[ ]:


#regular expression
import re
pattern=r"COOKIE"
sequence="Cookie"
if re.match(pattern,sequence):
    print("matching")
else:
    print("not matching")


# In[ ]:




