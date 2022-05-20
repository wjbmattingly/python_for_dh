#!/usr/bin/env python
# coding: utf-8

# In[4]:


from PIL import Image
import pytesseract

image_file = "data/index_02.jpg"
img = Image.open(image_file)


# In[5]:


ocr_result = pytesseract.image_to_string(img)


# In[6]:


print (ocr_result)


# In[41]:


lines = ocr_result.split("\n\n")


# In[ ]:





# In[42]:


for line in lines:
    temp_line = line.replace(",", "")
    if temp_line.isdigit():
        pass
    else:
        components = []
        segs = line.split(",")
        for seg in segs:
            seg = seg.strip()
            num = False
            for character in seg:
                if character.isdigit():
                    num = True
            if num == False:
                components.append(seg)
        print (components)
        


# In[ ]:




