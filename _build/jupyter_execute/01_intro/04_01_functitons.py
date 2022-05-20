#!/usr/bin/env python
# coding: utf-8

# # <center>Functions</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2022</center>

# ## Covered in this Chapter

# 1) What a function is conceptually<br>
# 2) How to create a function<br>
# 3) How to assign arguments to a function<br>
# 4) How to assign variable keyword arguments to a function<br>
# 5) How to assign variable arbitrary arguments to a function<br>

# ## Introduction

# In this chapter, you will learn all about functions. You have already been exposed to several functions in this textbook, such as the print() function. My goal in this chapter is to teach you how to create your own functions.
# 
# <b>Functions</b> exist in all programming languages. They allow you to write a set of code that can be used later in your program. They are essential because they allow you to not rewrite the same block of text over and over again. Good code is code that does not repeat. In other words, if your program has a task that it needs to do repetitively, then you should develop that code into a cleaned function.
# 
# A function, as we will see has four parts:
# 1. the name of the function
# 2. the arguments passed to the function
# 3. the code
# 4. the returned piece of data (optional)

# ## Functions in Action

# I think the best way to learn about functions is to see them in action before breaking down what is happening. Let's take a look at the code below.

# In[1]:


def my_function(number):
    x = number+1
    return x


# In the above cell, I have told Python that I am creating a function by using the command "def". This is followed by the name of the function, "my_function". After this we see open and a close parentheses, between which sit the word "number". This is the argument that the function expects to take. This is then followed with our ":", which, if you remember from the previous two chapters, means that the next block of text must be indented. Whatever is indented will belong to the function.
# 
# The code of the function is "x = number+1". Before moving on, pause for a moment and think about what this function might do. Once you have an idea, proceed reading to the next paragraph.
# 
# The final portion of the cell is "return x". This is the bit of code. This will return for the user the x object that we created temporarily in the function.
# 
# Let's now call this function in the cell bellow to see how it works.

# In[2]:


result = my_function(1)


# In the code above, we have created a new object, "result". This will be the result of our function. Like all objects, it can be named whatever you like, save for the forbidden object names in Python.
# 
# We then call the function, "my_function" and pass a single argument to it, an integer. In this case, 1.
# 
# I want you to take a moment and try and guess what result will be. Go ahead and try and recreate this code in your own notebook, or, if you are using this textbook with the built-in Binder environment, create a new cell below and print off "result".

# In[3]:


print (result)


# Did you guess correctly? If so, great. If not, that's okay. Why do you think your answer was wrong? Do you understand why? These are some of the core questions you should be asking yourself at this moment.
# 
# Let's break down the function now from a logical point of view. The key piece of code is "x = number+1". This code tells Python to create a new object called "x". This will be equal to whatever the input argument, "number", is plus 1. If we give the function the number 1, then our output will be 2. Likewise, if we do this with 3, we will get 4. But what would happen if we tried to pass the string "one"?

# In[5]:


bad_result = my_function("one")


# We receive an error. This error message allows us to debug the problem. It is a TypeError, meaning we tried to use the wrong object type. We know that the error occurs in line 2 of our cell, "x = number+1". Why do you think we received this error?
# 
# If you said because "one" is a string and you cannot add a string by the integer 1, then you would be right. If we were writing this program for ourselves, we would know this and never try to pass a string to the function, but what if someone else is trying to use our code and does not know precisely what it is supposed to do? In Python, we can pass in some key information to help our users.

# ## Functions with Multiple Arguments

# In the above section, we saw a simple function that had a single argument. In Python, you can assign as many arguments you want to a function. Let's try to make a slightly different function that adds two numbers together, each supplied by the user.

# In[1]:


def my_function2(number1, number2):
    x = number1+number2
    return x


# Notice that my_function2 is the precise same as the function above except we have two arguments, "number1" and "number2". Also, in the function x is the result of number1 plus number2.
# 
# Now, let's try and use this function by passing two numbers to it: 1 and 3.

# In[2]:


result2 = my_function2(1,3)
print (result2)


# Yay! We got the result we desired. These are known as positional arguments because we are relying on the position of the argument in the function's () section. Let's modify this function slightly again so that you can see what I mean.

# In[3]:


def my_function3(number1, number2):
    print ("Number 1 is ", number1)
    print ("Number 2 is ", number2)


# In[4]:


my_function3(1, 3)


# Notice that I have deleted the return line. This is because this function does not need to return anything to the user. Instead, it's sole purpose is to simply print off what the two arguments are. Let's reverse the order of our arguments now.

# In[5]:


my_function3(3, 1)


# Because these are positional arguments, we are dependent upon the position of the arguments to assign them correctly. We can get around this by specifying which argument we want to assign things to, thus avoiding the reliance on the order in which we pass the arguments to the function. Check out the code below to see this in action.

# In[6]:


my_function3(number2=3, number1=1)


# ## Keyword Argument

# Sometimes when we create a function, we want to make it optional for the user to pass an argument. In these instances, we will create what is known as a keyword argument, something that is set to a default. In the function below, we want to give the user the option to pass a last name to the function. Notice, though, it defaults to "Mattingly".

# In[7]:


def add_surname(first_name, last_name = "Mattingly"):
    print (first_name, last_name)


# In[8]:


add_surname("William")


# That worked well, but a user still has the ability to change the last_name object.

# In[9]:


add_surname("William", "Smith")


# ## Keyword Arbitrary Arguments

# In rare instances, you will not know precisely how many arguments a user will need to pass to your function, so you want to give them the option to pass as many as they wish. In these instances, you will use what are known as arbitrary arguments. You assign these with an * before the argument name.

# In[10]:


def print_names(*names):
    for name in names:
        print (name)


# In[11]:


print_names("William", "Marge", "Sally", "Alex")


# Notice that the function has allowed the user to pass as many arguments as they wish to the function. In my entire time coding, I have only used an arbitrary argument a handful of times, but it is important to keep it in the back of your mind in case you are ever in that situation.

# ## Conclusion

# Hopefully, you now have a basic understanding about what functions are and how they work in practice. I recommend spending a few hours playing around with some basic functions to do some tasks you need to perform on your own personal data. If you get stuck, try Googling your question. You would be surprised how many responses are available. Pay particular attention to StackOverflow responses.

# ## Answer for Result

# In[4]:


print (result)


# In[ ]:




