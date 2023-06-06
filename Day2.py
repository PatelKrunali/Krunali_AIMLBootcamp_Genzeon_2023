#!/usr/bin/env python
# coding: utf-8

# In[5]:


tup=(1,2,3,4)
tup2=("hi","good","genzeon",1.2)
tup3=("hello",tup,tup2)

print(tup3[2][0])
print(tup2[-3])
print(tup3[2][0:2])


# In[8]:


#tuple methods
print(tup.count(1))
print(tup.index(2))
print(max(tup))
print(min(tup))
print(len(tup))


# In[10]:


#set
s1={1,3}
s2={1,2,3,"hi",(1,2,3,4)}

l=[1,2,3,4]
s3=set(l)
print(s3)
s1.add(2)
print(s1)

s1.update([2,3,4])
print(s1)

s1.discard(4)
print(s1)

s1.remove(4) # give error if element is not present
print(s1)


# In[11]:


a={1,2,3,4}
b={4,5,6,7}
print(a|b)
print(a.union(b))
print(b.union(a))

print(a&b)
print(a.intersection(b))


# In[14]:


#dictionaries
dic={"name":"Krunali","id":33,"address":"pune"}
print(dic.keys())
print(dic.values())


# In[19]:


#string formats
name="genzeon"
language="python"
c="Trainees"

print(c,"are learning ",language,"programming at",name)
print("{} are learning {} programming at {}".format(c,name,language)) # format
print("{1} are learning {2} programming at {0}".format(c,name,language))

#placeholder
print("%s are learning %s programming at %s" %(c,language,name))

#rawstring
print(f"{c} are learning {language} at {name}")


# In[20]:


#decision making
var=10
if var>0:
    print("true")
    


# In[21]:


var1=-1
if var >0:
    print("true")
else:
    print("false")


# In[25]:


years=25
if(years < 5):
    print("free")
    if(years >=2 and years <=4):
        print("Hello")
    else:
        print("safe journey")
elif(years >= 5 and years <=10):
    print("20% off")
elif(years >=11 and years <=18):
    print("Half ticket")
else:
    print("full Ticket")


# In[26]:


#loops
list=[1,2,3,4,5,6,7,8]
sum=0
for i in list:
    sum +=i
print(sum)


# In[27]:


# tables using for and while loop
for i in range(1,10):
    print(i)


# In[50]:


for j in range(65,91):
    print(chr(j))


# In[34]:


num=int(input("enter the list of tables"))
i=1
while(i<=num):
    print(f"Table {i}")
    j=1
    while(j<11):
       print(f"{i}*{j}={i*j}")
       j=j+1
    print("____________________")
    i=i+1


# In[36]:


# control statement
for l in "python":
    if l=="h":
        break
    print(l)


# In[39]:


int1=10
while(int1>0):
    print(int1)
    int1=int1-1
    if int1==5:
        break


# In[40]:


for l in "python":
    if l=="h":
        continue
    print(l)


# In[41]:


for l in "python":
    if l=="h":
        pass
        print("pass block")
    print(l)


# In[ ]:




