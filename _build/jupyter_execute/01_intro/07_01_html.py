#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to HTML</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) HTML<br>
# 2) Tags<br>
# 3) Attributes<br>

# ## Introduction

# In part 7 of this textbook, we will learn about web scraping, one of the more vital skills of a digital humanist. <b>Web scraping</b> is process by which we automate the calling to a server (which hosts a website) and parsing the HTML file. <b>HTML</b> stands for HyperText Markup Language. It is the way in which websites are structured. When we web scrape a website, we write rules for extracting pieces of information from it based on how that data is structured within the HTML. To be competent at web scraping, therefore, one must be able to understand and parse HTML.
# 
# In this chapter, we will break down HTML and you will learn the most common tags, such as div, p, strong, and span. You will also learn about attributes within these tags, such as href, class, and id. It is vital that you understand this before moving onto the next chapter in which we learn how to web scrape with Python.

# ## Diving into HTML

# So why is HTML useful? HTML, like other markup languages, such as XML, or eXstensible Markup Language, allows users to structure data within data. This is achieved by what are known as tags. I think It is best to see what this looks like in practice. Let's examine a simple HTML file.

# In[1]:


html_file = """

<div>
    <p>This is a paragraph</p>
</div>

"""


# In the above cell, we see a very simple HTML file structure. Note the use of carrots "<" and ">". The first thing you may notice is that within the first set of carrots is the word "div". This is known as a div tag and it is one of the most common types of tags you will see within the HTML of a website. Jump ahead now to the bottom of the string and you will notice another div tag. There is something different with this one, however. Can you spot the difference?
# 
# If you said the "/" after the "<", you would be right! The first div tag is known as the <b>open tag</b> and the second div tag is known as the <b>close tag</b>. This tells a browser to parse this as a single block of data. Between these two tags, we have one piece of <b>nested data</b> Nested data is data that falls within a collection of tags. In our case, this is a <b>p tag</b>. P tags get their name from "paragraph". They are one of the essential types of tags you can expect to see. On websites, they are often used in the main content portion of the page and are used to break up texts. P tags allow your browser to understand how to render the HTML for you. When it sees a p tag, it will often separate it out from the paragraph above with a line break.
# 
# While in the early days of the internet, HTML files for websites were fairly simple on their structure, today that is no longer the case. It is very common for websites to have 20+layers deep of nested HTML structure. This is because websites are rarely written out by someone hard coding them. Instead, they are designed with user-friendly apps, such as Wordpress. They take user drag-and-drop input and features and convert it into robust HTML (and CSS - a subject for another day).

# ## Understanding Attributes

# Let's take a look at another block of HTML. This time, we will make one small change. Can you spot it?

# In[2]:


html_file2 = """

<div class="content">
    <p>This is a paragraph</p>
</div>

"""


# If you said the class="content" portion of the open div tag, then you would be right! This bit is nested within the tag and is known as an<b>attribute</b>. These will become your best friend when you try and start web scraping pages. You can use these attributes to specify which div tag to grab. Sometimes there will be multiple div tags with the same attribute name, however, but we will get to that in the next chapter. There are several common attributes, specifically class and id. Some websites will use custom attribute names, but this is quite rare and they are easy to spot.

# ## How to Find a Website's HTML

# Now that you are familiar generally with HTML and how it works, let's dive in and take a look at some real-world HTML from a real website. In the next chapter, we will web scrape Wikipedia, so let's go ahead and focus on Wikipedia here as well. If you are using a web browser that supports it (Chrome and Firefox), you can enter developer mode. Each operating system and browser has a different set of hotkeys to do this, but on all you can right click the webpage and click "inspect". This will open up developer mode. At this point in the chapter, I highly recommend switching over to the video as it will be a bit easier to follow along.
# 
# For this chapter (and the next), we will be working specifically with this page:
# https://en.wikipedia.org/wiki/List_of_French_monarchs
# 
# Go ahead and open it up on another screen or in a new tab. This Wikipedia article contains some text, but primarily it hosts a list of all French monarchs, from the Carolingians up through the mid-19th century with Napoleon III.
# 
# When you inspect this page, you will see all the nested HTML within it. Spend some time and go through these tags. In the next chapter, we will learn how to scrape this page, but for now take a look at what we can do with a few basic commands in Python.

# In[6]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_French_monarchs"
s = requests.get(url)

soup = BeautifulSoup(s.content)
body = soup.find("div", {"id": "mw-content-text"})
for paragraph in body.find_all("p")[:5]:
    if paragraph.text.strip() != "":
        print (paragraph.text)


# In the cell above, we used two libraries, requests and BeautifulSoup to call the Wikipedia server that hosts that particular page. We then searched for the div tag that contains the main body of the page. In this case, it was a div tag whose attribute "id" corresponded to "mw-content-text". I thin searched for all of the "p" tags, or paragraphs within that body and printed off the the text if the text was not blank. By the end of the next chapter, you will not only understand the code above, but you will be able to write it and code it out yourself. For now, inspect that page and see if you can find where the div tag whose id corresponds to "mw-content-text" is located in the HTML. It is okay if this is hard! It is not something that you naturally can do quickly. It takes practice. A trick to help get you started, however, is to right click the area that you want to scrape and then click inspect.
# 
# Once you feel comfortable with this, feel free to move on to the next chapter to start learning how to web scrape!

# In[ ]:




