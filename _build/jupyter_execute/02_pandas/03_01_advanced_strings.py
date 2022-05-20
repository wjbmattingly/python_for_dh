#!/usr/bin/env python
# coding: utf-8

# # <center>Advanced Searching on Strings</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) How to find Strings with Specific Features<br>
# 2) Finding Strings without Certain Features<br>
# 3) Larger Pandas Queries with RegEx<br>

# ## Finding Features within a String

# In[1]:


import pandas as pd
df = pd.read_csv("data/titanic.csv")
df


# When I am looking at the df, I notice that there is a "Rev." in index 886. As a historian, I find this fascinating. Now, I start to wonder, how many reverends were there on the Titanic? Is this individual unique? If I wanted to ask this question outside of Pandas, I could do the following:

# In[2]:


names = df.Name.tolist()
revs = []
for name in names:
    if "Rev." in name:
        revs.append(name)
print (revs)


# Sure, that works, but I don't have any of the other data associated with each of these reverends. I would have to then do some manual searching in the DataFrame to find their corresponding data, or save the data as a dictionary and then run look ups. But why do all of that, when we can do it in a single line of code using Pandas' built-in function. We can use  .str.contains() which takes an argument of what we want to return.

# In[3]:


df.loc[df["Name"].str.contains("Rev.")]


# We can, therefore, see not only the reverends, but also their corresponding data.

# ## Finding Strings that Don't Contain Feature

# What if we wanted to eliminate all names that do not contain "Rev."? We can introduce "~" prior to df to specify that the Names column should not have whatever condition we express.

# In[4]:


df.loc[~df["Name"].str.contains("Rev.")]


# ## Using RegEx with Pandas

# Out of the box, Pandas supports RegEx. RegEx stands for Regular Expressions. It is a powerful way of performing complex string matching. If we were interested in finding any instance of "Rev." or "Mr.", we would have to write something like this without RegEx:

# In[5]:


df.loc[(df["Name"].str.contains("Rev.")) | (df["Name"].str.contains("Mr."))]


# While this works, imagine if we had 20 or 30 different conditions! That would be a very long piece of code to write and while it would work, it is always best practice to write shorter, tighter code. So, let's do the same thing, but with RegEx. We can add the Or-condition into the str.contains() argument. This is a RegEx command. To ensure that RegEx is registered, it may be necessary to pass it as an argument.

# In[6]:


df.loc[df["Name"].str.contains("Rev.|Mr.", regex=True)]


# In some instances, we may have uncleaned data and the use of "Rev." may be lowercase in one instance. To ensure that we grab both upper and lowercase forms of this sequence, let's ignore the case by using the case keyword and setting it to False.

# In[8]:


import re
df.loc[df["Name"].str.contains("Rev.|Mr.", case=False, regex=True)]


# In[ ]:




