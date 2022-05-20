#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Data Structures</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Data Structures

# In the last chapter, we met strings, integers, floats, and booleans. Each of these were types of data. Strings, for example, allowed us to work with text and numbers allowed us to work with integers and floats. In this chapter, we will begin working with data structures. <b>Data structures</b> are ways of storing multiple kinds of data in a systematic way. In Python, these are created as objects that can be stored in memory and called later in a script. They are divided into two categories: mutable and immutable. We encountered these terms in the last chapter, but we will explore what they mean in more depth below.
# 
# Throughout this chapter, we will learn about some of the key types of data structures, how they are different, and how they can be used. We will only cover these in a cursory manner. Throughout this textbook, we will use these data structures to write code and perform data cleaning and data analysis tasks. It is essential that you know how to recognize types of data structures and differentiate them before moving forward. To keep things simple for now, we will focus on three types of data structures: lists, tuples, and dictionaries. There are other types of data structures in Python, but these are the core three that you will use.

# ## Lists

# <b>Lists</b> and tuples are identical with one major exception: lists are mutable. This means that you can create a list object and then alter it in memory as your script runs. This allows for you to do very powerful things to lists that you cannot do to tuples. And these are going to be one of the key data structures you use in all digital humanities projects. The reason? We often need to adjust data while working with it.
# 
# While we created a tuple with parentheses, we will create lists with square brackets. In the examples below we have two lists. In the first list we see that lists, just like tuples, can contain integers, floats, or strings. We separate items in our list with a comma. In the second example, a_list2, we see that lists can contain data structures within them. This is true for lists, tuples, and dictionaries.

# In[1]:


list1 = [1, 1.0, "one"]
print (list1)


# We can index lists, or grab the data from a certain position, with the square brackets. The command:

# In[2]:


print (list1[0])


# ## Tuples

# <b>Tuples</b> are lists of data that cannot be changed. When we look at lists in Lesson 06, we will see that lists are the exact same thing as tuples, except they can be changed. We can distinguish tuples from lists by the way in which they are formed. While lists use square brackets, tuples use parentheses. We create a tuple, like the example below. Our tuple object is a_tuple and the tuple consist of three items: an integer 1, a float 1.0, and a string of “one”. Lists and tuples can contain all three of these types of data. The way in which we separate items in a tuple is with a comma.

# In[4]:


tuple1 = (1, 1.0, "one")


# In[5]:


print (tuple1)


# ## Mutability vs Immutability

# As noted above, tuples are immutable which means they cannot be changed. Let's see precisely what this means in practice. Say, we wanted to add to a list. We can do this with the .append() method. This will take one argument, or piece of information placed between the parentheses. You will learn about arguments later when we discuss functions and methods in greater depth. For now, understand that the information passed between the parentheses tells the method or function what is needed to perform the function. In this case, .append() allows us to append, or add, something to a list. The argument that we pass, "one", tells what we want to append. In this case, the string, "one".

# In[6]:


list1.append("one")


# In[7]:


print (list1)


# Notice that we do not have an error. This is because our list is mutable, or changeable. This means that we can add to it, delete items from it, and other operations that allow us to change how it is stored in memory. Tuples, on the other hand, are immutable, or unchangeable. Let's try and perform the same method on the tuple and see what happens.

# In[8]:


tuple1.append("one")


# Notice that we get an AttributeError. This means that a tuple does not have the ability to use the append method. This does not exist for tuples because they are immutable or unchangeable. The only way to alter the object name, tuple1 is to entirely replace it in memory.

# ## Sets (Bonus Data Structure)

# There is one other data structure similar to lists and tuples and I include it here as a bonus data structure. This is the set. A <b>set</b> is identical to a list. It is mutable, meaning we can update it, but unlike a list, it cannot contain duplicates. This is useful in niche circumstances, such as when you need to remove all duplicates from a list. I include it here just so that you are aware that other types of data structures do exist.

# In[10]:


set1 = {1, 1.1, "one", "one"}
print (set1)


# ## Dictionaries

# Like tuples and lists, dictionaries are a data structure in Python. Like lists, dictionaries are mutable, meaning they can be changed in memory. Unlike tuples and lists, dictionaries are not lists of data. Instead, they have two components: keys and values. These two components are separated by a colon. All of this is contained within squiggly brackets. In the example below, we have a dictionary, a_dict, with a key of “name” and a value of "William".

# In[11]:


dict1 = {
        "name": "William",
         "last_name": "Mattingly"
        }


# In digital humanities projects, dictionaries are particularly useful for structuring complex data that you may have in Excel with each key being an Excel column and each value being its corresponding value. The dictionary name could be the name of the individual to whom the row corresponds. Like lists and tuples, you can embed data structures within a Python dictionary.

# In[12]:


print (dict1)


# In[13]:


list1 = ["William", "Mattingly"]
print (list1)


# In[15]:


print (dict1["last_name"])


# ## Indexing

# Often times, you will not simply make a data structure in Python, but need a way to interact with it. We saw above that one can append a list. This would be considered one type of interaction. In other instances, we may only want to interact with a single piece of data within a data structure or we may simply want to look at a single piece of data. This is known as <b>indexing</b>. Indexing is when we index, or pull from a particular data structure at a specific point or points. Let's learn about this first with lists and tuples.

# ### Indexing a List or Tuple

# Often we will index a list at a specific point. To do this, let's first create an object called list5.

# In[2]:


list5 = [1, 2, 3, 4, 5]


# Excellent. This list contains 5 pieces of data within it, the numbers 1-5. Each of these are separated with a comma, as is required by a list. To index this list, we call up the variable name list5 and we use \[ \]. Within these brackets, we place the index, or position within the list that we want to grab.
# 
# **It is very important to note that Python is a 0-Index language. This means that all indexing starts at 0 and moves up, so the first position in a list is index 0, second is index 1, etc.**
# 
# With that said, let's try and grab the first item in the list at index 0.

# In[3]:


print (list5[0])


# Notice that we have printed off successfully the number 1. Often times, though, it is important to index multiple items in a list. If we want to do this, we use \[ \] again. Within the brackets we will have a start position and an end position. The end position will be the point after we want to grab. These will be separated by a :. In code, it would look something like this:
# 
# index_item\[start:end\]
# 
# Let's say, we wanted to grab the first 3 items from the list, we would want to do something like this.

# In[20]:


print (list5[0:3])


# We can also work backwards with indexing. We can, for example, use a -1 to grab the final item in the list.

# In[21]:


print (list5[-1])


# We can also use range indexing to grab the final three items. In Python, if you index a list with no end point, it will grab everything up to the end of that list. We can see this in the two examples below.

# In[22]:


print (list5[-3:])


# In[23]:


print (list5[:3])


# ### Indexing Dictionaries

# In Python, we will frequently need to index a dictionary. Dictionaries, remember, are a bit different from lists and tuples. Rather than being a sequence of items in a list, a dictionary is a collection of keys and corresponding values. To index a dictionary, therefore, we need to work a bit differently. Rather than indexing at a specific point, we index dictionaries at a specific key.
# 
# To understand this, it is best to see it in practice, so let's go ahead and create a dictionary called dict5.

# In[4]:


dict5 = {"names": ["William", "Stephanie", "Samantha", "Anna", "Sierra"]}


# This dictionary has one key, "names". If I wanted to index at the key "names", I would use the same method of brackets and place the key within the brackets. It would look something like this.

# In[5]:


print (dict5["names"])


# ## Quiz

# In[6]:


quiz = '''
# What kind of data structure is made with [ ]?
mc
* List
-c t
-f

* Tuple
-c f
-f

* Dictionary
-c f
-f

# What kind of data structure is made with ()?
mc
* List
-c f
-f

* Tuple
-c t
-f

* Dictionary
-c f
-f

# What kind of data structure is made with {}?
mc
* List
-c f
-f

* Tuple
-c f
-f

* Dictionary
-c t
-f

# What are the two parts of a dictionary?
mc
* Key
-c t
-f

* Value
-c t
-f

* Index
-c f
-f

# What index does a Python list start at?
mc
* 0
-c t
-f

* 1
-c f
-f
'''


# In[7]:


from jupyterquiz import display_quiz
import md2json
import json
myquiz = md2json.convert(quiz)
myquiz = json.loads(myquiz)
display_quiz(myquiz)


# In[ ]:




