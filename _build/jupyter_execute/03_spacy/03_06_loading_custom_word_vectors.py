#!/usr/bin/env python
# coding: utf-8

# # <center>Loading Custom Word Vectors into a spaCy Model</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) How to load word vectors into a spaCy model<br>
# 

# ## Loading Word Vectors

# This notebook will be short. It has one purpose, to provide the code necessary for loading word vectors into a blank spaCy model. We will use the word vectors we created in the last notebook: data/word_vecs.txt. There are two different ways to load word vectors into a spaCy model, either via command line (demonstrated in video) or via a Python script using subprocess and sys. I prefer the latter because I can automate the creation of blank spaCy models. I detail both of these methods in the video below. The code is explained in more depth in the video as well.

# In[3]:


def load_word_vectors(model_name, word_vectors):
    import spacy
    import subprocess
    import sys
    subprocess.run([sys.executable,
                    "-m",
                    "spacy",
                    "init-model",
                    "en",
                    model_name,
                    "--vectors-loc",
                    word_vectors
                        ]
                    )
    print (f"New spaCy model created with word vectors. File: {model_name}")
load_word_vectors("data/sample_model", "data/word_vecs.txt")


# You will now be able to call the blank spaCy model, like so:

# In[6]:


import spacy

nlp = spacy.load("data/sample_model")


# ## Exercise

# Try to load the custom word vectors you created from the exercise in the last notebook into a blank spaCy model.

# ## Video

# In[5]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/aQPMWS6XiI8" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>')


# In[ ]:




