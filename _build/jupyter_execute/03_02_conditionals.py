#!/usr/bin/env python
# coding: utf-8

# # <center>Conditionals</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) What conditional statements are<br>
# 2) What the logic is behind them<br>
# 3) If<br>
# 4) Else<br>
# 5) Elif (or if)<br>
# 6) The in Operator<br>
# 7) The not in Operator

# ## Introduction

# Like Loops, Conditionals are an essential component of all programming languages. <b>Conditionals</b> are a type of logic in programming that allow you to control if something happens based on condition that something is true or false. Conditionals are always binary. I always find it useful to think about conditionals in plain English first.
# 
# If something is true, then do this. If that something is not true, then you can specify what should happen if that is the case. In pseudo code, it would look something like this:
# 
# If something is true:
# 
#     do this
# Otherwise:
# 
#     do this instead.
#     
# Notice again the indentation. As we progress throughout this chapter, you will learn three essential components of conditional statements:
# 
# 1. if
# 2. else
# 3. elif (or if)

# ## If Statement

# Let's first practice the if statement. In Python, you will need something to test if it is true. Let's create an object called x and make it equal to 0. Now, we can say if x is equal to 0, then print it off. Notice in the code below the ":" and the indentation afterwards, just as we saw with loops.

# In[1]:


x=0
if x==0:
    print (x)


# Let's try and state the opposite of this. Let's set our condition to x being equal to 1.

# In[2]:


if x==1:
    print (x)


# Notice that nothing happens.

# ## Else Statement

# If we want something to occur if that condition is not met, we can use the Else statement. Think of else as "otherwise" in English. If this condition it met, do this; otherwise, do something else. Let's write that out in real code.

# In[3]:


if x==1:
    print (x)
else:
    print ("X is not 1")


# Notice that else has the same indentation placement as the if and it too has a ":" followed by indented code. This allows us to create complex logic within our code. You will find yourself using conditional more often than you may realize now.

# ## Elif and the 'in' Operator with Strings

# I debated including elif in this chapter for fear that it may introduce too many new things at once, but I think it is import to at least be familiar with its existence, even if you will not be using it right away. Elif, in plain English, means "or if".
# 
# If condition 1 is met:
# 
#     do this
# Or if condition 2 is met:
# 
#     do this instead
# 
# Within this paradigm, it functions a little differently than else in that another condition must be met for it to occur, but it functions a little differently than a regular if statement. Let me demonstrate this in code.
# 
# In the code below, you will see within the conditional the word **"in"**, known as an operator. In Python, in functions rather like the way it functions in English. It is used to test if something is inside a piece of data or a data structure. So, if we want to know if some string is within another string, we can use in to see if that is the case.

# In[4]:


text = "I know two people. Marge and Susan."
if "Marge" in text:
    print ("Marge Found")
elif "Susan" in text:
    print ("Susan Found")


# This output may appear to be surprising. Both Marge and Susan are in the string, "text". Why, then, do we not see "Susan Found" printed off? The reason is because elif only is triggered if one of the preceding if or other elif statements has not been triggered. If I wanted to check if both conditions were met, I would, instead, use two if statements, like so:

# In[5]:


if "Marge" in text:
    print ("Marge Found")
if "Susan" in text:
    print ("Susan Found")


# The elif statement allows for more robust logic and sequential conditionals to occur.

# ## Conditionals and Lists with 'in' and 'not in'

# Conditionals are frequently necessary when checking to see if something is in a list. Remember, lists are data structures that contain a list of data. These can be strings, integers, floats, or even other data structures, such as lists, tuples, and dictionaries. You will frequently need to understand what a list contains. To do this, we can use conditionals with the same in operator that we saw above.
# 
# Let's begin by first making a list called names.

# In[17]:


names = ["Terry", "Marge", "Joanne"]


# In[18]:


if "Marge" in names:
    print (True)


# The in operator has a negative version to, **'not in'**. This operator functions precisely the same way, but it is the opposite of the in operator. Let's see it in action.

# In[19]:


if "Tom" not in names:
    print ("Tom is not in the list.")


# ## Conclusion

# This chapter has introduced the three essential components of conditional statements: if, else, and elif. I would recommend practicing with these on your own data. The best way to learn about conditionals is to use them. Remember, as you write them in Python, speak out loud in English. I still speak aloud (or in my mind) pseudo code as I write in proper Python syntax.

# ## Quiz

# In[15]:


quiz = '''
# What are the three words you use to create conditional statements?
mc
* if
-c t
-f

* elif
-c t
-f

* else
-c t
-f

* then
-c f
-f

# Conditionals require you to indent.
mc
* True
-c t
-f

* False
-c f
-f

# Conditionals allow you to structure binary logic in your code.
mc
* True
-c t
-f

* False
-c f
-f

# Which of the following is a good example of a conditional statement?
mc
* if x > 0:
-c t
-f

* if x > 0
-c f
-f Remember, in Python a conditional statement should be followed by :

* if x = 0:
-c f
-f Remember, you use a double = to state equal to

* If x > 0:
-c f
-f Incorrect. Note the capitalized I in If
'''


# In[16]:


from jupyterquiz import display_quiz
import md2json
import json
myquiz = md2json.convert(quiz)
myquiz = json.loads(myquiz)
display_quiz(myquiz)


# In[ ]:




