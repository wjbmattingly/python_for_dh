#!/usr/bin/env python
# coding: utf-8

# # <br><center>How to Train spaCy NER Model</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) Preparing Data for Training<br>
# 2) Converting Training Data to .spacy Binary<br>
# 3) How to Create a spaCy 3 config.cfg File<br>
# 4) How to Train a Model in spaCy 3

# ## Introduction to Training a Machine Learning Model in spaCy

# In the last notebook, we created a basic training set for a machine learning model using spaCy's EntityRuler. We were able to do this by making certain presumptions about things that are very likely or certainly going to fall under a specific label. Such an approach to cultivating a training set is, by its nature, problematic. It will miss some entities and falsely label others. If one wishes this to be the essential training set used to train a final model, I encourage a manual check. If, however, you want to use this model as a baseline model that can be used to cultivate a better training set via Prodigy, then this method will also work.
# 
# In this notebook, we will not be interested in the refining of this training set, rather the use of it to train a custom spaCy machine learning NER model. The methods, therefore, will receive the chief focus on this notebook, not the results.
# 
# In 01.04: Machine Learning NER, we first met machine learning and some of the fundamentals of it. If you have not viewed that notebook and the videos within, I encourage you to do so prior to working through this notebook as I will be assuming that you have a basic understanding of machine learning.
# 
# The reason I prefer spaCy over other NLP frameworks is spaCy's ability to scale well (work on both small and big data) and it's easy-to-use training process. An NER practitioner does not have to create a custom neural network via PyTorch/FastAI or TensorFlow/Keras, all of which have a steep learning curve, despite being some of the easiest frameworks to use. Instead, users of spaCy can take advantage of the predesigned CNN architecture behind the spaCy training process. In version 3.0 of spaCy (nightly is available at the time of writing this notebook), due in early 2021, the user will also be able to customize this neural network architecture, expanding spaCy's utility and customizability.
# 
# In order to take advantage of the spaCy training process, the user need only understand a few basic concepts, such as how the data should look going into the training process (covered in the last notebook) and a few hyperperameters (the things we adjust in the training process to try and find optimal results).

# ## Preparing the Data

# As noted in the last notebook, your input data should be in the following format:
# 
# TRAIN_DATA = [
#               (TEXT AS A STRING, {"entities": [(START, END, LABEL)]})
#               ]
# 
# To begin, let's bring in the code from the last video to generate our training data:

# In[5]:


import spacy

nlp = spacy.load("en_core_web_sm")
text = "Treblinka is a small village in Poland. Wikipedia notes that Treblinka is not large."
corpus = []

doc = nlp(text)
for sent in doc.sents:
    corpus.append(sent.text)

nlp = spacy.blank("en")

ruler = nlp.add_pipe("entity_ruler")

patterns = [
                {"label": "GPE", "pattern": "Treblinka"}
            ]

ruler.add_patterns(patterns)

TRAIN_DATA = []
for sentence in corpus:
    doc = nlp(sentence)
    entities = []

    for ent in doc.ents:
        entities.append([ent.start_char, ent.end_char, ent.label_])
    TRAIN_DATA.append([sentence, {"entities": entities}])

print (TRAIN_DATA)


# ## How to Convert the Training Data to spaCy Binary Files

# In a previous version of this textbook, we used spaCy 2. The way in which we train in spaCy 3 is entirely different. While it is possible to work through some of the fundamentals in a script, I think it is best done in the terminal. Because this textbook is a JupyterBook, which sits on top of many Jupyter Notebooks, we can execute terminal-based commands with an ! at the start of a cell. In order to train a machine learning model, the first thing that we need to do is to create a spaCy binary object of that training data. I find it is always good to use a function if a bit of code is going to repeated in the future, that way it can be reproducible. The following function is available on spaCy's repo: https://github.com/explosion/projects/blob/v3/pipelines/ner_demo/scripts/convert. I modified it slightly to work better in this textbook.
# 
# Let's break down what this function is doing. It's entire purpose is to convert our spaCy 2 formatted TRAIN_DATA into spaCy 3 binary training data. In my workflow, I like to keep these two steps separate. The reason is that I like to be able to examine and verify my training data prior to converting it to spaCy 3 binary format. It allows for one final quick manual validation. The function takes three arguments:
# 
# 1) lang => this will be the language of the blank model. Use "en" for English, "de" for German, etc.<br>
# 2) TRAIN_DATA => this will be the training data as a list of lists like we saw above.<br>
# 3) output_path => this will be the output directory in which the spaCy binary file will sit.<br>
# 
# The nice thing about this function is if your training data does not align, it will simply be ignored. This will prevent errors in the training process. In order for this function to work, it needs to create a DocBin object to save. The **db = DocBin()** allows us to run **db.add()** and add in our training data individually. These are then converted to binary objects (smaller in size and faster to load). and saved to disk with **db.to_disk()**.

# In[11]:


import srsly
import typer
import warnings
from pathlib import Path

import spacy
from spacy.tokens import DocBin

