#!/usr/bin/env python
# coding: utf-8

# # <center>Using EntityRuler to Create Training Set</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) training sets<br>
# 2) start_char<br>
# 3) end_char<br>
# 4) generating training sets<br>
# 

# ## Introduction to Training Sets

# In this notebook, we are going to be looking much more closely at training sets, what they are, why they are important, and how we can use spaCy's EntityRuler to automate the creation of a good (not great!) training dataset that will require a manual check. In the next video, I will show you how to use this training set to train a custom NER model in spaCy.
# 
# One of the nice things about spaCy, besides the fact that it scales very well (meaning it can perform well on small data and big data), is that it is easy to customize and perform advanced machine learning methods with little to no knowledge of machine learning. Understanding the basics of ML, however, as discussed in notebook 03 of this series, is helpful because it will allow you to understand *how* to cultivate a good training set and *why* certain methods may fail or struggle. In truth, you will develop of a sense of what works and what doesn't work in ML NER by simply doing it.
# 
# In Notebook 03 of this series, I mentioned that data for training a machine learning model existed in three forms: training data, validation data, and testing data. All this data will take the same form. It will be a list data structure within which each index will contain a text (a sentence, paragraph, or entire text). The length of this text will depend on what you are hoping to achieve via ML NER. The size of the text will affect the training process. For now, however, let us ignore that. The only other component the training data requires is a list of the entities in that text with their start position, end position, and label. During the training process, these annotations will allow the convolutional neural network (the architecture behind spaCy's machine learning training process), to learn from the data and be able to correctly identify the entities you are training.

# ## What Does a spaCy Training Set Look Like?

# SpaCy requires that your training data be in a very specific form:
# 
# TRAIN_DATA = [
#               (TEXT AS A STRING, {"entities": [(START, END, LABEL)]})
#               ]
#               
# Note that TRAIN_DATA is capitalized. It is Pythonic not to capitalize objects with a few exceptions. TRAIN_DATA is one of these exceptions. I don't know the history of this convention, but in every book/tutorial, you will always see TRAIN_DATA done this way. It is, of course, not necessary, but it is always good practice to be as Pythonic as possible in your code so that others will be able to more easily read your code. Any machine learning practitioner will expect to see TRAIN_DATA as such.
# 
# Getting the training data into this format is very difficult by hand. A researcher would have to count the characters to assign the start and end of the entity. Even if you consider using Python built-in string functions to get the start and end character, you will run into another problem. The way in which spaCy's training process reads the start and end characters is different than the way you may count them with the string functions. This means that in the training process, spaCy will drop the annotations that don't align with the start and end of a token. The reason for this is because of how spaCy tokenizes when compared to how your string functions tokenize the text. Fortunately, there are solutions built into spaCy via the EntityRuler to aid you in this process.
# 
# If you are interested in manual annotation, I highly encourage you to explore the paid software from Explosion AI, Prodigy (https://prodi.gy/). I am in no way being paid to promote that product. It is expensive, but if you need to do a lot of annotations (for images, text, video, or even audio), then Prodigy is the tool for you. It has a nice user-interface and because it is developed by the same team who gives us spaCy, it can fit seamlessly into a spaCy workflow. You can explore the Prodigy demo here: https://prodi.gy/demo.

# ## Creating a Training Set

# In the code below, we will make a spaCy machine learning training set via the EntityRuler. In other words, we will use a rules-based method to automatically generate a basic training set. Will this training set have mistakes? Possibly. That's why it is a good idea to look at the training set and manually verify it. By doing it in this manner, however, you can vastly increase prototyping to see if the custom entity you want to train is potentially viable. In machine learning, there are rarely concrete solutions for domain-specific problems. If there were, people wouldn't need specialists. Experimentation is often the name of the game in machine learning and it is no different with NER machine learning.
# 
# We are going to create a blank English model because we will only use this model temporarily. We don't need the other components. This model with only have an EntityRuler which we will temporarily use to generate the training set. Recall in our last notebook that the spaCy small model could not identify Treblinka correctly as a location? In the below code, we will create a basic training set from these three sentences that will allow us to generate a very small training set. I want to be clear. This training data is nowhere near enough to train a model. This process scales very well, however.
# 
# Here is the same code we saw before, but with a slightly different text. Note the output. It has correctly identified Treblinka as a GPE.

