#!/usr/bin/env python
# coding: utf-8

# # <center>Time Series Data</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) How to Work with Time Series Data
# 2) How to Work with NaN in Time Series Data
# 3) How to Convert Floats and Ints into Time Series Data
# 4) How to Plot Time Series Data

# ## What is Time Series Data

# **Time series data** is data that reflects either time or dates. In Pandas this type of data is known as datetime. If you are working with time series data, as we shall see, there are significant reasons to ensure that Pandas understands that the data at hand is a date or a time. It allows for easily manipulation and cleaning of inconsistent data formatting. Let us consider a simple example. Imagine we were given dates from one source as 01/02/2002 and another as 01.02.2002. Both are valid date formats, but they are structured entirely differently. Imagine now you had a third dataset that organized the data as 2 January 2002. Your task is to merge all these datasets together.
# 
# If you wanted to do that, you could write out some Python and script them into alignment, but Pandas offers the ability to do that automatically. In order to leverage that ability, however, you must tell Pandas that the data at hand is datetime data. Exactly how you do that, we will learn in this chapter.
# 
# Time series data is important for many different aspects of industry and academia. In the financial sector, time series data allows for one to understand the past performance of a stock. This is particularly useful in machine learning predictions which need to understand the past to predict accurately the future. More importantly, they need to understand the past a sequence of data. In the humanities, time series data is important for understand historical context and, as we shall see, plotting data temporally. Understanding how to work with time series data, therefore, in Pandas is absolutely essential.

# ## About the Dataset

# In this chapter, we will be working with an early version of a dataset I helped cultivate at the *Bitter Aloe Project*, a digital humanities project that explores apartheid violence in South Africa during the 20th century. This dataset comes from Vol. 7 of the Truth and Reconciliation Commission's *Final Report*. I am using not our final, well-cleaned version of this dataset, rather an earlier version for one key reason. It contains problematic cells and structure. This is more reflective of real-world data, which will often times come from multiple sources and need to be cleaned and structured. As such, it is good practice in this chapter to try and address some of the common problems that you will encounter with time series data.

# In[1]:


import pandas as pd
df = pd.read_csv("data/trc.csv")
df


# As we can see, we have a few different columns which are relatively straight forward. In this notebook, however, I want to focus on Yr, which is a column that contains a single year referenced within the description. This corresponds to the year in which the violence described occurred. Notice, however, that we have a problem. Year is being recognized as a float (a number with a decimal place), or floating number. To confirm our suspicion, let's take a look at the data types by using the following command.

# In[2]:


display(df.dtypes)


# Here, we can see all the different columns and their corresponding data types. Notice that Yr has float64. This confirms our suspicion. Why is this a problem? Well, if we were to try and plot the data by year (see the bar graph below), we would have floating numbers in that graph. This does not look clean. We could manually adjust these years to have no decimal place, but that requires effort on a case-by-case basis. Instead, it is best practice to convert these floats either to integers or to datetime data. Both have their advantages, but if your end goal is larger data analysis on time series data (not just plotting the years), I would opt for the latter. In order to do either, however, we must clean the data to get it into the correct format.

# In[3]:


df['Yr'].value_counts().sort_index().plot.bar(figsize=(20,5))


# ## Cleaning the Data from Float to Int

# Let's first try and convert our float column into an integer column. If we execute the command below which would normally achieve this task, we get the following error.

# In[4]:


df['Yr'] = df['Yr'].astype(int)


# At the very bottom, we see why the error was returned. "IntCastingNaNError: Cannot convert non-finite values (NA or inf) to integer". This means that somewhere in our data, there are a few blank cells in the Year column. We need to fill in these blank cells. To do that, we can use the fillna function that we met earlier in this textbook.

# In[5]:


df = df.fillna(0)


# If we try and rerun our same command as above, you will notice we have no errors.

# In[6]:


df['Yr'] = df['Yr'].astype(int)


# Now, let's see if it worked by displaying the data types again.

# In[7]:


display(df.dtypes)


# Notice that Yr is now int32. Success! Now that we have the data in the correct format, let's plot it out. We can plot out the frequency of violence based on year by using value counts. This will go through the entire Yr column and count all the values identified and store them as a dictionary of frequencies.

# In[8]:


df['Yr'].value_counts()


# This looks great, but let's try and plot it.

# In[9]:


df['Yr'].value_counts().plot.bar(figsize=(20,5))


# What do you notice that is horribly wrong about our bar graph? If you noticed that it is not chronological, you'd be right. It would be quite odd to present our data in this format. When we are examining time series data, we need to visualize that data chronologically (usually). We can fix this, by adding sort_index().

# In[10]:


df['Yr'].value_counts().sort_index()


# Notice that we have now preserved the value counts, but organized them in their correct order. We can now try plotting that data.

# In[11]:


df['Yr'].value_counts().sort_index().plot.bar(figsize=(20,5))


# We have a potential issue, however. That first row, 0, is throwing off our bar graph. What if I didn't want to represent 0, or no date, in the graph. I can solve this problem a few different ways. Let's first create a new dataframe called val_year.

# In[12]:


val_year = df["Yr"].value_counts().sort_index()
val_year


# With this new dataframe, I can simply start at index 1 and then graph the data. Notice that the 0 value is now gone.

# In[13]:


val_year.iloc[1:].plot.bar(figsize=(20,5))


# Although we have been able to now plot our time series data chronologically, Pandas has not seen this as a datetime type. Instead, it has viewed these years solely as integers. In order to work with the years as time series data formally, we need to convert the integers into datetime format.

# ## Convert to Time Series DateTime in Pandas

# Our goal here will be to create a new column that will store Yr as a datetime type. One might think that we could easily just convert everything to datetime. Normally the following command would work, but instead we get this error.

# In[14]:


df['Dates'] = pd.to_datetime(df['Yr'], format='%Y')


# Just as the NaN cells plagued us above, so too has the 0s that we filled them with. Fortunately, we can fix this issue by passing the keyword argument errors="coerce".

# In[15]:


df['Dates'] = pd.to_datetime(df['Yr'], format='%Y', errors="coerce")


# In[16]:


display(df.dtypes)


# And like magic, we have not only created a new column, but notice that it is in datetime64[ns] format. We should also understand the keyword argument passed here, format. Format takes a formatted string that will tell Pandas how to interpret the data being passed to it. Because our integer referred to a single year, we use %Y. Let's try and plot this data now to see how it looks.

# In[17]:


df['Dates'].value_counts().sort_index().plot.bar(figsize=(20,5))


# While this data is now plotted as Pandas-structured time series data, it does not look good. Our dates are rendered in the long, full format that has both the date (in its entirety) and the time. Let's fix this by first, extracting the relevant data. In this case, the year and the counts.

# In[18]:


new_df = df['Dates'].value_counts().sort_index()
new_df


# Next, we need to convert that data into a new DataFrame.

# In[19]:


new_df = pd.DataFrame(new_df)
new_df.head()


# Now that we have that new DataFrame created, let's fix our column name and change Dates to ViolentActs.

# In[20]:


new_df = new_df.rename(columns={"Dates": "ViolentActs"})
new_df.head()


# With the new DataFrame, we can also fix the index so that it is strictly the year. Because Pandas knows that the index is a datetime type, then we can use the extra method, year, to grab just the year.

# In[21]:


new_df.index = new_df.index.year
new_df.head()


# Notice that our data is now just the year, the only piece of data in the time series data that matters to us. With that new DataFrame in the correct format, we can now plot it.

# In[22]:


new_df.plot.bar(figsize=(20,5))


# And thus we have successfully plotted our datetime data after properly formatting it in Pandas. While working with time series data in Pandas as a datetime can be a bit more complex in the beginning, it allows for you to more advanced things, such as we saw above by calling the year with .year. As we will see in the next few chapters, there are other advantages as well.
