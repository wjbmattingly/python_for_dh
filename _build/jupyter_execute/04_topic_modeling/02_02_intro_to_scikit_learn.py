#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Scikit Learn</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>February 2021</center>

# ## Key Concepts in this Notebook

# 1) Scikit Learn<br>
# 2) Algorithm<br>
# 3) How to Install Scikit Learn<br>
# 4) Why Scikit Learn is important<br>
# 5) Common Problem with NumPy on PC<br>

# ## Introduction

# In this notebook, you will meet a powerful and important Python library: Scikit-Learn, or Sklearn (often pronounced S-K-Learn). For humanists, Sklearn is a library that is used when necessary. It is rarely a library that one devotes significant time to learning. This, however, drastically limits the capabilities of the humanist. While sklearn is more often used in the sciences, its potential for use in the humanities is vast, especially in when it comes to certain tasks in text analysis, namely topic modeling and data clustering.
# 
# As we explore TF-IDF in Part Two of this notebook, we will see the power of Sklearn as we use it to perform two tasks. First, we will use it to perform TF-IDF. This will get all documents to a set of a key words. We will then use those key words to harness another feature of Sklearn, KMeans. We will use KMeans to cluster the keywords to identify topics present in our sources. If you are unsure what all this means, by the end of Part Two, you will not only understand these concepts and terms, you will also know how to do it in Python.
# 
# Before we begin to explore the code, however, it is vital that you have a basic understanding of the key library, Sklearn, its features, and how to install it correctly. This notebook will cover these ideas as well as some of the potential problems you may encounter while installing Sklearn on a Windows PC.

# ## What is Scikit-Learn?

# **Scikit-Learn** is a powerful Python library often used by the sciences. In the sciences, Scikit-Learn is a necessary library and one that is encountered early in coding courses on Python. The reason? Because it provides users with easy-to-implement algorithms. An **algorithm** is nothing more than an algebraic formula designed to have a specific output based on a set of rules designated as variables. Rather than writing out algorithms manually in Python, Scikit-Learn allows users to select an algorithm and pass variables to the algorithm. Most importantly, it allows for significant and custom tweaking to these algorithms so that complex tasks can be achieved often in a single line of code.
#  
# In addition, Scikit-Learn provides easy-to-use clustering algorithms so that in a single line of code a user can cluster data and achieve complex analysis relatively simply. In the image below, we can see an example of K-Means clustering, discussed in more depth in Notebook 01.02.
# 
# <p style="text-align:center;">
# <img src="https://d2908q01vomqb2.cloudfront.net/f1f836cb4ea6efb2a0b1b99f41ad8b103eff4b59/2018/11/02/k-means-sagemaker-1.gif" height="240" align="center"/>
# </p>
# 
# Most advanced Python libraries sit on top of, or depend on, Scikit-Learn. In machine learning, practitioners often use Scikit-Learn to implement standard machine learning algorithms or create rudimentary neural networks. Prior to TensorFlow/Keras and Pytorch/FastAI, this was the chief library in Python for handling machine learning.
# 

# ## Why Scikit Learn is Important

# All of this explains why Scikit-Learn is important for the sciences, but why is it important for humanists? In order to perform distant reading, humanists need to be able to leverage computational methods for understanding documents en masse. In order to do that, the documents must be efficiently processed by a computer system. This is achieved via algorithms and clustering. In other words, for text analysis, Scikit-Learn should be a familiar library. While the original intention behind Scikit-Learn was for the analysis of data, the same methods can be used for the analysis of text. All the humanist needs to do, is to learn how to get the data into an appropriate form for parsing by the Scikit-Learn functions. That is what we will be covering in the next notebook.

# ## How to Install Scikit-Learn

# The biggest hurdle for using Scikit-Learn is installing it. In order to install Scikit-Leran, visit their <a href="https://scikit-learn.org/stable/install.html" target="_blank">docs installation page</a> and select the options that conform to your system. Select your operating system (Windows, macOS, or Linux), then packager (pip or conda) and finally if you are using a virtual environment. If you are not familiar with virtual environments, keep that turned off. Once selected, there will appear code that you can copy and paste into your terminal to install Scikit-Learn, i.e. pip install -U scikit-learn.

# ## Common Problem with NumPy on Windows PC

# If you are on Windows, you may encounter a problem in the installation process with the dependency NumPy. In order to install NumPy Correctly, I recommend doing it manually with the Math Kernal Library, the file is found <a href="https://www.lfd.uci.edu/~gohlke/pythonlibs/" target="_blank">here</a>. Watch the video below for instructions on how to resolve this problem.

# In[1]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/21Zip60GW1A" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# In[ ]:




