#!/usr/bin/env python
# coding: utf-8

# # <center>Creating Location Pipe for Holocaust NER</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) How to add pipes to a spaCy model<br>
# 2) How to custom labels to NER pipe<br>

# ## Introduction

# In this notebook, we will cover how to create a blank spaCy model, load in pipes from another model, save that new model. We will also work with custom entities.

# ## Creating a Blank spaCy Model

# Whenever you are creating a custom spaCy model, it is usually a good idea to start with a blank model. Let's do that first. The spaCy blank class takes one argument, the language. In our case, we want to create a blank English model. The language affects how spaCy will tokenize the text.

# In[2]:


import spacy

main_nlp = spacy.blank("en")


# Our goal now is to take the NER pipeline from the spaCy small English model and inject it into our blank model First. We need to grab the English model.

# In[3]:


en_model = spacy.load("en_core_web_sm")


# Next, we need to grab specifically the NER pipe. We can do that with the function get_pipe(). This will take one argument, the pipe desired. Because we want to grab the NER pipe, we will specifcy "ner".

# In[4]:


ner = en_model.get_pipe("ner")


# Now that we have that pipe, we can add it to our blank spaCy model using the add_pipe() function.

# In[5]:


main_nlp.add_pipe(ner)


# Now that we have that added to our main_nlp pipeline, let's test it out and make sure that it works.

# In[6]:


sent = "Hello, my name is Bob and I live in the United States."

doc = main_nlp(sent)
for ent in doc.ents:
    print (ent.text, ent.label_)


# Notice that our blank model now can use the ner pipe from the small English spaCy model. Success.

# ## Saving a spaCy Model

# Saving a spaCy model is just as simple. Let's go ahead and save our blank model before moving forward. We can do this with the to_disk() function. This will take one argument, the location we want to save it to. We are going to put it in the subfolder models.

# In[8]:


main_nlp.to_disk("models/sample_model")


# ## Placing Pipes

# Sometimes, we will want to make more sophistocated pipelines where we have multiple pipes. In these scenarios, we will want to place specific pipes in specific locations. Let's try and work through how to do that.
# 
# We can do this several different ways. First, we can place pipes in order in our script. The last pipe added will be the last pipe in the pipeline. In the code below, we add English and German NERs to our pipeline. If we do this, however, we will get an error:

# In[12]:


import spacy

main_nlp = spacy.blank("en")

en_ner = spacy.load("en_core_web_sm").get_pipe("ner")
de_ner = spacy.load("de_core_news_sm").get_pipe("ner")

main_nlp.add_pipe(en_ner)
main_nlp.add_pipe(de_ner)


# The reason we are getting this error is because we are trying to add two NER pipes that have the same name, "ner". We need to give each of these a unique name. We can do this with the code below and then we will iterate over the pipeline to make sure we have all the pipes listed correctly.

# In[14]:


import spacy

main_nlp = spacy.blank("en")

en_ner = spacy.load("en_core_web_sm").get_pipe("ner")
de_ner = spacy.load("de_core_news_sm").get_pipe("ner")

main_nlp.add_pipe(en_ner, name="en_ner")
main_nlp.add_pipe(de_ner, name="de_ner")

for pipe in main_nlp.pipeline:
    print (pipe)


# Notice in the output that we not only get the correct pipes with unique names, we also get them in the order we expected. Let's try and put the German model in front of the English one. To do that, we can pass an argument. You can use either before or after, depending on how you want to place the pipe. We will use before="en_ner".

# In[15]:


import spacy

main_nlp = spacy.blank("en")

en_ner = spacy.load("en_core_web_sm").get_pipe("ner")
de_ner = spacy.load("de_core_news_sm").get_pipe("ner")

main_nlp.add_pipe(en_ner, name="en_ner")
main_nlp.add_pipe(de_ner, name="de_ner", before="en_ner")

for pipe in main_nlp.pipeline:
    print (pipe)


# Placement of specific pipes in a specific order is essential because later pipes receive the data of the earlier pipes. In the case of NER, this means that later pipes cannot overwrite earlier pipes, unless we give them permission.

# ## Adding Custom Labels

# In order to best demonstrate how to add custom labels, it is best to watch the video below.

# ## Exercise

# Try to create some custom pipelines for fun. See how they perform on texts when ordered in specific ways.

# ## Video

# In[16]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/1l3v2Zcgb3s" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')

