#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Pandas</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# ## Covered in this Chapter

# 1) What is Pandas?<br>
# 2) Why use Pandas?<br>
# 3) What is a DataFrame?<br>
# 4) How to Install Pandas<br>
# 5) How to Import Pandas (as PD!!)<br>

# ## What is Pandas?

# <center><img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/1200px-Pandas_logo.svg.png" width="500"></center>

# Pandas is a Python library in Python that allows for you to easily work with tabular data that is often stored in Excel files or .csv files. It is often considered one of the most vital Python libraries for data analysis because of its ease of use. There are other Python libraries that allow you to work with Excel data, such as XLSX and XLRD, which are leveraged by Pandas on the back end to interact with Excel spreadsheets. However, most tabular data is stored in .csv files, or Comma Separated Values files. There are other variations of this same structure (such as .tsv), but they all work the same. They use a special character to denote movement in the table to the next cell.

# ## Why use Pandas?

# If you work with data at all or plan to in the future, becoming comfortable with Pandas early on will make your life a lot easier. There are other Python libraries that allow you to work with .csv files, such as CSV, but these are not the same as Pandas. Pandas has one large advantage over CSV. It not only allows you to input .csv files into Python, it allows you to easily load them as DataFrames.
# 
# **DataFrames** are special data structures that contain not only the raw data in a table, but preserve the structure and hierarchy of that table. By loading .csv files as a DataFrame, Pandas not only allows you easy access to your data, but a powerful way to analyze it within a script. In addition to that, Pandas also has robust built-in features that we will explore throughout this textbook.
# 
# Finally, many MANY!! libraries for data analysis are built on top of Pandas. If you plan to understand how certain libraries work or how to get data to specific classes or functions correctly as a Pandas DataFrame, then you must be familiar with the Pandas library.
# 
# So, why use Pandas? Because it is the best library for importing and working with tabular data. It allows you to easily read files as DataFrames. And, it is a required library for most data analysis libraries.

# ## How to Install Pandas

# Installing pandas is as easy as installing any other Python library. If you are working within a Jupyter notebook like this one, you can execute the following command within a cell:

# In[1]:


get_ipython().system('pip install pandas')


# In Jupyter notebooks the ! indicates that you want to perform a command in the terminal. We then specify what command we want to run. In this case, pip install. Finally, we specify the library we want to install, pandas. If you are not working within a Jupyter notebook, you can do the same thing by opening up your terminal, such as Command Prompt on Windows, and executing the same command.

# ## How to Import Pandas

# Once you have installed Pandas, it is time to import it. It is Pythonic, or good Python practice, to import pandas as pd. By importing a library as something, you give it that specific variable as a name. This has a few benefits. First, it makes Pandas easier to call in your script, because you can call the library with "pd" rather than "pandas". Second, all... yes. ALL. Pandas tutorials and posts on Stackoverflow will use "pd".

# In[2]:


import pandas as pd


# After executing the above command, you will have successfully imported pandas into your Python script. In the next notebook, we will start working with Pandas
