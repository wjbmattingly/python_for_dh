#!/usr/bin/env python
# coding: utf-8

# # <center>Cultivating a Corpus</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) What to look for in a corpus<br>

# ## Introduction

# This notebook has a single purpose, to provide the steps I took to cultivate a corpus to run an EntityRuler across to cultivate a large training set. I will use this as a case study for what to look for in a corpus.

# ## Variety

# The goal of machine learning models is to be able to generalize well on unseen data. The best way to get the model to generalize well on all unseen data (or at least a lot of it), is to give the model texts is a wide variety. Variety is key when training because variety allows for a model to learn different things from different types of texts, which are written in different styles, dialects, contexts, etc. So the first thing you need to consider when putting together a corpus to generate training data from is, variety. So, with that in mind, give the model as much textual data as you can.

# ## Preparing the Corpus

# Once you have compiled documents from various sources that represent a wide range of styles, dialects, and contexts, it's time to begin preparing that corpus. At this stage, the NLP practitioner must consider *how* they want to prepare the corpus. How one prepares the corpus radically alters *what* a model learns.
# 
# Let's consider these few sentences:

# In[16]:


sent1 = "My name is William Mattingly."
sent2 = "My name is William Mattingly"
sent3 = "my name is william mattingly"
sent4 = "MY NAME IS WILLIAM MATTINGLY"


# While each of these sentences is identical to humans, but to a machine they are entirely different. Let me demonstrate what I mean.

# In[17]:


sents = [sent1, sent2, sent3, sent4]

all_words = []

for sent in sents:
    words = sent.split()
    for word in words:
        all_words.append(word)

no_duplicates = list(set(all_words))
no_duplicates.sort()
print (no_duplicates)


# In the above code, we combined all sentences into a bag of words and then removed duplicates. Notice, however, that despite removing duplicates, each word appears multiple times. This is because the computer does not see "WILLIAM", "William", or "william" as the same word. How you clean and prepare your training data will affect how your model understands its world. In other words, if you clean your data and expect your model to be given unclean data, it will not perform well. If you lowercase all your training data and your model encounters capitalized words, it will not perform well.
# 
# Cleaning and preparing data are fundamental steps in natural language processing, but when it comes to training, you, as the creator of your model, must understand how those steps will affect the performance of your model and should you take the steps to clean your data in a specific way, you should let your users know the steps you took and how data should be given to your model. You may even want to provide a few functions or classes to your users to help them clean their data and structure it in a way that you did for training.
# 
# Let's take a brief look at how we might achieve this with the code below. It is identical to the code above, except each sentence is lowercased and the period removed before being appended to the all_words list.

# In[18]:


sents = [sent1, sent2, sent3, sent4]

all_words = []

for sent in sents:
    #New line in which we lowercase and remove the period punctuation.
    sent = sent.lower().replace(".", "")
    print (sent)
    words = sent.split()
    for word in words:
        all_words.append(word)

no_duplicates = list(set(all_words))
no_duplicates.sort()
print (no_duplicates)


# By cleaning the text, we've succcessfully eliminated. However, in doing this, our model will never encounter data where proper nouns are uppercased. It will never encounter periods, either. In cleaning your data, therefore, be mindful of this.

# ## To Lemmatize or Not to Lemmatize

# Next, we must consider the question of lemmatization. We met lemmatization in notebook 01.02, but perhaps it is worth describing it again here. Lemmatization is the process by which we reduce all words to their lemma, or root. There are different libraries that perform lemmatization differently. For our purposes, we will use spaCy. Let's look at a new example in the sentences below.
# 
# In both sentences, we have almost the same meaning except the concept of time and one being entirely uppercase. Lemmatization offers the ability to make these both sentences identical.

# In[19]:


import spacy

nlp = spacy.load("en_core_web_sm")

sent1 = "The ball is his."
sent2 = "THE BALL WAS HIS."

sents = [sent1, sent2]

all_words = []

for sent in sents:
    sent = sent.lower().replace(".", "")
    doc = nlp(sent)
    new = []
    for token in doc:
        if "-" not in token.lemma_:
            new.append(token.lemma_)
        else:
            new.append(token.text)
    sent = " ".join(new)
    print (sent)
    words = sent.split()
    for word in words:
        all_words.append(word)

no_duplicates = list(set(all_words))
no_duplicates.sort()
print (no_duplicates)


# By performing lemmatization on the sentences, we were able to entirely eliminate the temporal difference between these two texts. This is occasionally a useful step in cleaning textual data for various NLP tasks, and sometimes it is good to introduce this simplified forms to texts, depending on what you want the model to do. Again, by doing this, it means a model will never encounter "was" or any non-lemmatized forms of words. Again, what you give the model, is what the model will learn.

# ## Segment the Corpus

# A final note before we wrap up this notebook is on segmentation. Text segmentation is the process by which you break up the large corpus (sometimes millions of documents) into managable sizes delinated in a single text file by line breaks (my preference). I find it is always good to think about the size of training data I want to give the model. If I am working with Latin texts, I choose a segment size that is a chapter (usually 4-20 sentences). If I am working with USHMM oral testimonies, I segment the corpus by blocks of question-answer. If I am working with regular textual data, I may segment the text at individual sentences.
# 
# Think about the size of the training data you want to give the model. I find for the process of automating a rules-based EntityRuler for generating training data, smaller sizes eliminates the potential for false negatives.

# ## Exercise

# For the exercise in this notebook, find a corpus that meets the requirements I mentioned above and expirement with different methods of cleaning that corpus.

# ## Video

# I do not have a video for this notebook, unfortunately.
