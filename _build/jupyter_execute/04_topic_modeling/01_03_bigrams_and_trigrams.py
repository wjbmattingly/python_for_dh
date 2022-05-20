#!/usr/bin/env python
# coding: utf-8

# # <center>Bigrams and Trigrams</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>February 2021</center>

# ## Key Concepts in this Notebook

# 1) unigrams<br>
# 2) bigrams<br>
# 3) trigrams<br>

# ## Introduction

# Let's take a moment and step away from the subject of this textbook, topic modeling. Instead, let's think about language, the essential medium of topic modeling. This notebook will be exclusively about one aspect of langauge: bigrams and trigrams. When we use words, those words correspond to something distinct.
# 
# If I use the word apple, you likely are thinking of something like this:
# 
# <p style="text-align:center;">
# <img src="https://i2.wp.com/ceklog.kindel.com/wp-content/uploads/2013/02/firefox_2018-07-10_07-50-11.png?fit=641%2C618&ssl=1" height="240" align="center"/>
# </p>
# 
# Apple is a simple word, yet it can mean different things in different contexts. What if I said the following: "My Apple is better than a PC." Now, what image comes to mind? Perhaps this?
# <p style="text-align:center;">
# <img src="https://images-na.ssl-images-amazon.com/images/I/71pheYd9W0L._AC_SX466_.jpg" height="240" align="center"/>
# </p>
# This is an example of textual ambiguity. Syntactical context helps eliminate textual ambiguity. Apple is a single word here that contains a single concept. It's a relatively simple word. Perhaps one of the earliest a native speaker of English learns as a child. And yet it has textual ambiguity. Because "apple" is a single word, it is known as a unigram. A **unigram** is a single word that represents a single concept.
# 
# Textual ambiguity, however, occurs in more dynamic ways when we think about concepts beyond the single span of a single word. In this notebook, we will focus on two such cases that are essential for natural language processing: bigrams and trigrams. **Bigrams** are two words that contain a distinct meaning when used together, while **trigrams** are three words that contain a distinct meaning when used together.
# 
# Understanding bigrams and trigrams are essential because in order for a computer to truly understand langauge the way a human does, it must be able to understand the nuances of a single word and how a word's meaning not only shifts in context, but shifts in meaning when used in conjunction with other words.

# ## Bigrams

# As noted above, a bigram is a combination of two words that have a distinct meaning. To demonstrate this, let us consider quickly the word "French". A single word, that may have multiple meanings. Perhaps the word French refers to the language:
# <p style="text-align:center;">
# <img src="https://www.unb.ca/cel/_assets/images/enrichment/ll-fred/ll-french-beginners.jpg" height="240" align="center"/>
# </p>
# Perhaps it references a French person:
# <p style="text-align:center;">
# <img src="https://images.movehub.com/wp-content/uploads/2017/09/15150656/living-in-france.jpg"  height="240" align="center"/>
# </p>
# Let's hold off on the word French for just a moment. Let's now use the word "revolution". Again, there is textual ambiguity, but perhaps I am referencing the concept of revolution in the sense of the Earth.
# <p style="text-align:center;">
# <img src="https://i.ytimg.com/vi/CqkQv617bcw/maxresdefault.jpg" height="240" align="center"/>
# </p>
# 
# Now you may already see where I am going with this, but let's now think about what happens when I put those two textually ambiguous unigrams together "The French Revolution". "The" here is a stop word that is frequently dropped in natural language processing, so "French Revolution" is all that we should consider. This two words when combined have a distinct concept. Now, you may be thinking of this:
# <p style="text-align:center;">
# <img src="https://images.immediate.co.uk/production/volatile/sites/7/2018/04/GettyImages-917743986-5ffaa22.jpg?quality=45&resize=768,574" height="240" align="center"/>
# </p>
# But we can think about language in even more nuanced ways.

# ## Trigrams

# Trigrams, as noted above, are the same as bigrams, except with three words, instead of two. Let's continue with our example of "French". What might you think about if I used the word "army". Perhaps something distinct to your own experiences with the word. For me, as a modern American, I think initially about the American Army in the modern sense of the word. So I may picture something like this:
# <p style="text-align:center;">
# <img src="https://www.goarmy.com/content/dam/goarmy/refresh/redesign-nav-images/Desktop_Navigation_IMG_1.jpg" height="240" align="center"/>
# </p>
# For others in other parts of the world, other images may be more relevant. However, when I use the phrase "The French Revolutionary Army", I now have something defined, something distinct. I have this:
# <p style="text-align:center;">
# <img src="https://upload.wikimedia.org/wikipedia/commons/4/47/Bataille_Jemmapes.jpg" height="240" align="center"/>
# </p>
# This is a trigram, a distinct concept consisting of three words that may have individual meanings when used alone.

# ## Why are these Important?

# So, why are bigrams and trigrams so important? The reason comes down to getting machines to understand that when certain words are used together, they bear a distinct meaning. In order to produce a good topic model, therefore, the model must be able to understand and process words in this manner, the way we humans use the language we are trying to get the machine to understand.

# In[5]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/GBQFelgzjKQ" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# In[ ]:




