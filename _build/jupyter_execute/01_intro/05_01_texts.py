#!/usr/bin/env python
# coding: utf-8

# # <center>Working with Textual Data</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) Text Files<br>
# 2) The With Operator<br>
# 3) How to Open Text Files in Python<br>
# 4) How to Read from Text Files in Python<br>
# 5) How to Write to Text Files in Python<br>

# ## Introduction

# Up until now, we have strictly worked with data that we have produced within our own code. Rarely will you ever copy-and-paste data into a Python script. Instead, you will need to interact with external data. Further, you will often need to save data in some way. This chapter is the first of two that walk you through how to interact with external data. We will be working with textual data in this chapter, while in the following chapter we will work with JSON, or JavaScript Object Notation data. In Part 07, Chapter 02, we will work with tabular data.

# ## The With Operator

# The with operator in Python is an essential command that allows for you to do something in memory for so long as the operator is open. This is really important when opening text files. There are several ways to open text files in Python, but I am only showing you this method because it is the most Pythonic. Other methods require you to close the text file in code. If you do not, it will remain open in memory. If you are working with 10,000 text files (I have done this before), and forget to add a close command in your code while iterating over all 10,000 files, your computer will run out of memory and crash. The with operator avoids this problem entirely.

# ## How to Open a Text File

# Let's see what it looks like in action and then we will break down what is happening.

# In[1]:


with open ('data/sample.txt', "r") as f:
    data = f.read()


# The first line in our code is
# 
# with open (file, "r") as f:
# 
# We can see that we start clearly with the "with" operator. Next, we specify what we are going to do with the with operator. In this case, we will be using the open command. Open tells Python to open a file. Within the parentheses, we pass two arguments. The first argument is a string that corresponds to where the file is located. Here, the file is in our data subfolder and is called "sample.txt". The final component of this line is "as f". This tells Python to open that file up temporarily as the object name "f". The final colon, which we have seen before, indicates that we are about to do something indented.
# 
# The next line is indented because this is a nested bit of code that is being done within the with operator. The line reads:
# 
# data = f.read()
# 
# The name data is the object name that we are assigning to the contents of the file. Next, we see f.read(). This command tells Python to take the f object, in this case the temporary file, open it and read its contents.
# 
# Now, let's take a look at those contents! We can print them off with the print command.

# In[2]:


print (data)


# We can see that the text file contains three lines. It is frequently necessary to split up input data by linebreaks. Sometimes this is necessary when the text file is a list of data with each piece of data stored on a new line. Other times, you need to clean the data so that a paragraph of a scanned book is a continuous string of text. One of the easiest ways to do this is to use the built-in method, splitlines().

# In[4]:


print (data.splitlines())


# As you can see, splitlines allows us to convert our string into a list of strings that are separated by linebreaks.

# ## How to Write Data to a Text File

# Just as it is necessary to access external data via Python, you will find yourself frequently needing to storing data outside of a Python script. Let's take a look at how to do this in the following block of code.

# In[5]:


new_string = "This is a new string."
with open ("data/sample2.txt", "w") as f:
    f.write(new_string)


# This block of code looks very similar to the one above, but with a few exceptions. First, we created a string called new_string. Next, we need to drop that new string into a text file. In this case, we will drop it into data/sample2.txt. Notice, that we have replaced the "r" with "w". This is because we are telling Python that we want to write to the file, not read it.
# 
# In the indented bit of code, we use f.write(), rather than f.read(). This allows us to write to the f object, rather than read from it. It will take one argument, the string that we want to write to the file. In our case, it is the string object, new_string.

# In[ ]:





# 

# In[ ]:





# In[ ]:





# In[ ]:




