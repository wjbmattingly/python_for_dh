#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
from PIL import Image


# In[2]:


img_file = "data/page_01.jpg"
no_noise = "temp/no_noise.jpg"


# In[3]:


img = Image.open(no_noise)
display(img)


# In[4]:


ocr_result = pytesseract.image_to_string(img)


# In[5]:


print (ocr_result)


# In[ ]:




