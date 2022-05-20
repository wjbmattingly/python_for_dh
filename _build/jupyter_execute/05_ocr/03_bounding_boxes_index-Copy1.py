#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pytesseract
import cv2


# In[2]:


image = cv2.imread("data/index_02.JPG")
base_image = image.copy()


# In[3]:


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


# In[4]:


cv2.imwrite("temp/index_gray.png", gray)


# In[5]:


blur = cv2.GaussianBlur(gray, (7,7), 0)


# In[6]:


cv2.imwrite("temp/index_blur.png", blur)


# In[7]:


thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


# In[8]:


cv2.imwrite("temp/index_thresh.png", thresh)


# In[9]:


kernal = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 13))


# In[10]:


cv2.imwrite("temp/index_kernal.png", kernal)


# In[11]:


dilate = cv2.dilate(thresh, kernal, iterations=1)


# In[12]:


cv2.imwrite("temp/index_dilate.png", dilate)


# In[13]:


cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


# In[14]:


cnts = cnts[0] if len(cnts) == 2 else cents[1]


# In[15]:


cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[0])


# In[20]:


results  = []
for c in cnts:
    x, y, w, h = cv2.boundingRect(c)
    if h > 200 and w > 20:
        roi = image[y:y+h, x:x+h]
        cv2.rectangle(image, (x, y), (x+w, y+h), (36, 255, 12), 2)
        ocr_result = pytesseract.image_to_string(roi)
        ocr_result = ocr_result.split("\n")
        for item in ocr_result:
            results.append(item)
cv2.imwrite("temp/index_bbox_new.png", image)


# In[21]:


print (results)


# In[31]:


entities = []
for item in results:
    item = item.strip().replace("\n", "")
    item = item.split(" ")[0]
    if len(item) > 2:
        if item[0] == "A" and "-" not in item:
            item = item.split(".")[0].replace(",", "").replace(";", "")
            entities.append(item)


# In[32]:


print (entities)


# In[33]:


entities = list(set(entities))


# In[34]:


print (entities)


# In[35]:


entities.sort()


# In[36]:


print (entities)


# In[ ]:




