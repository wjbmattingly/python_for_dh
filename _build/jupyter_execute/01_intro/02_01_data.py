#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Data</center>

# ## Some Quick Notes about Terminology and Commands we will Use

# ### Objects

# When we import or create data within Python, we are essentially creating an object in memory with a variable. These two words, <b>object</b> and <b>variable</b> mean slightly different things and, but are often used interchangeably. We will not get into the complexities of their differences and why they exist in this textbook, but for now, view an object as something that is created by a Python script and stored in your computer's memory so that it can be used later in a program.
# 
# Think of your <b>computer's memory</b> rather like your own brain. Imagine if you needed to remember what the word for "hello" in German. You may use your memory rather like a flashcard, where "hello" in English equates to "hallo" in German. In Python, we create objects in a similar way. The object would be the dictionary entry of "hello: hallo".created

# ### Variables

# In order to reference this dictionary entry in memory, we need a way to reference it. We do this with a variable. The variable is simply the name of the item in our script that will point to that object in memory. Variables make it so that we can have an easy-to-remember name to reference, call, and change that object in memory.
# 
# Variables can be created by typing a unique word, followed by an = sign, followed by the specific data. As we will learn throughout this chapter, there are many types of data that are created differently. Let's create our first object before we begin. This will be a string, or a piece of text. (We will learn about these in more detail below.) In my case, I want to create the object author. I want author to be associated with my name in memory. In the cell, or block of code, below, let's do this.

# In[1]:


author = "William Mattingly"


# ### The Print Function

# Excellent! We have created our first object. Now, it is time to use that object. Below, we will learn about ways we can manipulate strings, but for now, let's simply see if that object exists in memory. We can do this with the print function.
# 
# The print function will become your best friend in Python. It is, perhaps, the function I use most commonly. The reason for this is because the print function allows for you to easily debug, or identify problems and fix them, within your code. It allows us to print off objects that are stored in memory.
# 
# To use the print function, we type the word print followed by an open parentheses. After the open parentheses, we place the object or that or piece of data that we want to print. After that, we close the function with the close parentheses. Let's try to print off our new object author to make sure it is in memory.

# In[2]:


print(author)


# Notice that when I execute the cell above, I see an output that relates to the object we created above. What would happen if I tried to print off that object, but I used a capital letter, rather than a lowercase one at the beginning, so Author, rather than author?

# ### Case Sensitivity

# In[3]:


print(Author)


# The scary looking block of text above indicates that we have produced an error in Python. This mistake teaches us two things. First, python is case sensitive. This means that if any object (or string) will need to be matched in not only letters, but also the case of those letters. Second, this mistake teaches us that we can only call objects that have been created and stored in memory.

# ### Reserved Words

# When working with Python, there are a number of words known as **reserve words**. These are words that cannot be used as variable names. As of Python version 3.6, there are a total of 33 reserve words. In can sometimes be difficult to remember all of these reserve words, so Python has a nice built in function, "help". If we execute the following command, we will see an entire list.

# In[13]:


help("keywords")


# These are words that you cannot use as a variable name.

# ### Built-in Types

# In addition to reserve words, there are also built-in types in Python. These are words that you can use (as we will see) to convert one type of data into another. There are 94 of these in total. Unlike reserve words, you *can* use a built-in type as a variable name. It is, however, strongly discouraged to do so because it will overwrite the intended use of these variable names in your script.

# In[8]:


import builtins
[getattr(builtins, d) for d in dir(builtins) if isinstance(getattr(builtins, d), type)]


# Of this long list, I recommend paying particular attention to the ones that you are more likely to write naturally: bool, dict, float, int, list, map, object, property, range, reversed, set, slice, str, super, tuple, type, and zip. You are more likely to use these as variable names by accident than, say, ZeroDivisionError; and this shorter list is a lot easier to memorize.

# ## What is Data?

# In Python there are seven key pieces of data and data structures with which we will be working:
# 
# - strings (text)
# - integers (whole numbers)
# - floats (decimal numbers)
# - Booleans (True or False)
# - lists
# - tuples (lists that cannot be changed in memory)
# - dictionaries (key : value)
# 
# In the next two chapters, we will explore each of these. While this chapter focuses on data: strings, integers, floats, and Booleans; the next chapter will focus on data structures: lists, tuples, and dictionaries.
# 
# Data are pieces of information (the singular is datum)i.e., integers, floats, and strings. Data structures are objects that make data relational, i.e. lists, tuples, and dictionaries. Before you proceed to lesson three, you MUST have a basic understanding of the ways in which you create data in Python and the ways in which you make that data relational through data structures. Start to train your brain to recognize the Python syntax for these pieces of data and data structures discussed below.

# ## Strings

# <b>Strings</b> are a sequence of characters. A good way to think about a string is as a text. We can create a string in python by designating a unique variable name and setting = to something within quotation marks, i.e. ” ” or ‘ ‘.
# 
# The opening of a quotation mark indicates to Python that a string has begun and the closing of the same style of a quotation mark indicates the close of a string. It is important to use the same style of quotation mark for a string, either a double or a single. In the examples below, we have two string objects: a_string and b_string, the former corresponds to the string “Hello” and the latter corresponds to the string “Bye”.
# 
# Let's take a look at a few examples of strings.

# ### Examples of Strings

# In[4]:


#Strings - any kind of text
str1 = "This is a string."


# In[5]:


print (str1)


# In[10]:


str2 = 'This is a string too.'


# In[7]:


print (str2)


# In[8]:


str3 = "This is a "bad" example of a string"


# In[10]:


str4 = '''
This is a verrry long string.

'''


# In[11]:


print (str4)


# ## Numbers (Integers and Floats)

# Numbers are represented in programming languages in two several ways. The two we will deal with are integers and floats.
# 
# An <b>integer</b> is a digit that does not contain a decimal place, i.e. 1 or 2 or 3. This can be a number of any size, such as 100,001,200. A float, on the other hand, is a digit with a decimal place. So, while 1 is an integer, 1.0 is a float. Floats, like integers, can be of any size, but they necessarily have a decimal place, i.e. 200.0020002938. In python, you do not need any special characters to create an integer or float object. You simply need an equal sign. In the example below, we have two objects which are created with a single equal sign. These objects are titled an_integer and a_float with the former being an object that corresponds to the integer 1 and the latter being an object that corresponds to the float 1.1.

# ### Examples of Numbers

# In[12]:


int1 = 1


# In[13]:


print (int1)


# In[14]:


float1 = 1.1


# In[15]:


print (float1)


# ## Booleans

# The term boolean comes from Boolean algebra, which is a type of mathematics that works in binary logic. Binary is the basis for all computers, save for the more nascent quantum computers. Binary is 0 or 1; off or on; true or false. A boolean object in programming languages is either True or False. True is 1, while False is 0. In Python we can express these concepts with capitalized T or F in True or False. Let's make one such object now.

# ### Examples of Booleans

# In[16]:


bool1 = True


# In[17]:


print (bool1)


# In[18]:


bool2 = True


# In[19]:


bool3 = False


# In[20]:


print (bool3)


# In[21]:


bool4 = False


# ## Working with Strings as Data

# Often when working within Python, you will not be simply creating data, you will be manipulating it and changing it. Because humanists frequently work with strings, I recommend spending a good deal of time practicing and memorizing the basic ways we work with strings in Python via the built-in methods.
# 
# In order to interact with strings as pieces of data, we use <b>methods</b> and <b>functions</b>. The chief functions for interacting with strings on a basic level come standard with Python. This means that you do not need to install third-party libraries. Later in this textbook we will do more advanced things with strings using third-party libraries, such as Regex, but for now, we will simply work with the basic methods.
# 
# Let's learn to manipulate strings now through code, but first we need to create a string. Let's call it str6.

# In[22]:


str6 = "This is a new string."


# It is not a very clever name, but it will work for our purposes. Now, let's try to convert the entire string into all uppercase letters. We can do this with the method <b>.upper()</b>. Notice that the .upper() is coming after the string and within the () are no arguments. This is a way you can easily identify a method (as opposed to a function). We will learn more about these distinctions in the chapters on functions and classes.

