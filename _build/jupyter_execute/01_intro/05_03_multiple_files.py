#!/usr/bin/env python
# coding: utf-8

# # <center>Working with Multiple Files</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>March 2022</center>

# ## Covered in this Chapter

# 1) The glob library<br>
# 2) Working with os<br>
# 3) Walking Directories<br>

# ## Introduction

# Often times, it is necessary to open multiple files in a Python script. There are multiple ways to do this, but unlike most Python textbooks. I recommend that beginners use the library called glob. <b>Glob</b> comes standard with Python which means you do not have to install it. A good way to think about glob is as a library that allows you to look into a directory and find all potential files based on certain parameters.

# ## Working with Glob

# Working with glob can be a little confusing at first, but let's break it down. First, we need to import glob.

# In[1]:


import glob


# Next, we need to use the glob class. This will take one argument, the string of files that you want to find. Let's use the data subfolder as an example. In the example below, we pass one string to this class. This string will be the subfolder in which the data lies followed by a slash followed by an \*. This \* is known as a wild card. In our case, it looks for all files within this directory.

# In[2]:


files = glob.glob("data/*")


# Let's print off the files now to see what all is inside the folder.

# In[3]:


print (files)


# Notice that we have grabbed all files! Most of the time, however, you will only want to grab files that are a specific type, e.g. .txt or .json. To achieve this we can add a .txt after the \*. This will grab all the .txt files.

# In[4]:


files2 = glob.glob("data/*.txt")
print (files2)


# ## Grabbing Multiple Nested Directories

# If you look in the subdirectory data, you will notice two nested directories called "other" and "other2". We can grab all files in each directory with the same wildcard \*.

# In[5]:


files3 = glob.glob("data/*/*.txt")
print (files3)


# ## Walking a Directory

# While glob is easy-to-use, it has certain limitations. One of these is when you need to walk through a directory. Imagine if we needed to grab all the txt files in data, data/other and data/other2. In order to grab all of these, we need to walk through all the subdirectories of data and collect all potential files. This is not possible to do with glob. In these rare circumstances, you should be familiar with the os library.
# 
# The <b>os</b> library allows us to do a lot of more advanced things in Python that I will not cover in this introductory textbook. One of the main things you will use os for is to navigate directories and create directories. For Linux users, a lot of the syntax will be familiar, but for Windows users it can feel a bit foreign. For now, let's simply import os.

# In[6]:


import os


# Once we have imported os, we can use the os.walk command. This will take one string. This should correspond to the directory that you want to start walking. Imagine that this is our directory:
# 
# - data
#     - other
#     - other2
# 
# We want to get all the text files in data, other, and other2.

# In[7]:


walking = os.walk("data/")
print (walking)


# This above output tells us what what we are looking at is a generator. Generators are a bit beyond this textbook, but think of them as a special kind of object that exists for a single moment in memory. Whenever you see generators, you can usually convert them to a list to work with them. Let's convert it by using the list() function in Python

# In[8]:


walking = list(walking)
print (walking)


# This can be a bit diffult to parse, so let's iterate over each item in walking.

# In[9]:


for item in walking:
    print (item)


# As we can see, each item is a tuple with 3 parts:
# 
# - root directory
# - subfolders
# - files
# 
# For our purposes, we only care about the root directory and the file itself. We can use these two pieces of data. Let's now modify our loop to grab these two pieces of data and print them off.

# In[10]:


final_files = []
for item in walking:
    root = item[0]
    files = item[2]
    print ("This is the Root")
    print (root)
    print ("These are the Files")
    print (files)
    print ()
    print ()


# As we can see, the files are a list. We can then iterate over the files to recombine the root with the files to cultivate a list. With os, we can do this with os.path.join(). This will take two arguments, the root directory and the file. Let's again modify our loop. We will print off the results.

# In[11]:


for item in walking:
    root = item[0]
    files = item[2]
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))


# Excellent! Now, we can use this exact same loop to append the file names to an empty list called final_files.

# In[12]:


final_files = []
for item in walking:
    root = item[0]
    files = item[2]
    for file in files:
        if file.endswith(".txt"):
             final_files.append(os.path.join(root, file))
print (final_files)


# Notice that we now have all the .txt files in the main directory and all subdirectories. This will be very useful when your files are in multiple subdirectories within multiple subdirectories.

# ## Conclusion

# I would recommend playing around with the code provided to you in this chapter. I cannot emphasize enough how frequently you will need to work with multiple files in a Python project. It is perhaps one of the things you should work hard to commit to memory. Over time, it will become more instinctual.

# In[ ]:




