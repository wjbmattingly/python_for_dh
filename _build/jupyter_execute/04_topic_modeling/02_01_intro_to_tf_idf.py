#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to TF-IDF</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>February 2021</center>

# ## Key Concepts in this Notebook

# 1) TF-IDF<br>
# 2) Term Frequency<br>
# 3) Inverse Document Frequency<br>

# ## Introduction

# The key subject of this notebook is TF-IDF, or Term Frequency-Inverse Document Frequency. **TF-IDF** is an algorithm for determining the relevancy of words in a given document, respective to the corpus in which it sits. It is a fundamental method for search retrieval in search engines. This notebook will explore not only what TF-IDF is, but the math behind it. While understanding the math is not essential, it will give you a much clearer sense of *how* TF-IDF works and, more importantly, when to use it.

# ## Meaning of TF-IDF

# As noted above, TF-IDF stands for Term Frequency-Inverse Document Frequency. What does that mean? It means the frequency of a given term respective to that word’s frequency on all other documents. In theory, this basic algorithm will result in a number that tells you how significant a word is not only within the document, but also how significant that document is for a search of that term. In order to understand this, however, it is essential to explore the math. I have found that the best way to explore the math is to break the algorithm into its two components: TF and IDF. 

# ## Term Frequency

# Let’s first explore Term Frequency. **Term Frequency** means the frequency of a given term. To calculate term frequency, it is actually quite intuitive and simple. We simple calculate how frequently that term appears in a given document, i.e. a percentage. So, if we have a document that is 100 words long and a term appears 30 times, that term would have a term frequency of .3, or 30%.

# ## Inverse Document Frequency

# The second part of this algorithm is Inverse Document Frequency. **Inverse Document Frequency** is a little more complex, but simple if broken down. Let’s imagine that a corpus has 10,000 documents in it and 352 documents mention the same term referenced above. First, we need to calculate what percentage of documents contain that term. To do this, we would simply divide 10,000 by 352. That gives us approximately 28.41. To calculate the IDF, however, that is not enough, we must log() that number. The logarithm flattens out the number to make the number more proportional to the number. So, when we do log(28.41), we get 1.45 (to see this in action, watch the video below). This means that the IDF is 1.45.

# ## Bringing it all Together

# Now that we have our TF (.30) and our IDF (1.45), we can now bring this algorithm together. To do that, we simply multiple the two numbers, i.e. .3 x 1.45. When we do that, we get the number .44, this is our TF-IDF score. If this was confusing at all, I encourage you to watch the video below in which I walk you through how to do this with a calculate. In later notebooks, we are going to see how to do this in Python with Scikit-Learn.

# ## Video

# In[4]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/YtuydcHCkK8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# In[ ]:




