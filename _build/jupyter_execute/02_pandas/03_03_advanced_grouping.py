#!/usr/bin/env python
# coding: utf-8

# # <center>Advanced Grouping with Groupby()</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) What is the Purpose of Groupby()<br>
# 2) What are Pandas Group Objects<br>
# 3) How to Analyze Group Objects Quantitatively<br>
# 4) How to work with Multiple Groupings at Once<br>

# ## Introduction

# When working with large quantities of data, it can sometimes be a bit difficult to understand broad patterns within your data. Often, you will need to group your data into small subsections based on some parameter, such as age, name, or some other feature. You can do this in Pandas using groupby(), which will be the main subject of this chapter. **Groupby** is a feature of Pandas that returns a special groupby object. This object can be called to perform different types of analyses on data, especially when leveraging the built-in quantitative features of Pandas, such as count() and sum(). In this chapter, we will explore these features and see how they can be used on a real-world dataset, the Titanic dataset.

# In[1]:


import pandas as pd
df = pd.read_csv("data/titanic.csv")
df


# ## Groupby()

# The groupby() function allows us to easily group our data in the DataFrame. Once your data are grouped, there are a lot of quantitative questions you can begin to ask. Let's start simple. Let's group our DataFrame by Sex.

# In[2]:


df.groupby("Sex")


# This output may not be quite what you expect. This is an object to which we can now pose targeted questions. Let's try and see a DataFrame that only has "male" in the Sex column. We can do that by using get_group("male")

# In[3]:


df.groupby("Sex").get_group("male")


# This argument does not have to be a string. Let's say, we want to just get all the people who are aged 20. We can do the same thing by grouping the dataset by "Age" and then getting the group of 20 year olds.

# In[4]:


df.groupby("Age").get_group(20)


# ## Quantitative Analysis with Count() and Sum()

# This is typically not how you would use the grouby function. It is far more powerful and often used for quantitative analysis on subsets of your data. Let's say that I want to examine my dataset by sex and I am interested in known the quantity of column based solely on the metric of sex. I could use groupby() and .count(). When chained together, our question then becomes, how many PassengerId, Survived, Pclass, Name, etc. do we see for each column based on sex. While this question is particularly useful for the qualitative rows (such as Name) or numerical strings (such as PassengerId) because they display the total number of passengers because each person has a unique PassengerId and Name.

# In[5]:


df.groupby("Sex").count()


# For the quantitative rows, we can use sum() function. This will tell us the sum of all the columns that have floats or integers. Note that this is not a really good question to pose for the Age column. It is, however, very useful for the Fare column and the Survived Column. Remember, if a person survived, they have a 1; if they did not, they have a 0. We can use the sum to know how many male vs. female survivors there were.

# In[6]:


df.groupby("Sex").sum()


# Let's say, though, that we are only interested in the Fare column. Before we add sum to our chain, we can specify that we want specifically the Fare column.

# In[7]:


df.groupby("Sex").Fare.sum()


# ## Working with Multiple Groups

# Now, we have just the data on a single column. We can see that the combined fare of male passengers was greater than the combined sum of female passengers. Let's say though that we are interested in how these sums divide over Pclass. We can pass a list to groupby, rather than just a string. This list will be a list of a strings that correspond to columns.

# In[8]:


df.groupby(["Sex", "Pclass"]).Fare.sum()


# The result of this new question is more nuanced. We are not looking at the sum of all fares, rather the sum of fares divided on a Pclass-by-Pclass basis. This means that we can now understand that these sums varied by class. For example, while the total fare for male passengers was greater, the total fare for first class female passengers was greater than their first class male counterparts. The male fare, however, is greater for both the 2nd Class and 3rd Class groups.

# ## Groupings with Many Subsets

# What if we were interested in something that would have more than just 6 neat subsections, such as 3 classes per sex. What if we also wanted to add another aspect to the groups, such as age. If we try and do that, our results are cutoff. We can try and use pd.set_option()

# In[9]:


df.groupby(["Sex", "Pclass", "Age"]).Fare.sum()


# In order to print off this many rows, we need to increase the amount of data Pandas will display. We can use the pd.set_options() command and pass an argument to display 1000 rows.

# In[10]:


pd.set_option('display.max_rows', 1000)
df.groupby(["Sex", "Pclass", "Age"]).Fare.sum()


# What if we wanted to make this look a bit nicer, as a Pandas DataFrame? We can pass all our data back into a new DataFrame object.

# In[11]:


df = pd.DataFrame(df.groupby(["Sex", "Pclass", "Age"]).Fare.sum())
df


# This is now a bit easier to read. You should now have a fairly good understanding of how to group data in Pandas using groupby() and some of the more powerful ways you can use groupby() to manipulate quantitative data.