# In[23]:


print (str6.upper())


# Noice that our string is now all uppercase. We can do the same thing with the <b>.lower()</b> method, but this method will make everything in the string lowercase.

# In[24]:


print (str6.lower())


# On the surface, these methods may appear to only be useful in niche circumstances. While these methods are useful for making strings look the way you want them to look, they have far greater utility. Imagine if you wanted to search for a name, "William", in a string. What if the data you are examining is from emails, text messages, etc. William may be capitalized or not. This means that you would have to run two searches for William across a string. If, however, you lowercase the string before you search, you can simply search for "william" and you will find all hits. This is one of the things that happens on the back-end of most search engines to ensure that your search is not strictly case-sensitive. In Python, however, it is important to do this step of data cleaning before running searches over strings.
# 
# Let's explore another method, <b>.capitalize()</b>. This method will allow you to capitalize a string.

# In[25]:


str7 = "william"


# In[26]:


print (str7.capitalize())


# I will use this in niche circumstances, particularly when I am performing data cleaning and need to ensure that all names or proper nouns in a dataset are cleaned and well-structured.
# 
# Perhaps the most useful string method is .replace(). Notice in the cells below, replace takes a mandatory of two arguments, or things passed between the parentheses. Each is separated by a comma. The first argument is the substring or piece of the string that you want to replace and the second argument is what you want to replace it with. Why is this so useful? If you are using Python to analyze texts, those texts will, I promise, never be well-cleaned. They may have bad encoding, characters that will throw off searches, bad OCR, multiple line breaks, hyphenated characters, the list goes on. The <b>.replace()</b> method allows you to quickly and effectively clean textual data so that it can be standardized.
# 
# Unlike the above methods, for .replace(), we need to put two things within the parentheses. These are known as arguments. This method requires two and they must be in order. The first is the thing that you want to replace and the second is the thing that you want to replace it with. These will be separated by a parentheses and both must be strings. It should, therefore, look something like this:
# 
# .replace("the thing to replace", "the thing you want to replace it with")
# 
# In the example below, let's try and replace the period at the end of "Mattingly."

# In[27]:


str8 = "My name is William Mattingly."


# In[28]:


print (str8.replace(".", ""))


# Excellent! Now, let's try and reprint off str8 and see what happens.

# In[29]:


print (str8)


# Uh oh! Something is not right. Nothing has changed! Indeed, this is because strings are <b>immutable objects</b>. Immutable objects are objects that cannot be changed in memory. As we will see in the next chapter with lists, the other type of object is one that <i>can</i> be changed in memory. These are known as <b>mutable objects</b>. In order to change a string, therefore, you must recreate it in memory or create a new string object from it. Let's try and do that below.

# In[30]:


str9 = str8.replace(".", "")


# In[31]:


print (str9)


# Excellent! Now we have a new string that has been cleaned, but let's say I am only interested in grabbing what comes after the phrase "My name is". I have a couple different methods to do this. I could use the .replace() method.

# In[32]:


str10 = str9.replace("My name is", "")


# Everything looks good when we print it off below, but notice, there is a leading white space before the W. This is uncleaned data. We often want to remove leading or trailing whitespaces so that all data is consistent in our dataset. We can do this by using the .strip() method.

# In[33]:


print (str10)


# In[34]:


print (str10.strip())


# Now, our data is cleaned.

# In[35]:


print (str9)


# Strings have a lot of other useful methods that we will be learning about throughout this textbook, such as the split() method which returns a list of substrings that are split by the delimiter, which is the argument of the method. By default, split() will split your string at the whitespace.

# In[36]:


print (str9.split())


# As we learn about lists in the next chapter, you will be able to use split to grab specific items from that list. Notice that in the output below, we have the same output as our method of replace and strip above. It is important to remember that in programming, there is rarely one right answer. Usually a problem can be solved many ways, but some are more efficient or easier to parse when another programmer tries to read your code.

# In[37]:


print (str9.split("My name is ")[1])


# In[38]:


#Pythonic => the standard way to do something in Python


# ## Working with Numbers as Data

# Now that you understand how strings work, let’s begin exploring another type of data: numbers. Numbers in Python exist in two chief forms:
# 
# - integers
# - floats
# 
# As noted above, integers are numbers without a decimal point, whereas floats are numbers with a decimal point. This is am important distinction that you MUST remember, especially when working with data imported from and exported to Excel.
# 
# As digital humanists, you might be thinking to yourself, “I just work with text, why should I care so much about numbers?” The answer? Numbers allow us to perform quantitative analysis. What if you want to know the times a specific author wrote to a colleague or to which places he wrote most frequently, as was the case with the Republic of Letters project at Stanford? In order to perform that kind of analysis, you MUST have a command of how numbers work in Python, how to perform basic mathematical functions on those numbers, and how to interact with them. Further, numbers are essential to understand for performing more advanced functions in Python, such as Loops, explored in Chapter 03.01.
# 
# The way in which you create a number object in Python is the to create an object name, use the equal sign and type the number. If your number has a decimal, Python will automatically consider it a float. If it does not, it will automatically consider it an integer.

# In[39]:


num1 = 1
num2 = 2


# Throughout your DH project, you will very likely need to manipulate numbers through mathematical operations. Here is a list of the common operations:
# 
# 1. Addition +
# 2. Subtraction –
# 3. Multiplication *
# 4. Exponential Multiplication **
# 5. Division /
# 6. Modulo % #This will return the remainder, e.g. 2%7 will yield 1.
# 7. Floor // #This will return the max number of times two numbers can be divided into each other, e.g. 2//7 will yield 3.

# In[40]:


print (num1+num2)


# In[41]:


print (num1-num2)


# In[42]:


print (num1*num2)


# In[43]:


print (num1/num2)


# In[44]:


print (100*8)


# In[45]:


print (num1/num2)


# In[46]:


print (num1//num2)


# In[47]:


print (5/2)


# In[48]:


print (5//2)


# In addition to this, you will very often in loops need to identify Comparison Operators (equal to, less than, etc). Here is a list of those:
# 1. Equal to (==)
# 2. Greater than (>)
# 3. Less than (<)
# 4. Less than or equal to (<=)
# 5. Greater than or equal to (>=)
# 6. Not equal to (!=)
# 
# We will address these in greater detail in a later chapter as they are particularly useful when you work with loops.

# ## Conclusion

# This chapter has introduced you two some of the essential types of data: strings, integers, floats, and booleans. It has also introduced you to some of the key methods and operations that you can perform on strings and numbers. Before moving onto the next chapter, I recommend spending some time and testing out these methods on your own data. Try and manipulate an input text to locate and retrieve specific information.
# 
# If you haven't yet installed Python, that's okay! There are free compilers online, including the one I have available at https://pythonhumanities.com/lesson-02-storing-data-in-python/. Once you feel comfortable with types of data and how to create and interact with them in Python, feel free to continue into the next chapter as we explore data structures.

# ## Quiz

# In[53]:


from jupyterquiz import display_quiz
import md2json
import json


# In[57]:


quiz = '''
# What type of data is associated with text?
mc
* Strings
-c t
-f Correct! Strings are how we create text in Python.

* Integers
-c f
-f While a type of data, Integers are not text

* Floats
-c f
-f While a type of data, Floats are not text

* Boolean
-c f
-f Booleans are not text.


# How do we create strings?
mc
* With ""
-c t
-f Correct!

* With ''
-c t
-f Correct!

* With :
-c f
-f

* With <>
-c f
-f

# What are the two types of numbers?
mc
* Integers
-c t
-f

* Floats
-c t
-f

* Strings
-c f
-f

* Booleans
-c f
-f

# What are the types of Booleans?
mc
* True
-c t
-f

* False
-c t
-f

* true
-c f
-f Close. Remember, case matters in Python.

* false
-c f
-f Close. Remember, case matters in Python.
'''


# In[ ]:





# In[58]:


myquiz = md2json.convert(quiz)
myquiz = json.loads(myquiz)
display_quiz(myquiz)


# In[ ]:





# In[ ]:




