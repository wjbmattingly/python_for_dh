#!/usr/bin/env python
# coding: utf-8

# # <center>Extracting Tabular Data from HTML</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>March 2022</center>

# ## Covered in this Chapter

# 1) Table Tags<br>
# 2) TR Tags<br>
# 3) TH and TD Tags<br>
# 4) How to parse an HTML Table<br>

# ## Introduction

# In this chapter, we will put our skills to work! We will learn how to extract tabular data via requests and BeautifulSoup. We will work with a lot of the commands and methods we saw in the last chapter, but we will not be trying to extract p tags, rather tabular data from the same Wikipedia page. All of this will allow you to apply your skills to the final challenge of this textbook (introduced in the next chapter).
# 
# First, let's import the same libraries as in the last chapter, requests and BeautifulSoup.

# In[1]:


import requests
from bs4 import BeautifulSoup


# Let's also go ahead and make the same string object, the url of the page we want to scrape.

# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_French_monarchs"


# Now, let's dive in!

# ## Finding the Tables on the Page

# In the cell below, we will make the call to the Wikipedia server and convert the HTML content into a soup object as we saw in the last chapter.

# In[3]:


s =  requests.get(url)
soup = BeautifulSoup(s.content)


# Now that we have our soup object, we can start to parse it. Tables are often structured in HTML the same way across all sites. The main tag used is the table tag. On Wikipedia, there are multiple kinds of tables. The class we want is a table class called "wikitable". Let's go ahead and grab all these tables and print off how many we have on the page.

# In[4]:


tables = soup.find_all("table", {"class": "wikitable"})
print (len(tables))


# ## Grabbing Rows of a Table

# Excellent! Now that hwe have the tables, let's take a look at the first one's HTML.

# In[5]:


first_table = tables[0]
print (first_table)


# A table is a combination of 2 things: rows and cells. Rows will almost always be "tr" tags. This stands for table row. Cells with either be th tags or td tags. The th tag stands for table header. This will usually be used in the first row that indicates the name of the column. The td tag stands for Table Data cell. These are the cells that start on the first row that contains data and continue on down until the table ends. Because tables are precise structurally, there will always be the same name of headers as there are columns of data. We can use this structure to our advantage.
# 
# Let's find all the rows in the first table

# In[6]:


rows = first_table.find_all("tr")


# Excellent! Now, let's iterate over all the rows.

# In[7]:


for row in rows:
    print (row)


# We can see the precise same HTML that we saw above. Now that we can access the rows, let's try and access the first row of data.

# ## Find Cells

# To do this, we will need to find each cell. Remember, on row 1, we are working with th tags because these are headers.

# In[8]:


first_row = rows[0]
print (first_row)


# Let's now try to find all the cells in the first row.

# In[9]:


cells = first_row.find_all("th")
print (cells)


# We can iterate over these cells and print off their text. I am adding .strip() here to remove the leading whitespaces and line breaks.

# In[10]:


for cell in cells:
    print (cell.text.strip())


# ## Iterating Across the Entire Table

# Now that we know how to grab all tables, all rows within a table, and all cells within a row, let's try and iterate over the entire first table. First, let's grab the headers.

# In[11]:


rows = first_table.find_all("tr")
for row in rows:
    cells = row.find_all("th")
    for cell in cells:
        print (cell.text.strip())


# Now that we know all the headers, explore all the table data cells which start on the next row.

# In[12]:


rows = first_table.find_all("tr")
for row in rows:
    cells = row.find_all("td")
    for cell in cells:
        print (cell.text.strip())


# Now that you know how to grab all of this data, it will be time to bring all of this together for your final task. In the next chapter, we will try and extract all this data into properly structured data that will be stored within Python, then parsed as a Pandas DataFrame, and finally saved as a .csv file.

# ## Other Options

# I want to emphasize that there are other, easier ways to do this task. As with all things in Python, there are multiple solutions to the same problem. Here is one potential solution with Pandas. Pandas has a .read_html() function that can take a url. It will return a list of all tables in an HTML document. Let's try that and take a look at the first table.

# In[13]:


import pandas as pd


# In[14]:


df = pd.read_html(url)[0]


# In[15]:


df


# It's not bad. And for a quick result, this is great, but it is not perfect. Notice the brackets with the citations in the Start column and the circle at the lead of each string in the Succession column. We also likely do not need to know NaN for each Portrait column. In other words, while Pandas is a quick solution, it is good to know how to do a custom solution using requests and BeautifulSoup.

# In[ ]:




