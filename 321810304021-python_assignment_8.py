## 1.Write a Python program to get single string from two given strings,separated by a space and swap the first two characters of each string.

# In[1]:


def swap(a,b):
    new_a=b[:2]+a[2:]
    new_b=a[:2]+b[2:]
    return new_a+''+new_b
print(swap('abc','xyz'))


# ## 2.Write a Python program to remove a newline in python.

# In[2]:


str1='sai\n'
print(str1)
print(str1.rstrip())


# ## 3.Write a Python program to perform Deletion of a character.

# In[3]:


s1="apple"
print(s1)
print(s1[1:])


# ## 4.Write a program to print every character of a string entered by user in a new line using loop.

# In[4]:


s1="mango"
for i in s1:
    print(i)