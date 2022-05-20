#!/usr/bin/env python
# coding: utf-8

# # <center>Classes</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) Classes<br>
# 2) Methods<br>
# 3) How to Create Class>

# ## Introduction

# In this chapter, you will meet classes. <b>Classes</b> are rather like data structures, but they differ in one significant way. They can have functions attached to them. When you create a class in Python, you are essentially creating a special kind of data object that can have functions. Functions embedded within classes are known as <b>methods</b>. You have actually already met methods. In chapter 02_01 when we first learned about strings, you may recall that when we altered the data, we used a "." after the string object name followed by the function (method) that we wanted to call, e.g. str1.replace(something, something_else). This is what separates a function from a method syntactically in python. While a function is called by itself, a method must be called from a class object. While there is no easy way to explain this distinction, I hope that this explanation will be aided by working with classes and methods at a closer level below.

# ## Creating a Class

# Let's try creating a basic Class. Our class with store data specifically related to emperors, so let's go ahead and give it the name Emperor. We expect each emperor in our dataset to have four attributes: name, birth, coronation, and death.

# In[14]:


class Emperor():
    def __init__(self, name, birth, coronation, death):
        self.name = name
        self.birth = birth
        self.coron = coronation
        self.death = death


# This is the way this basic class will look. It can be a bit difficult to parse what is happening here when you see it for the first time, so let's break it down a bit.
# 
# In line one, we state:
# 
# class Emperor():
# 
# This line tells Python that we are creating a class. It's name is "Emperor". The open and close parentheses indicate the end of the class name. The colon indicates that anything that is indented afterwards is part of the class object's code.
# 
# The next line is intended. This is the structure you will use for most classes. The def __init__() creates four distinct objects from the incoming data associated with the class. These four objects are name, birth, coronation, and death, which we place inside the (). Notice that the first thing we pass, though, is self. Self points back at the current object. In our case, the class. It also allows each of the attributes: name, birth, coronation, and death, to be associated with a unique instance of class. This will become more clear as we proceed.
# 
# The next four lines just create these attributes and bind them to the instance of the class, by stating self.name = name, self.birth = birth, etc.
# 
# With this, our class is created. Now, let's try and make an object that is associated with this class.

# In[16]:


charlemagne = Emperor("Charlemagne", 742, 800, 814)


# Notice that we create the class object by using the class name, Emperor() and passing four arguments associated with the four attributes: name, birth, coronation, death.
# 
# Let's now try and print off that class object.

# In[18]:


print (charlemagne)


# This is new and likely not what you expected. This indicates that the object is a special class object. We can get the data from this class object by using the vars() command.

# In[19]:


print (vars(charlemagne))


# At this point, you may be thinking to yourself: "...what's the big deal? I've just made a dictionary."
# 
# And, at this point, you would be right. Our class, the way it is structured is really nothing more than a dictionary of data stored in a special way. This really is not a good usecase for a class. Remember, what makes classes unique is the ability to attach functions to them. Let's learn how to do that now!

# ## Adding Functions to a Class

# To create a function within a class, we create a function within it. Let's make a simple function that will print off a string that states who the emperor is and when that emperor was born. To do that, we will alter a class as so:

# In[34]:


class Emperor():
    def __init__(self, name, birth, coron, death):
        self.name = name
        self.birth = birth
        self.coron = coron
        self.death = death
    def birth_date(self):
        print (f"{self.name} was born in {self.birth}")


# Notice that we have now added a function within our class called birth_date(). This will receive self, or all the data associated with that particular class. This function will now strictly print off an f string that will state when a specific emperor was born.
# 
# Now, we just need to create a new class for Charlemagne.

# In[35]:


charlemagne = Emperor("Charlemagne", 742, 800, 814)


# Within this class, we can access the method birth_date(), like so:

# In[37]:


charlemagne.birth_date()


# And viola! You have now created your first class that has a specific function associated with it. Classes and functions are the two building blocks of any project. They allow for you to have tight, neater code that will be easier to read and look polished and professional. They prevent the writing of duplicate code. While it may appear unnecessary at times to view your code through functions and classes, I highly encourage you to start looking at it that way. It will make you a better programmer and you are less likely to have mistakes in your code.

# In[ ]:




