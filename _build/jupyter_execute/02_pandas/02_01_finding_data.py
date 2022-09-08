#!/usr/bin/env python
# coding: utf-8

# # Pandas Textbook for Digital Humanities

# ## Chapter Three: Finding Data in DataFrame

# ## Covered in this Chapter

# 1) How to Find Column Names<br>
# 2) How to Get a Quick Sense of the Dataset<br>
# 3) How to Grab a Specific Range of Rows<br>
# 4) How to Get a Quick Quantitative Understanding of the Dataset<br>
# 5) How to Find Specific Information in the Dataset<br>
# 6) How to use Or in a DataFrame query<br>

# ## Video

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<center>\n<iframe width="560" height="315" src="https://www.youtube.com/embed/IFVkOCnH_Qs" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</center>')


# ## About the Titanic Dataset

# In[1]:


import pandas as pd


# <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/f/fd/RMS_Titanic_3.jpg/1200px-RMS_Titanic_3.jpg">

# In the next two notebooks, we will be using the same dataset, the infamous *Titanic Survivor* dataset that was put out by Kaggle a few years ago. It has since become a staple dataset in machine learning and data science communities because of the breadth of data that it offers on the Titanic passengers. The goal of most machine learning challenges is to use this dataset to train a model that can accurately predict if a passenger would have survived given certain gender, economic, and class conditions.
# 
# In these notebooks, we will be using a cleaned version of the dataset available on the GitHub page below. We will be using it because of its breadth of its qualitative and quantitative data.
# 
# In this notebook, we are strictly interested in finding key data in the DataFrame. By the end of the notebook, you should have a good understanding of why working with CSV data in Python via Pandas is far more powerful and easy than using Excel.

# In[2]:


#data obtained from => https://github.com/datasciencedojo/datasets , but originally from Kaggle
df = pd.read_csv("data/titanic.csv")


# ## How to Find Column Data

# Let's presume that we just obtained this dataset. Let's also presume we know nothing about it. Our first job is to get a sense of the data. Maybe we want to know all the columns that the dataset contains. To find this information, we can use df.columns

# In[3]:


df.columns


# With our knowledge from the last notebook, we now know how to convert this into a list!

# In[4]:


cols = df.columns.tolist()


# In[5]:


cols


# ## How to Get a Quick Sense of the Dataset with df.head()

# Another way to get a quick sense of the data is to use df.head(). This allows us to return to top pieces of information from the dataset. By default, head returns the top 5 rows.

# In[6]:


df.head()


# We can pass in an argument to return more than 5. Let's try and display 20.

# In[7]:


df.head(20)


# ## How to Grab a Specific Range of Rows with df.iloc[]

# Sometimes, however, you need to grab a specific range of rows. Let's say I am interested in rows 5-20. To grab this data, we can use the df.iloc[] command that we met in the last notebook. This will allow us to pass a specific index range like a list.

# In[8]:


df.iloc[5:20]


# ## How to Get a Quick Quantitative Understanding of the Dataset with Describe()

# When working with numerical, quantitative data, we can automatically grab all numerical rows and learn a lot about the data with df.describe(). This will return the count, mean, standard deviation, minimum, maximum, etc. of our quantitative data. Sometimes, this data is useful to compute in such a way, such as the column Survived. Here, we can see that roughly .38 or 38% of the passengers (in this dataset) survived. Other numerical data does not really lend itself well to this kind of analysis, e.g. PassengerId which a unique numerical number corresponding to each passenger.

# In[9]:


df.describe()


# ## How to Find Specific Information in the Dataset with df.loc

# As researchers, however, we often need to find targeted information in our dataset. Let's say I am researching female passengers on the Titanic. I can achieve this fairly easily in Excel and in Python with Pandas. To do this in Pandas, you can use df.loc[] to pass a specific argument. In the example below, we are stating that we are looking for the columns in the DataFrame of "Sex" that match the string "female". Try to recreate this and find all males in the dataset on your own. Note at the bottom of the DataFrame 314x12. This is the dimensions of the DataFrame. We can see that we have 314 results. 

# In[10]:


df.loc[df["Sex"] == "female"]


# But that's not all df.loc[] can do. We can add multiple arguments to our search query here, rather like SQL. In the example below, note the addition of the parentheses around df\["Sex"\] == "female" this denotes one parameter of our search. We then use the & to add a second parameter. In this case, we are interested in not only returning those that are female, but also those who are in Pclass, or Passenger Class 1, i.e. First Class. When we execute the command below, we see that we have found 94 results.

# In[11]:


df.loc[(df["Sex"] == "female") & (df["Pclass"] == 1)]


# Let's say now we are interested in only finding those that did not survive of the 94. To do that, we would simply add a third argument to our query. We ask Pandas to only show those whose Survived value is 0, or False. In other words, we are seeking to find those who did not survive.

# In[12]:


df.loc[(df["Sex"] == "female") & (df["Pclass"] == 1) & (df["Survived"] == 0)]


# With this data, I not only have qualitative information about each passenger, I also have some significant quantitative information as well. I know that of the 314 people in the dataset with the sex of female, 94 were in first class and of those 94, all survived except 3. Let's now pose a question and I think you may already know the answer. Did class in any way play a role in the chance off survival on the Titanic. We don't need a fancy machine learning algorithm to help us answer this question. We can simply examine the results from our query. Let's find the total number of passengers that are identified as female, but not in first class, and then find the number of those who did not survive.

# In[13]:


df.loc[(df["Sex"] == "female") & (df["Pclass"] > 1)]


# In[14]:


df.loc[(df["Sex"] == "female") & (df["Pclass"] > 1) & (df["Survived"] == 0)]


# As we can see, we have 220 total people identified as female with 78 not surviving. We can perform some quick calculations to understand better our results.

# In[15]:


x = 3/94
x


# In[16]:


y = 78/220
y


# In this case, x is the death rate for a first class female, whereas y is the death rate for those not in first class and female. The result is clear. The chance for survival was significantly greater for those identified as female if they were in first class, roughly 32.5% difference. Were there other factors at play, possibly. But that is beyond the point here. I am simply trying to illustrate how to obtain data to begin framing the research question at hand.
# 
# Although we can achieve this same analysis in Excel, doing this in Python allows us to leverage the power of an entire programming language with the data at hand. This is a simple example of the power of Pandas over Excel. As we move forward in the next notebooks, you will see more examples of this.

# ## How to Query with "OR" (|) on a DataFrame

# Above we saw how to use df.loc to structure logical arguments for finding two specific conditions with "&". This indicated that both conditions must be true to be returned as a result. In case you don't remember it, it looked like this:

# In[17]:


df.loc[(df["Sex"] == "female") & (df["Pclass"] > 1)]


# We can do the same conditional approach, but rather than using and, we can also tell Pandas "Or" with the "|", that vertical character you probably never use located above the "Enter" button on a standard American keyboard. Let's try and grab all first and second class passengers. We can specify if the Pclass is either 1 OR 2.

# In[18]:


df.loc[(df["Pclass"] == 1) | (df["Pclass"] == 2)]

