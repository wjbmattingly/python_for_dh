#!/usr/bin/env python
# coding: utf-8

# # <center>Libraries in Python</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) External Libraries<br>
# 2) How to Install Libraries<br>
# 3) How to Import Libraries<br>

# ## Introduction

# Libraries are common across all programming languages. They allow you to import large amounts of code that contain functions and classes that you can leverage in your own code. A good way to think about a library is as the old expression: "don't reinvent the wheel". Use what others have done! Open-source is open for a reason! People who make these libraries do it so that you don't have to solve certain problems. They've done it for you.
# 
# In this chapter, we will learn how to install and import libraries. The reason we are doing this now is because the remainder of this textbook will require external libraries, specifically pandas, requests, and BeautifulSoup.

# ## How to Install Python Libraries

# Python comes preinstalled with pip. <b>Pip</b> is a package manager. It downloads, installs, and manages different versions of software on your machine. If you are coming to this textbook from windows, this concept might be a bit foreign. Think of pip something that will manage all your libraries for you. If you have installed Python via Anaconda, as I recommended, then pip will be automatically put into your system's Path. <b>Path</b> on Windows is a way that your computer can understand commands for exe files that you have on your system. If you open the terminal and you type "pip --version". On Windows, the terminal is command prompt.
# 
# Because I am using JupyterNotebook for this textbook, I can make terminal commands with the "!" before a block of code. When you type "pip --version", you should see something like the following output.

# In[2]:


get_ipython().system('pip --version')


# If pip is working, then it means we can install the libraries that we will need for the remainder of the textbook. We will require three libraries:
# 
# - Pandas
# - requests
# - BeautifulSoup
# 
# To install a library, you use the pip command "pip install library_name", like so:

# !pip install pandas

# You should see an output similar to this. If you do, then pandas has installed correctly. Let's now do the same thing for requests and BeautifulSoup.

# In[5]:


get_ipython().system('pip install requests')


# If you have already installed a library, the output will look something like this above.
# 
# For BeautifulSoup, we need to say pip install beautifulsoup4 (I will explain why later in this textbook.)

# In[6]:


get_ipython().system('pip install beautifulsoup4')


# And that's it! You have installed 3 new Python libraries! We need to learn one last thing, though, before we conclude this chapter. We need to learn how to import libraries within a Python script.

# ## How to Import a Library

# To import a library, we use the command import library_name, like so:

# In[8]:


import requests


# Sometimes, when we work with libraries, there is a certain Pythonic way to import the library. A classic case is pandas. With pandas, we import it "as pd". The "as pd" means that the name in the script will not be "pandas", rather "pd".

# In[7]:


import pandas as pd


# ## Conclusion

# That's all we need to cover in this chapter about libraries. You should feel a bit more comfortable about what libraries are, why they are useful, how to install them, and how to import them. As we continue through the final parts of this textbook, you will become more comfortable with libraries.