# In[1]:


#Import the requisite library
import spacy

#Build upon the spaCy Small Model
nlp = spacy.blank("en")


#Sample text
text = "Treblinka is a small village in Poland. Wikipedia notes that Treblinka is not large."

#Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler")

#List of Entities and Patterns
patterns = [
                {"label": "GPE", "pattern": "Treblinka"}
            ]

ruler.add_patterns(patterns)

doc = nlp(text)

#extract entities
for ent in doc.ents:
    print (ent.text, ent.label_)


# Now, we are going to modify this code slightly so that we can generate a slightly different output, one with the start and end of the text.

# In[2]:


#Import the requisite library
import spacy

#Build upon the spaCy Small Model
nlp = spacy.blank("en")

#Sample text
text = "Treblinka is a small village in Poland. Wikipedia notes that Treblinka is not large."

#Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler")

#List of Entities and Patterns
patterns = [
                {"label": "GPE", "pattern": "Treblinka"}
            ]

ruler.add_patterns(patterns)

doc = nlp(text)

#extract entities
for ent in doc.ents:
    print (ent.text, ent.start_char, ent.end_char, ent.label_)


# Notice now, that our output has 0,9 and 61, 71 for the start and end respectively of each entity. With this data, we can now begin to generate the output we wish. However, let's try and take the input text and break it down into sentences first to then have two different sets of training data.

# In[3]:


#Import the requisite library
import spacy

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")

#Sample text
text = "Treblinka is a small village in Poland. Wikipedia notes that Treblinka is not large."

#Create a blank list for appending later.
corpus = []

doc = nlp(text)

#use the spacy tokenizer to get the sentences.
for sent in doc.sents:
    corpus.append(sent.text)

print (corpus)


#Build upon the spaCy Small Model
nlp = spacy.blank("en")

#Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler")

#List of Entities and Patterns
patterns = [
                {"label": "GPE", "pattern": "Treblinka"}
            ]

ruler.add_patterns(patterns)



#iterate over the sentences
for sentence in corpus:
    doc = nlp(sentence)

    #extract entities
    for ent in doc.ents:
        print (ent.text, ent.start_char, ent.end_char, ent.label_)


# Notice now we have a different output with different starts and endings. Now, we can once again modify our code to get it into the format we want:
# 
# TRAIN_DATA = [
#               (TEXT AS A STRING, {"entities": [(START, END, LABEL)]})
#               ]

# In[4]:


#Import the requisite library
import spacy

#Build upon the spaCy Small Model
nlp = spacy.load("en_core_web_sm")

#Sample text
text = "Treblinka is a small village in Poland. Wikipedia notes that Treblinka is not large."

corpus = []

doc = nlp(text)
for sent in doc.sents:
    corpus.append(sent.text)

#Build upon the spaCy Small Model
nlp = spacy.blank("en")

#Create the EntityRuler
ruler = nlp.add_pipe("entity_ruler")

#List of Entities and Patterns
patterns = [
                {"label": "GPE", "pattern": "Treblinka"}
            ]

ruler.add_patterns(patterns)


TRAIN_DATA = []

#iterate over the corpus again
for sentence in corpus:
    doc = nlp(sentence)
    
    #remember, entities needs to be a dictionary in index 1 of the list, so it needs to be an empty list
    entities = []
    
    #extract entities
    for ent in doc.ents:

        #appending to entities in the correct format
        entities.append([ent.start_char, ent.end_char, ent.label_])
        
    TRAIN_DATA.append([sentence, {"entities": entities}])

print (TRAIN_DATA)


# ## Exercise

# For the exercise in this video, I'd like for you to try and replicate this process with a corpus you are familiar with. Come up with a series of rules to identify several or many of the entities you want to identify. Don't worry about finding them all. The purpose of this is to generate a good enough training set with enough diversity to teach a machine learning model in the next notebook. In the video below, I show you how to do this in a larger scale using the characters from the first book of Harry Potter.

# ## Video

# In[5]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/YBRF7tq1V-Q" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>')

