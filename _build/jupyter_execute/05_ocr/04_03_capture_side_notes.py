#!/usr/bin/env python
# coding: utf-8

# # <center>Finding and Isolating Marginalia</center>

# In[3]:


import pytesseract
import cv2


image = cv2.imread('data/sample_mgh_2.jpg')
base_image = image.copy()

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7,7), 0)
thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

# Create rectangular structuring element and dilate
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,25))
dilate = cv2.dilate(thresh, kernel, iterations=1)

# Find contours and draw rectangle
cnts = cv2.findContours(dilate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
cnts = sorted(cnts, key=lambda x: cv2.boundingRect(x)[1])
main_text = ""
for c in cnts:
    x,y,w,h = cv2.boundingRect(c)
    if h > 200 and w > 250:
        roi = base_image[y:y+h, 0:x]
#         cv2.rectangle(image, (0, y), (x, 0 + h+20), (36,255,12), 2)
        
        constant= cv2.copyMakeBorder(roi.copy(),30,30,30,30,cv2.BORDER_CONSTANT,value=[255,255,255])
        ocr_result = pytesseract.image_to_string(constant)
        cv2.imwrite("temp/output.png", roi)
        
        print (ocr_result)
#         print (ocr_result)
# cv2.imwrite("temp/output.png", image)


# In[2]:


ocr_result = pytesseract.image_to_string(img)


# In[ ]:


print (ocr_result)


# In[ ]:


lines = ocr_result.split("\n\n")


# In[ ]:





# In[ ]:


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




