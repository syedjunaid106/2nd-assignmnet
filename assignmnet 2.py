#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np


# In[3]:


import numpy as np
arr = np.array([0, 1, 2, 3, 4 , 5, 6, 7, 8, 9])
arr = arr.reshape((2,5))
print(arr)


# In[4]:



arr1 = np.array([[0, 1, 2, 3, 4],
                [5, 6, 7, 8, 9]])
arr2 = np.ones((2,5))
arr3 = np.vstack((arr1,arr2))
arr3 = arr3.astype('int32')
print(arr3)


# In[5]:


arr4 = np.hstack((arr1,arr2))
arr4 = arr4.astype('int32')
print(arr4)


# In[6]:


arr = arr.flatten()
print(arr)


# In[7]:


arr5 = np.array([
    [ 0, 1, 2],
    [ 3, 4, 5],
    [ 6, 7, 8],
    [ 9, 10, 11],
    [12, 13, 14]
])
arr5 = np.ravel(arr5)
print(arr5)


# In[8]:


arr5.reshape(5,3)


# In[9]:



arr6 = np.random.randint(1,25, size = (5,5))
print("Original Array: \n")
print (arr6)
print("\n")
print("Square of Array: \n")
print(arr6 ** 2)


# In[10]:


arr8 = np.random.randint(1,20, size = (5,6))
print("Original Array: \n")
print (arr8)
print("\n")
print("Mean of Array: \n")
print(arr8.mean())


# In[11]:


print("Original Array: \n")
print (arr8)
print("\n")
print("Standard deviation of Array: \n")
print(np.std(arr8))


# In[12]:


print("Original Array: \n")
print (arr8)
print("\n")
print("Median of Array: \n")
print(np.median(arr8))


# In[13]:


print("Original Array: \n")
print (arr8)
print("\n")
print("Transpose of Array: \n")
print(np.transpose(arr8))


# In[14]:


arr7 = np.random.randint(1,20, size = (4,4))
print("Original Array: \n")
print (arr7)
print("\n")
print("Sum of diagonal elements of Array: \n")
print(np.trace(arr7))


# In[15]:



print("Original Array: \n")
print (arr7)
print("\n")
print("Determinant of Array: \n")
print(np.linalg.det(arr7))


# In[16]:


print("Original Array: \n")
print (arr7)
print("\n")
print(f"5th percentile of array: {np.percentile(arr7, 5)}")
print(f"95th percentile of array: {np.percentile(arr7, 95)}")


# In[17]:


np.isnan(arr7).any()


# In[ ]:




