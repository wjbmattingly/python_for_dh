#!/usr/bin/env python
# coding: utf-8

# # <center>The Basics of Pandas</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) How to Create a DataFrame from a Dictionary<br>
# 2) How to Display a DataFrame<br>
# 3) How to Save a DataFrame to CSV<br>
# 4) How to Create a DataFrame from a CSV File<br>
# 5) How to Create a DataFrame from a JSON File<br>
# 6) How to Add a Column to a DataFrame<br>
# 7) How to Grab a Specific Column of a DataFrame<br>
# 8) How to Convert a Column to a List<br>
# 9) How to Grab a Specific Row of a DataFrame

# ## Video

# In[7]:


get_ipython().run_cell_magic('HTML', '', '<center>\n<iframe width="560" height="315" src="https://www.youtube.com/embed/dMoXe8DUQ7E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</center>\n')


# ## How to Create a DataFrame from a Dictionary

# As we noted in the last notebook, we need to first import pandas. To do that we will import pandas as pd.

# In[1]:


import pandas as pd


# With pandas now loaded correctly, we can begin to work with the library. Normally, you will create a Pandas DataFrame from a CSV or some external data file. We will see examples of that below. To begin, though, let's start with the basics. Below we have a dictionary. A good way to think of this dictionary is as an Excel Spreadsheet. Each key in the dictionary is a column and its value is a list which contains each cell in that column. We will see an example of a two-column dataset below, but for now let's work with the single column dataset, "names". In this column, we have a list of 6 names.

# In[2]:


names_dict = {"names":
        [
            "Tom",
            "Mary",
            "Jeff",
            "Rose",
            "Stephanie",
            "Rodger"
        ]}


# Normally in Python, we would work with this data as an object. I could do something like the following to get the value of names:

# In[3]:


print (names_dict["names"])


# But this is a textbook on Pandas and DataFrames. We want to do more! We want to work strictly with our data as a DataFrame. In order to do this, we need to convert the data into a Pandas DataFrame. To do that, we can use the line of code below. The pd.DataFrame can take numerous arguments. We won't get into all of them right now. For now, understand that there is one essential argument that you must pass: the data that you wish to convert into a DataFrame. In our case, we will be converting the single-column dictionary into a DataFrame, so we pass that object as the only argument. We can see this in the code below.

# In[4]:


df = pd.DataFrame(names_dict)


# ## How to Display a DataFrame

# Loading the data as DataFrame is not the end of our work. It is often times essential to view that data in a Jupyter notebook or terminal. To see what it looks like, you can use the following command.

# In[5]:


df


# Note that we are not printing off the data. This is because we are working within a Jupyter notebook. Were we working within an IDE, such as Atom, we would need to use the following command:

# In[6]:


print (df)


# Notice, however, that the formatting of the data in the output is a bit different. When we print off a DataFrame, we do not see the nice formatting, such as the row highlighting and column header emboldening. It is for these reasons, that I recommend using the command "df" rather than print (df)

# ## How to Save DataFrame to CSV

# Often times when you convert your data into a DataFrame, you will process it and then ultimately save it to disk. To do this, we have a few different options, such as CSV and JSON. We will meet this process with JSON a bit later. For now, let's focus on one file type: CSV, or comma separated value. To save your DataFrame to a CSV file, you can write the following command

# In[7]:


df.to_csv("data/names.csv")


# As we will see a little later, there are different arguments that you can pass here (and should!) For now, let's focus on that single argument that we used: a string. This string should correspond to the file that you want to create. In this case, we are putting it into the data subfolder under the name "names.csv".

# ## How to Read DataFrame from CSV

# Now that we have the data saved to a CSV file, let's create a new DataFrame, df2, and read that data. We can do this with the command pd.read_csv(). As with to_csv, we can pass multiple arguments here, but for now, we will stick with the one mandatory one, a string of the file that we wish to open. In this case, it is the same file we just created. Let's open it and print it off.

# In[8]:


df2 = pd.read_csv("data/names.csv")


# In[9]:


df2


# This doesn't look right. Notice that this DataFrame looks a bit off from what we saved to disk. Why is that? It is because of *how* we saved the file. If we don't specify an index, Pandas will automatically create one for us. In order to correctly save our file, we need to pass an extra keyword argument, specifically index=False. Let's try and save this file again under a different name: "names_no_index.csv".

# In[10]:


df.to_csv("data/names_no_index.csv", index=False)


# Let's create a new DataFrame, df3, and reopen and print off the data.

# In[11]:


df3 = pd.read_csv("data/names_no_index.csv")


# In[12]:


df3


# Like magic, now we have a DataFrame that represents our original data.

# ## How to Save DataFrame to JSON

# In Pandas, we are not limited to CSV files, we can do this same process with JSON files, which are JavaScript Object Notation files. These are a bit different from CSV files and are used to store more complex data, specifically data that is used on the web because all browsers can interpret JSON data off-the-shelf. To save our data to a JSON file, we can use the to_json(). Note that we are not passing the index argument here. When our data is stored as a JSON file this is not necessary.

# In[13]:


df3.to_json("data/names.json")


# Now, let's open that same data as a new DataFrame, df4. We can do the same thing as we did with the CSV file, except use read_json() and then print it off.

# In[14]:


df4 = pd.read_json("data/names.json")


# In[15]:


df4


# ## How to Add a Column to the DataFrame

# When working with DataFrames, you will almost always need to manipulate the data in some way. This means adding columns, deleting columns, performing permutations on data in columns, etc. We are going to cover all these things throughout this textbook. For now, let's start with the basics. Imagine we got the names of individuals from one source and their ages from another. We now need to add those ages into our DataFrame. We can approach the DataFrame as something like a dictionary here. We can add a column by creating it with df4\["ages"\]. This allows us to make that equal to the new data. The command below essentially adds a column to our DataFrame. Let's execute the command and print it off.

# In[16]:


df4["ages"] = [20, 26, 20, 18, 52, 40]


# In[17]:


df4


# Notice that we now have our second column. I want to stress right now, that to do this we needed data that matched the length of the names. If we tried to do this same act, but with 5 ages, rather than 6, we would have received an error.

# ## How to Grab a Specific Column

# When working with a DataFrame, you will often need to grab a single column of data. To do that, we can navigate the column data rather like a Python Class. Let's create a new object, names, and grab just the names column by stating df4.names. This command tells Pandas to grab the "names" column. Note, this is case sensitive. After we grab it, let's print it off too.

# In[18]:


names = df4.names


# In[19]:


print (names)


# Notice that we have a lot of data here about our names. We have their index (left column of integers). At the bottom, we have the type of data that it is. Don't worry about this extra data at the bottom for now. Let's try and grab the ages column now.

# In[20]:


ages = df4.ages


# In[21]:


ages


# ## How to Convert a Column to a List

# When you are working with a DataFame, you will often times need to work with that data not as a column, rather as a list. To do this, you will want to convert that data into a list. You can do this, by calling the method .tolist() after the data in question. Let's try it with ages and print off a list of ages.

# In[22]:


ages_list = df4.ages.tolist()


# In[23]:


print (ages_list)


# While this may not seem necessary on the surface, it is. One of the main reasons that this is essential is for processing large quantities of data. It is often times computationally less expensive to work with that data as a list or, better yet, as a NumPy array.

# ## How to Grab a Specific Row of a DataFrame

# It will often times be necessary to grab a DataFrame by row, not column. We have a lot of different ways to grab a row, but for now let's imagine we want to just grab a specific row by index. (We can grab all rows that have a certain value in a certain column also, but we will see that a bit later.) To grab a row by index, you can use the iloc command. This stands for Index Location. Index Location can be indexed rather like a list, as in the code below. The index you choose should correspond to the row index (starting with 0).

# In[24]:


row1 = df4.iloc[1]


# In[25]:


row1


# ## Conclusion

# You should now feel comfortable with creating, reading, and saving DataFrames. You should also be comfortable with adding columns and indexing by rows. In the next notebooks, we will dive into more complex features of DataFrames.

# In[ ]:




