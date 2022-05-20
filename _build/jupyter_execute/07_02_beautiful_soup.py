#!/usr/bin/env python
# coding: utf-8

# # <center>Requests and BeautifulSoup</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) The basics of requests<br>
# 2) The basics of BeautifulSoup<br>
# 3) How to navigate the soup object<br>

# ## Introduction

# In the last chapter, I introduced you to the basics of HTML. At the end of the chapter, we saw briefly how that HTML can be used to call a server that holds a website's page and then parse that data. While we did not cover precisely what was happening in the code, all of this was achieved with two libraries that we will meet in this chapter: requests and BeautifulSoup.
# 
# The <b>requests</b> library allows us to send a signal via Python to server. A good way to think about requests is as an invisible browser that opens in the background of your computer. Requests does the precise thing your browser does. It sends a signal over the internet to connect to a specific server address. While all servers have a unique IP address. Often the internet links a specific and unique address that can be used as a way to connect to a server without having to type out an IP address. Unlike your browser, however, requests does not will up the results for you to see. Instead, it receives the return signal and simply stores the HTML data in memory.
# 
# <b>BeautifulSoup</b> is the second library in this workflow. It allows us to create a unique soup object which converts the HTML into a unique data structure in memory that we can then parse, analyze, and navigate through Python.

# ## Why Requests and BeautifulSoup?

# I recommend learning requests and BeautifulSoup to beginners of web scraping for two reasons. First, they are the simplest libraries to learn in Python. Second, for the vast majority of web scraping tasks, requests and BeautifulSoup will do everything you need. In some circumstances, websites may have robust methods in place to prevent web scraping.
# 
# While not covered in this chapter, there are more robust and powerful ways to scrape data with Python, specifically with Selenium. <b>Selenium</b> performs both the functions of requests and BeautifulSoup. Additionally, Selenium allows you to open up a special instance of a browser (typically Chrome or Firefox) and control that browser through Python. When you need to do more sophisticated web scraping, particularly instances where you need to type in a password or scroll down a page or need to imitate a human, Selenium is the method of choice. I will be coming out with a textbook around web scraping in the near future (as of March 2022) that will detail this process in greater detail. For now, I mention it so that you know the limitations of requests and BeautifulSoup and the potential ways to fill their gaps.

# ## Installing the Libraries

# In part 6 of this textbook, I introduced you to the installation of libraries. In case you have forgotten, you can install the libraries with pip, Python's package manager. You can do this with the following commands:
# 
# - pip install requests
# - pip install beautifulsoup4

# ## Requests

# Now that we have installed the libraries, we can go ahead and start working with them. As noted above, the request library lets us make calls via Python to a server over the internet. Let's try it out now.
# 
# First, let's import the requests library

# In[1]:


import requests


# Now that we have imported requests, let's go ahead and create a string object that will be the website we want to scrape. I always call this string "url" in my code. 

# In[2]:


url = "https://en.wikipedia.org/wiki/List_of_French_monarchs"


# Excellent! Now we can use the requests library to make a call to this particular page. We will do this via the get function in the requests library. The get function has one mandatory argument: the website that you want to request. In our case, this will be our "url" string.

# In[3]:


s = requests.get(url)


# Now that we have created a request object, let's take a look at what this looks like.

# In[4]:


print (s)


# On the surface, this looks like we may have failed. What is this odd "response 200" and what does it mean? This particular response means that our attempt to connect to a server was successful. There are many types of responses, but 200 is the one we want to see. If you ever see a response that is not 200, you can Google the particular server response and you will find out what is happening. Sometimes, a response indicates that your request was blocked. This may be because the website has anti-web scraping measures in place. In other cases, the page may be protected, meaning that it lies behind a login. There are too many potential errors that may surface that I cannot detail them all in this basic introduction chapter. I will, however, give you a solution to a very common problem that can allow you to get around a common 403 response. For that solution, check out the final section of this chapter.

# ## BeautifulSoup

# Now that we have learned how to make a call to a server and stored the response (the HTML) in memory, we need a way to parse that data. Buried within the s request object is the HTML content. We can access that data by accessing the content method of the response object class. Let's do that and check out the first 100 characters.

# In[5]:


print (s.content[:100])


# Notice that this data is HTML. At this stage, however, we do not have an easy way to take this string and process it as structured data. This is where BeautifulSoup comes into play. BeautifulSoup allows us to convert s.content into structured data that we can then parse. To do this, we first need to import BeautifulSoup. Unlike most libraries, BeautifulSoup installs as bs4 (BeautifulSoup4). Because of this we need to import the BeautifulSoup class from bs4. The command below does this for us.

# In[1]:


from bs4 import BeautifulSoup


# Next, we need to create a new soup object.

# In[7]:


soup = BeautifulSoup(s.content)


# If we don't see an error, then it means we have successfully created a soup object. Let's print it off to see what it looks like:

# In[17]:


print (str(soup)[:200])


# While the soup object looks precisely the same as the s.content, it is entirely different. It retains the structure of the HTML because BeautifulSoup has parsed it for us. This means that we can use special methods. In this section of the textbook, we will use find and find_all.
# 
# - find - this will allow us to find the first instance of a tag being used and grab that tag and all its nested components.
# - find_all - this will return a list of all tags and their nested components that align to this specific tag.
# 
# Let's take a look at a basic example of the find method.

# In[9]:


div = soup.find("div")


# Here, we grabbed the first div tag on the page. Div tags, however, are quite common because they are one of the essential building blocks of HTML. Let's take a look at how many there are on the entire page. We can do this with the find_all method and then count the list size with the len function that we met in chapter 02_02.

# In[10]:


all_divs = soup.find_all("div")
print (len(all_divs))


# So, if we want to grab a specific div with only find and find_all, we would have to count all the div tags and find the right index and grab it. This would not work at scale because this would vary from page to page, even if the HTML data structure were similar across all pages on a site. We need a better solution. This is where our second optional argument comes in. The find function can also take a dictionary that allows us to pass some specificity to our parsing of the soup object.
# 
# Let's say I want to grab the main body of the Wikipedia article. If I inspect the page, I will notice that one particular div tag contains all the data corresponding to the body of the Wikipedia article. This div tag has a special unique id attribute. This id attribute's name is "mw-content-text". This means that I can pass as a econd argument a dictionary where id is the key and the corresponding id name is the value. This will tell BeautifulSoup to find the first div tag that has an id attribute that matches mw-content-text. Let's take a look at this in code.

# In[11]:


body = soup.find("div", {"id": "mw-content-text"})


# Now that we have grabbed this body portion of the article, we can print it off with the text method.

# In[18]:


print (body.text[:500])


# This is fantastic! But, what if we wanted to grab the text and maintain the structure of the paragraphs. We can do this by searching the soup object at the body level. The body object that we created is still a soup object that retains all that HTML data, but it only contains the data for the data found under that particular div. We can use find all now to grab all the paragraphs from within the body. We can use find_all on the body object to find all the paragraphs like so:

# In[13]:


paragraphs = body.find_all("p")


# We can now iterate over the paragraphs. Let's do that now over the first five paragraphs and print off the text.

# In[14]:


for paragraph in paragraphs[:5]:
    print (paragraph.text)


# Viola! You have now officially webscraped your first page in Python and grabbed some relevant data.

# In[ ]:




