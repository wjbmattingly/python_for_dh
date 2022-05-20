#!/usr/bin/env python
# coding: utf-8

# # Cleaning the DataFrame

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) How to Drop a Column in the DataFrame<br>
# 2) How to Remove Rows that have NaN in any Column<br>
# 3) How to Remove Rows that have NaN in a Specific Column<br>
# 4) How to Convert DataFrame Data Types (from Float to Int)

# ## How to Drop a Column in Pandas DataFrame

# In[1]:


import pandas as pd
df = pd.read_csv("data/titanic.csv")
df


# With our data loaded, let's go ahead and jump right into the chapter. Imagine that we have a large DataFrame, but we are not interested in a couple columns. This is especially import when your DataFrame has 10s or 100s of columns. In these instances, you need to examine the DataFrame without the useless data. Imagine that we wanted to study the Titanic data but knew that Parch and Ticket were categories that we did not need. We can use df.drop() to pass an argument to remove those specific columns.

# In[2]:


df.drop(columns=["Parch", "Ticket"])


# ## How to Remove Rows that have NaN in any Column

# One of the biggest problems in datasets is the absence of data. If you are training a machine learning model or just performing quantitative analysis, rows that have missing values, or NaN, can radically alter your results. It is often good practice to ignore that data or alter it in some way. Let's presume that we want to simply remove it from our dataset. To do that, we can use df.dropna() which will remove all rows that have any instance of NaN in any column.

# In[3]:


df.dropna()


# ## How to Remove Rows that have NaN in a Specific Column

# In some instances, though, we don't want to remove an entire row just because of NaN in one column. Maybe that column is not as important for quantitative analysis and we are not planning to include it in our analysis, but we still want to see it. A good example of this is the column Cabin which is a string or Age which is a float (we'll get to that in a moment). Let's say we want to remove all rows that have NaN in the Age column. We can use the command below.

# In[4]:


df2 = df[df["Age"].notna()]


# In[5]:


df2


# As we can see, the size of our DataFrame dropped from 891 rows to 714.

# ## How to Convert DataFrame Data Types (from Float to Int)

# In other instances, it may be important not to simply remove a column, but alter it into a different type of data. In this dataset, Age is a float. This is to account for infants who were below the age of 1 on the Titanic. Let's presume that we want to convert all these floats to integers. To do that we can use the .astype() method on a specific row.

# In[6]:


df2.Age = df2.Age.astype(int)


# In[7]:


df2


# Now our Age column is no longer a float, rather an integer.
