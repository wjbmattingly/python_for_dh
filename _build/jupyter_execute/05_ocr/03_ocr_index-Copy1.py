#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
from PIL import Image


# In[2]:


image_file = "data/index_02.JPG"
img = Image.open(image_file)


# In[3]:


ocr_result = pytesseract.image_to_string(img)


# In[4]:


print (ocr_result)


# In[ ]:





# In[ ]:





# In[ ]:




