#!/usr/bin/env python
# coding: utf-8

# In[5]:


#1 methods of String

Str=" Genzeon "
print(len(Str))
print(Str.count("e"))
print(Str.strip()) # removes leading and trailing zeroes
print(Str.endswith("eon ")) # true if present else false

Str1="Pythononon"
print(Str1.replace("th","ht"))
print(Str1.find("on")) # returns lower index of occurance if found else -1
print(Str1.rfind("on"))
print(Str1.rindex("on"))
print(Str.upper())
print(Str.swapcase())
print("*".join(Str))


# In[34]:


#methods of list
List=["Krunali",14,(1,2,3),{"Location":"Pune"},3]
print(List)

List.append("June")
print(List)

List.insert(2,"Rainy")
print(List)

print(List.count(3))
print(List.count(1))
print(List.index(3))

print(List.pop()) # removes last element
print(List)

print(List.remove(14))
print(List)


# In[39]:


#methods of tuples
tup=(0,0,4,5,6,4,5,6,5,6)
print(tup.count(6))
print("First occurance of 4 is at index",tup.index(4))
tup1=([1,2],[1,2],1,"Hello","Hello",[1,2])
print(tup1.count([1,2]))


# In[51]:


#methods of dictionary
dictionary={1:"one",2:"two",3:"three",4:"four",5:"five"}
print(dictionary)

New_dictionary=dictionary.copy()
print(New_dictionary)

print(dict.fromkeys(New_dictionary,"Number")) # default value number

print(dictionary.get(1))
print(dictionary.get(6,"not found"))

dict1={1:{"one":"number"}}
print(dict1.get(1).get("one"))

print(dictionary.pop(5))
print(dictionary)


# In[78]:


#methods of set
set={"Good","Evening","Good"}
print(set)
type(set)
set.add("Morning")
print(set)
print(set.pop())
set.discard("Good")
print(set)
set.remove("Morning")
print(set)

set1={1,2,3,4,"Forest","Mountain",76}
set2={76,2,"Glaciers","Desert"}
set3={2,"Plateau"}
print(set1.difference(set2))
print(set2.difference(set1))


print(set1.union(set2))
print(set1 |  set2 | set3)

print(set1.intersection(set2))
print(set1.intersection(set2,set3))
print(set1 & set2)
print(set1 & set2 & set3)


print(set1.isdisjoint(set2))
print(set1.issubset(set2))


# In[52]:


#convert decimal to binary ,oct , hexa
decimal = int(input("Enter a number"))
binary = bin(decimal)
octal = oct(decimal)
hexadecimal = hex(decimal)
print("Decimal:", decimal)
print("Binary:", binary)
print("Octal:", octal)
print("Hexadecimal:", hexadecimal)


# In[53]:


#arithmetic operators
a=10
b=20
print(a+b)
print(a-b)
print(a*b)
print(a/b) # will give float answer 
print(a%b)
print(a//b) # will give int answer
print(a**b) #power


# In[61]:


#assignment operators
a=10
b=10
c=a+b
print(c)
c+=a
print(c)
c-+a
print(c)
c*=a
print(c)
c/=a
print(c)
c%=a
print(c)
c**=a
print(c)

a//=b
print(a)

a&=b
print(a)

a|=b
print(a)

a^=b
print(a)

a>>=b
print(a)

a<<=b
print(a)


# In[57]:


#comparision operators
a=10
b=20
print(a==b)
print(a!=b)
print(a>b)
print(a == b)
print(a<=b)


# In[63]:


#logical operators
a=80
b=90
print(a>8 and a<15)
print(a>4 or b<7)
print(not(a and b))


# In[62]:


#bitwise operators
a=11
b=12
print(a&b)
print(a|b)
print(a^b)
print(~a)#Not
print(a>>2)
print(a<<2)


# In[58]:


#membership operators
x="hello world"
y={1:'a',2:'b'}
print(y)

print('H' in x)
print(1 in y)
print('a' in y)


# In[59]:


#identity operators
x1=5
y1=5
x2="Hello"
y2="Hello"
x3=[1,2,3]
y3=[1,2,3]
print(x1 is not y1)
print(x2 is y2)
print(x3 is y3)


# In[97]:


#negative indexing for list and slicing
List1=[1,2,3,4,"Hello","World"]
print(List1[-1:0:-4])


# In[80]:


print('Welcome to Python training program'[3:10][::-1]) # took string from 3 to 9 then reversed
print('A series of characters designated as one object known as a string'[::-1][4::3]) # reversed and from 4 to end , alternate 3


# In[93]:


str="was it a car or a cat I saw"
print(str[::-1].upper())


# In[89]:


X=int(input("Enter Number"))
print(X*"Z"+(X*2)*"O")


# In[82]:


matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]+matrix2[i][j]


print(result)


# In[83]:


#need to explore more about numpy
import numpy as np

matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]

result=np.array(matrix1) + np.array(matrix2) 
print(result)


# In[84]:


matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]
result=[[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matrix1)):
    for j in range(len(matrix1[0])):
        result[i][j]=matrix1[i][j]-matrix2[i][j]


print(result)


# In[98]:


import numpy as n
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]

result=n.dot(matrix1,matrix2)
print(result)


# In[99]:


import numpy as n
matrix1=[[1,2,3],[4,5,6],[7,8,9]]
matrix2=[[1,2,3],[4,5,6],[7,8,9]]

result=n.multiply(matrix1,matrix2)
print(result)


# In[ ]:




