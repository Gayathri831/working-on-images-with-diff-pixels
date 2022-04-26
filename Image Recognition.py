#!/usr/bin/env python
# coding: utf-8

# In[18]:


import numpy as np


# In[2]:


import cv2


# In[3]:


img1 = cv2.imread('C:/Users/gayat/OneDrive/Pictures/gayathri image.jpg 1.jpg')


# In[4]:


h,w,bpp = np.shape(img1)


# In[5]:


img_gray = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)


# In[6]:


img2=cv2.merge((img_gray,img_gray,img_gray))


# In[7]:


th1, img3 = cv2.threshold(img2, 127, 255, cv2.THRESH_BINARY)


# In[8]:


img4 = cv2.resize(img1,None,fx=0.1, fy=0.1, interpolation = cv2.INTER_AREA)


# In[9]:


img4 = cv2.resize(img4,None,fx=10, fy=10, interpolation = cv2.INTER_AREA)


# In[10]:


img5 = cv2.GaussianBlur(img1,(9,9),10)


# In[11]:


img6 = cv2.cvtColor(img1,cv2.COLOR_BGR2HSV)


# In[12]:


temp1 = np.concatenate((img1,img2,img3), axis=1)


# In[13]:


temp2 = np.concatenate((img4,img5,img6), axis=1)


# In[14]:


img_final = np.concatenate((temp1,temp2), axis=0)


# In[15]:


cv2.imshow("result",img_final)


# In[16]:


cv2.waitKey(0)


# In[17]:


cv2.destroyAllWindows()


# In[ ]:




