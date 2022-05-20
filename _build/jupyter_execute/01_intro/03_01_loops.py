#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Loops</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) What are Loops?<br>
# 2) Iterations<br>
# 3) Why are Loops Important?<br>
# 4) For Loops<br>
# 5) While Loops<br>

# ## What are Loops?

# Loops are a fundamental concept in all programming languages. They are essential in nearly every piece of code that I write and my experience is far from unique. Loops are essential because they allow you to systematically iterate over data. <b>Iteration</b> is the process by which you move across a piece of data or collection of data. As we will learn in this chapter, there are two types of loops in Python:
# 
# 1. For Loops
# 2. While Loops
# 
# While most tasks can be achieved with either loop, the way in which you use them is different. By the end of this chapter, you will understand not only how to construct a loop in Python, but have a general idea about when to use which loop. As you code more and more, you will learn that coders tend to favor one type of loop over the other. For me (pun intended), I prefer the for loop. If you asked me why, I could not give you an answer. Maybe by the end of this chapter, you will have a favorite as well!

# ## For Loops

# A good way to think about a for loop is to first imagine in your mind a list of names:
# 
# Tom, Nancy, Drew, Steph
# 
# Notice that in our list above, we have four names. Each name is separated by a comma. The for loop allows us to move across this list where each comma occurs. Still to this day, when I write a for loop, I say the following in my mind:
# 
# "For each item in this list, do something."
# 
# Let's imagine that we wanted to use Python to print off each of the names. I would say in my mind:
# 
# "For each item in this list, print off the name".
# 
# I have not written a single bit of code, rather expressed a type of logic, or series of operations in regular English. This is known as pseudo-code, or false code. The above statement in English will not work if I wrote it in a Python file, but it allows for me to get the logic of what I want to do down on paper. Next, I would need to write out this logic into normal Python syntax. Let's try and do that now.
# 
# First, let's make a list of names by creating an object named namelist.

# In[2]:


namelist = ["Tom", "Nancy", "Drew", "Steph"]


# Great! Now that we have our namelist object, let's try and iterate over it, or pass over each item in that list. To do this in Python, we would write something like this:

# In[4]:


for name in namelist:
    print (name)


# Let's break down a series of things that are happening here. We start off by writing "for". This tells Python that we are about to enter a for loop and that it should check for proper syntax. Next, we have the word "name". This is an object that will be created in memory and changed each time the loop iterates over the next item in the expression, "namelist". This word "namelist" corresponds to the object name that I want to iterate over. Finally there is a ":". In Python, this is the way that we note a nested portion of code. We will use these in nearly every script we write because we frequently need to nest items in code. Once Python sees a ":", it will expect the next line to be indented.
# 
# On the next line, we have an indent followed by print, the function that we met in Part 2. Next, we have what we want to be printed, the object name. In other words, we want each name that is temporarily created in memory to be printed off.
# 
# Notice in the block of code below, I have changed the object "name" to "item". The name here does not matter. It is simply a word that will indicate the name of the object that you are creating. It is considered Pythonic, or good form, to select a name for the object that makes sense. Because this is a namelist, it makes sense to use the word "name" for that object name so that others who read your code will understand it better.

# In[3]:


for item in namelist:
    print (item)


# While being able to print things off in a for loop is useful, especially when debugging, usually for loops are used to modify data in some capacity. In the cell below, I want to be able to create a new list based on the list of names in namelist. However, I know that all individuals in that list have the last name "Mattingly". I could manually add the last name Mattingly to each individual person, but that would be tedious and, if I had a list of thousands of names, impractical.
# 
# Within the for loop, therefore, I want to modify the existing string and add it to the new list, "new_names". We can modify a string in several ways. For now, we will use the simpler approach of simply adding a plus sign (+) between the object name and the new piece of information I want to add to it, " Mattingly"

# In[4]:


new_names = []
for name in namelist:
    print (name+" Mattingly")
    new_names.append(name+" Mattingly")


# Now that we have executed the cell above, let's see how our new list looks. Let's print it off.

# In[9]:


print (new_names)


# Viola! Like magic, we have brought two different pieces of data together in a for loop. But there is another kind of loop in Python, the while loop.

# ## Operators

# In Chapter 02-01, we met briefly operators. I mentioned them there so that you were aware of them and because they most often associated with numbers, but as we will see, these can be used on all types of data. We will very often in loops need to identify Comparison Operators (equal to, less than, etc). Here is a list of those:
# 
# 1. Equal to (==)
# 2. Greater than (>)
# 3. Less than (<)
# 4. Less than or equal to (<=)
# 5. Greater than or equal to (>=)
# 6. Not equal to (!=)
# 
# Operators allow us to return a Boolean (True or False) about the question we pose with them. Say, for example, we wanted to know if 1 was less than 2. This is True, but in Python we could structure it like so:

# In[12]:


print (1 < 2)


# We could also structure the false statement of if 1 is greater than 2.

# In[13]:


print (1 > 2)


# Or even if 1 is equal to 2. Notice the double = here. We have to use two = because one = in Python sets up a new variable.

# In[14]:


print (1 == 2)


# In math, we use an equal sign with a slash through it to state not equal to, but in code that does not work so cleanly because it is not a character on the keyboard. Instead, we use !=. Believe it or not, you will get really good about writing != over time. If we wanted to see if 1 is not equal to 2, we would write this:

# In[15]:


print (1 != 2)


# On the surface, it may seem like you would never need to use comparison operators. You know that 1 is not equal to 2. In fact, you will use them all the time because comparison operators allow for you to leverage Boolean logic, or True-False logic. This is particular useful in loops. A good way to demonstrate this is with a while loop.

# ## While Loops

# These operators allow us to structure complex conditions within our loop. So, we can say that while something is equal to something else, Python should do x. We will see this same concept in the following chapter as we explore conditionals. I think the best way to learn about this concept is to jump in and explore it.
# 
# In the for loop, the loop iterated over a set of data. A while loop is a bit different. In a while loop, the loop will run continuously while something is true. Like the for loop, we create the loop with a set of commands beginning with its name, while. Next we state the condition to be met that will result in breaking, or stoping the loop. Let's say we wanted to count from 0 to 10. We would create an object named x and set that equal to our start position. Then we would state so long as x != (not equal to) 10, print off x. In order to ensure that x ticks up, we need to make sure that we change the object from x to x+1 so that it moves up by 1 number each time.

# In[10]:


x=0
while x != 10:
    print (x)
    x=x+1


# I know I have stated this before, but it is worth mentioning again. In coding, there us usually never one way to do a task. Notice in the block of code below what is different? Why don't you take a look at it and see if you can figure out precisely what is happening and why it succeeds in performing the same task.

# In[11]:


x=0
while x < 10:
    print (x)
    x=x+1


# ## Quiz

# In[6]:


quiz = '''
# Which of the following is an operator?
mc
* <
-c t
-f

* >
-c t
-f

* =
-c f
-f Close. Remember = is used in Python to create a variable. == is it's operator form.

* !=
-c t
-f

# What are the two kinds of loops in Python?
mc

* For
-c t
-f

* While
-c t
-f

* If
-c f
-f

* Then
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




