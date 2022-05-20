#!/usr/bin/env python
# coding: utf-8

# # <center>Working with JSON Data</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) JSON data format<br>
# 2) json.dump()<br>
# 3) json.load()<br>

# ## Introduction

# In this chapter, you will meet JSON data. JSON is a data format that is frequently used online. It stands for JavaScript Object Notation. It is the principal way in which data is stored for websites and called by JavaScript. There are two reasons to learn JSON data structures early in your coding career.
# 
# 1) JSON is universally recognized by all browsers.
# 2) JSON allows you to structure hierarchical data.
# 
# What is hierarchical data? This is data that may be nested within other data. This type of data is sometimes difficult to represent cleanly in CSV format. A good way to think about this is with the following data structure. Imagine you wanted to store a series of texts in Excel. In one column, you would have a text and then in the next column, you would store a list of speakers. Now, how do you represent the list of names? You could do it like this:

# | Text                                                             | Names                        |
# |------------------------------------------------------------------|------------------------------|
# | John and Kathy both know each other. Marge and Francois do not. | John, Kathy, Marge, Francois |

# But this can get messy really quickly because lists are difficult to store as a data structure within a cell. There are ways to get around this, but when you start working with this type of CSV data computationally, it can get complicated the deeper the hierarchies go. Imagine if for each person, we had an age and a role. How would we store that data? Perhaps like this:

# | Text                                                             | Names                        | Age            |
# |------------------------------------------------------------------|------------------------------|----------------|
# | John and Kathy both know each other. Marge and Francois do not. | John, Kathy, Marge, Francois | 20, 25, 30, 35 |

# If I want to update the data, I need to make sure that the list of ages corresponds to the list of names. Again, this can lead to issues down the road. The solution is to stop using CSV or Excel to store this type of data and use a format that is more flexible and able to handle things like lists and nested hierarchical data. In Python, the easiest solution is JSON. To use JSON, you do not need to install any special libraries. It comes prebuilt with a special library called JSON. The only methods you need to know to use JSON: json.dump() and json.load(). But first, let's import json.

# In[1]:


import json


# Let's create the data above as a data structure within Python.

# In[1]:


data = {"text": "John and Kathy both know each other. Marge and Francois do not.",
        "names": ["John", "Kathy", "Marge", "Francois"]}
data


# ## json.dump()

# Now, let's try and store that data outside of Python as a JSON file. To do that, we with use the with open operator we learned about in the last chapter. Instead of naming this a .txt file, however, we will name is .json. Next, we will execute the command json.dump(). This will take 2 essential arguments: the data that you want to dump to the file and the object in which you want to dump the data, in this case "f". The other keyword argument here is indent. I always like to use this because it makes the JSON file easier to read. It indents the data 4 spaces each time it goes deeper into the hierarchy.

# In[12]:


with open ("data/sample_json.json", "w") as f:
    json.dump(data, f, indent=4)


# ## json.load()

# Now that we have dumped the data into a file, let's try and load it back up. Here, we will open the same JSON file, but this time as readable. We will create a new object, new_data and use json.load(). This will take one argument, the file object that you want to load from. So long as your JSON file is not corrupted, the data will load successfully.

# In[14]:


with open ("data/sample_json.json", "r") as f:
    new_data = json.load(f)
new_data


# These are the only two commands that you need to know to start working with JSON data in Python. I highly encourage you to spend a few minutes playing with these commands and trying to store data with json.dump() and load data with json.load()

# In[ ]:




