#!/usr/bin/env python
# coding: utf-8

# # <center>Advanced Filter and Querying</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) How and When to use the Filter() Function<br>
# 2) How and When to use the Query() Function<br>

# ## Introduction

# In this chapter, we will meet two advanced ways of filtering or searching (querying) our data. These are aptly named Filter() and Query() functions. These two functions allow us to do some fairly advanced things within a narrow scope. By narrow scope, I mean the questions that we want to pose. Whenever you are manipulating or probing data, it is always best to think about the task as simply asking a question. In essence, this is precisely what you are doing. You are asking the database a question. In order to ask the question correctly, as is the case with any language, you need to know the correct syntax and when that particular question is the right one to ask. In this chapter, we explore how to frame specific questions with Filter() and Query().
# 
# Each function is used in particular circumstances. Filter() is useful for getting a large data down to a smaller size, based on the questions you want to ask. Query(), on the other hand, is useful for phrasing questions that use comparison operators (less than, equal to, greater than, etc.). Let's explore each in turn, but first, let's import our Titanic dataset.

# In[1]:


import pandas as pd
df = pd.read_csv("data/titanic.csv")
df


# ## The Filter Function

# The filter function is a great way to grab only the relevant columns. The syntax of filter is a bit easier to use. It takes a single argument, a list of strings. These strings correspond to the columns.
# 
# **When to use Filter()**<br>
# Use filter() when you want to get a quick sense of your dataset or, as we shall see, create a new dataframe based on the columns you want. It is particularly useful if your dataset has many columns. You can also use it to reorder your columns in a more desired way.
# 
# Let's say that we are interested in just studying the names of the passengers of the Titanic. It does not make sense to work with the entire DataFrame. We can, therefore, use filter to just grab the names column, like so.

# In[2]:


df.filter(["Name"])


# This is great, but what if I also want to see the ages of these passengers. No problem. I can add an additional column to the list.

# In[3]:


df.filter(["Name", "Age"])


# What if I want age to come before name? I can rearrange the order.

# In[4]:


df.filter(["Age", "Name"])


# Note that we are not bound to the order of the DataFrame. This is particularly useful if we want to make a new DataFrame.

# In[5]:


new_df = df.filter(["Age", "Name"])
new_df


# Now, we can only examine the data that we actually need. This will make our code faster and require examining fewer data for each row. Filter's big limitation is in the fact that it cannot filter the data further. We cannot, for example, add an extra argument to filter() that would only return the Names with "Miss.", but we can tack on additional arguments to filter, such as those that we saw in the previous chapter on searching strings.
# 
# Let's try that now.

# In[6]:


df.filter(["Age", "Name"]).Name.str.contains("Miss.")


# Note that we now have a list of True False statements. These tell us if the word "Miss." is in the column Name. If it is there, we see a True. If it is not, we see a False. Let's say we want to know how many passengers have the title "Miss.", we stack .value_counts() into the chain. Note the plural of counts.

# In[7]:


df.filter(["Age", "Name"]).Name.str.contains("Miss.").value_counts()


# Now, let's say we were interested in ONLY seeing the rows that contain "Miss." in them. We need to structure that filtering as a list. But note that if we wrap the whole thing in a list, we don't filter out just the Age and Name columns. Instead, we get the entire DataFrame.

# In[8]:


df[df.filter(["Age", "Name"]).Name.str.contains("Miss.") == True]


# This is because of where our filter occurs in the chain of commands. Note that filter occurs within the brackets where we are setting up our parameters. This means that we are filtering under the conditions of how the list is created, but that once a row is processed, the DataFrame is unfiltered. If we want our filter to work, we need to place it after the conditions have been sorted. Notice that the filter is outside of our brackets now.

# In[9]:


df[df.Name.str.contains("Miss.") == True].filter(["Age", "Name"])


# ## The Query Function

# The Pandas Query() method is a fantastic way to filter and query data. Unlike other Pandas methods, it uses a string argument that functions rather similar to SQL syntax.
# 
# **When to use Query**<br>
# You should only use Query() when your question (query) can be posed as greater than, less than, equal to, or not equal to (or some combination of these). Let me demonstrate. If we wanted to filter out all the rows where the Pclass was equal to 3, we could use the following string.

# In[10]:


df.query("Pclass == 3")


# I can even stack questions together within this string. Let's say, I am interested in all who were in Pclass 3 and survived. I could write the following string argument.

# In[11]:


df.query("Pclass == 3 & Survived == 1")


# Let's make the question even more complex. I want to now find the number of these individuals who were over the age of 40.

# In[12]:


df.query("Pclass == 3 & Survived == 1 & Age > 40")


# I now have a list of 3 individuals who met all criteria. I can also use my Or operator (|), rather than &. Let's see if we can achieve what we want. (*Note this is an intentional mistake. Look below for why*).

# In[13]:


df.query("Pclass == 3 & Survived == 1 & Age > 40 | Age < 10")


# Woops! Something has gone seriously wrong here. We have all different kinds of Pclasses, not just 3s. We have people who survived and did not. And, most problematically, we have people only under the age of 10. What has gone wrong here!? The answer lies in a perhaps forgotten part of math from when we were children, the order of operations. If you recall from those lessons, the order of operations determines the way in which you process the problem. 4 + 7 x 2 is very different from (4+7) x 2. The former is 18 and the latter is 22 because the latter has parentheses which tell the reader to do that operation first. Because programming sits on top of mathematics (especially Boolean algebra), the syntax of mathematics is often embedded in programming.
# 
# Let's use the order of operations correctly and rephrase our query. Note the parentheses now before Age > 40 and after Age < 10. Note also that the & is before the parentheses.

# In[14]:


df.query("Pclass == 3 & Survived == 1 & (Age > 40 | Age < 10)")


# This is why query is such a powerful function in Pandas. You can do a lot with a single string. There are other ways to achieve this same result, but if your question cna be entirely phrased as a series of comparison operators (equal to, less than, etc.), then Query is likely the best option.