def convert(lang: str, TRAIN_DATA, output_path: Path):
    nlp = spacy.blank(lang)
    db = DocBin()
    for text, annot in TRAIN_DATA:
        doc = nlp.make_doc(text)
        ents = []
        for start, end, label in annot["entities"]:
            span = doc.char_span(start, end, label=label)
            if span is None:
                msg = f"Skipping entity [{start}, {end}, {label}] in the following text because the character span '{doc.text[start:end]}' does not align with token boundaries:\n\n{repr(text)}\n"
                warnings.warn(msg)
            else:
                ents.append(span)
        doc.ents = ents
        db.add(doc)
    db.to_disk(output_path)


# In[21]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/TKoPva69_6E" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe></div>')


# Now that the function is ready, we can call. In this simple, toy example, we are going to do (intentionally) a major mistake in ML. We are going to use not only a small training data sample (only 2), we are going to use both for training and validation. I cannot stress this enough. NEVER DO THIS. We are doing it here, simply to establish a workflow and demonstrate some of the problems that this method of small training data can present.

# In[12]:


convert("en", TRAIN_DATA, "data/train.spacy")
convert("en", TRAIN_DATA, "data/valid.spacy")


# ## What is the spaCy config.cfg File and How do I create it?

# Now that we have our training data ready, it's time to start preparing our model. In spaCy 3, we have a lot of control over the neural network architecture and hyperperameters of our model. This all takes place in the new config.cfg file. This config file is giving to spaCy during the training process so that it knows what to train and how. In order to create the config.cfg file, we first need to create a base_config.cfg file. To do that, we can use spaCy's handy GUI, found here: https://spacy.io/usage/training (scroll down a bit). You will find something that looks like this:

# <img src="images/spaCy_config_gui.JPG" width=600>

# For our purposes, select, "English", the language that we are training, "ner" only, the model we are training, "CPU" (GPU is a bit more complex), and efficiency (quicker to train and smaller because there are no word vectors). You will copy and paste the output in the GUI into your directory as "base_config.cfg". We will only make two minor changes to this base_config.cfg file. We will specify the path of train and dev (seen under the first category of paths). We will set these to the location of our train.spacy and valid.spacy files.

# <img src = "images/paths.JPG">

# Now that the base_config file is setup correctly, it's time to convert it to a config.cfg file. To do that, we need to execute a terminal command. Fortunately, we can do that here in Jupyter Notebook. I have placed my base_config file in the subfolder data. By running the command below, spaCy reformats the base_config into a properly formatted config.cfg file.

# In[16]:


get_ipython().system('python -m spacy init fill-config data/base_config.cfg data/config.cfg')


# In[28]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/l67PXnhu0ig" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>')


# With the config.cfg file in place, we can train our first model. In our case, I will be placing our models in the subfolder models/output. We run the command below, and we have a trained model.

# ## How to Train a spaCy 3 Model from the config.cfg File

# In[17]:


get_ipython().system('python -m spacy train data/config.cfg --output ./models/output')


# The above output tells us the epochs, the number of samples, as well as some metrics for our model. Our model shows 100%, but this does not mean we have a good model. It is overfitted, meaning it essentially memorized one sample, Treblinka. Nevertheless, let's load up the model and see how it performs.

# In[18]:


trained_nlp = spacy.load("models/output/model-best")
text = "The village of Treblinka is located in Poland."
doc = trained_nlp(text)

for ent in doc.ents:
    print (ent.text, ent.label_)


# Note that we gave the machine learning model NER a new sentence and it correctly identifies Treblinka as a "GPE". But we should not get too excited. Minor alterations to this text result in a missed entity.

# In[20]:


text = "Mark, from New York, said that he wants to go to Treblinkaa to speak to the locals."
doc = trained_nlp(text)

for ent in doc.ents:
    print (ent.text, ent.label_)
if len(doc.ents) == 0:
    print ("No entities found.")


# Why does our model now fail? Because we have trained a machine learning model, not an EntityRuler. It knows that Treblinka is a GPE, but it has only learned to identify it if it is spelled correctly. This is a bad model. Machine learing NER models improve with the more training data that we feed them. Most importantly, however, they improve with the greater amount of varied training data we feed them. A good rule of thumb is to start with 200 training samples and then make adjustments going forward. You may need to gather more varied training data or you may need to reconsider your labels. Another possibility is that you need to fine-tune your hyperperameters in the config.cfg file. We will be covering these problems and solutions throughout the remainder of this textbook. By now, though, you should have a good sense of how the training process works in spaCy 3. The material discussed in this notebook are by far the most challenging so far. Take your time here and get to know this process well before moving forward.

# ## Excerise

# For this notebook's exercise, try and generate a larger quantity of training data and feed it into a spaCy model and test that model on new, unseen texts. See how it performs.

# ## Video

# In this notebook, I rushed through this process with little exposition. The reason is because this material is easier to cover in video form. Please see the video below in which we perform similar tasks on a larger scale with the characters from the first book of Harry Potter.

# In[23]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/PJZzBp6em-Q" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>')

