#!/usr/bin/env python
# coding: utf-8

# # <center>Organizing the DataFrame</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) How to Sort Data by Single Column<br>
# 2) How to Reverse Sort Data by Single Column<br>
# 3) How to Sort Data by Multiple Columns<br>
# 4) How to Sort Data by Multiple Columns with Different Values Organized Differently<br>

# ## Video

# In[1]:


get_ipython().run_cell_magic('HTML', '', '<center>\n<iframe width="560" height="315" src="https://www.youtube.com/embed/1G1ursLeZNg" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</center>\n')


# ## How to Sort Data By Single Column

# In[1]:


import pandas as pd
df = pd.read_csv("data/titanic.csv")


# Now that we've import pandas and created our DataFrame, let's see what it looks like again.

# In[2]:


df


# In this scenario, I am interested in sorting the data (rather like Excel). Rather than using the sort feature in Excel, we can use the df.sort_values() method in Python. This will take one argument, specifically the column that you want to organize by. By default, this will be ascending. Let's do this by class. In other words, sort the DataFrame so that those who were in first class appear first and those in third class appear last. We will do this by passing the argument "Pclass", the column name corresponding to Passenger Class.

# In[3]:


df.sort_values("Pclass")


# ## How to Reverse Sort Data by Single Column

# As we can see, our data is now appearing as expected. We can pass additional keyword arguments to sort the data in the opposite direction, or descending by setting ascending to False. See the example below.

# In[4]:


df.sort_values("Pclass", ascending=False)


# ## How to Sort Data by Multiple Columns

# Again, we can see the power of Pandas over Excel by the simplicity of altering our command to include multiple columns. Let's say that we want to sort all the data by Pclass, then we want that data organized again by sex, so that all male and female passengers appear in order. We can do this by passing the argument of what we want organized as a list. Note the order of the list as well. The columns that appear earlier in the list correspond to those that receive primacy in the ascending. In other words, we organize by passenger class firsit, then sex. In this case, the method head, is simply showing the top 100 rows.

# In[5]:


df.sort_values(["Pclass", "Sex"]).head(100)


# As with before, we can control how the data is sorted, either ascending or descending. If we set ascending to False, we organize all items in the list by this method. We can do this with the sample code below.

# In[6]:


df.sort_values(["Pclass", "Sex"], ascending=False)


# ## How to Sort Data by Multiple Columns with Different Values Organized Differently

# What if we want to organize the data differently. By this I mean, we want for all the data to be organized by passenger class first and for that data to be ascending (1, 2, 3), but we want the sex of the passengers to be organized descending (male, female, rather than female, male). To achieve this, we can pass a list to ascending with 0s and 1s. 0 is False and 1 is True.

# In[7]:


df.sort_values(["Pclass", "Sex"], ascending=[1,0])


# What is particularly nice about Pandas over Excel is that this operation scales nicely. If we want to add more methods of sorting, we can do that too by simple increasing the indices of our lists. Always make sure that the length of your lists match, however. In other words, do not have 3 attributes to sort by and 2 items in your ascending list. In this case, we want to organize by passenger class, sex, and age with passenger class ascending, sex descending, and age ascending. Let's see what that would look like.

# In[8]:


df.sort_values(["Pclass", "Sex", "Age"], ascending=[1,0,1])


# As we move forward throughout this textbook, we will explore more robust ways to sort and organize our data. For now, you should feel comfortable with how to use sort_values() to do fairly robust tasks quickly.

# In[ ]:




