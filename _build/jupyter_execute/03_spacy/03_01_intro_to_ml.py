#!/usr/bin/env python
# coding: utf-8

# # <center>Machine Learning NER with spaCy</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) Machine Learning<br>
# 2) Statistics<br>
# 3) Linear Algebra<br>
# 4) Matrix (pl. Matrices)<br>
# 5) Vectors<br>
# 6) Tensors<br>
# 7) Word Embeddings (Word Vectors)<br>
# 8) Machine Learning Training, Validation, and Testing<br>
# 8) spaCy models<br>

# ## What is Machine Learning?

# **Machine learning** is a branch of Artificial Intelligence. In order to understand artifical intelligence and how modern machine learning is different from its predecessor, I would recomend my video on the subject (a brief cinematic introduction to machine learning from my series on Machine Learning for DH.)

# In[2]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/G6cW5JybUPU" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# Machine Learning (and deep learning) is the process by which practitioners teach a computer system to perform a task, not with rules, but with statistics and linear algebra so that the system can learn from repeated (and randomized) experiences. If this does not make sense right now, it will by the end of this notebook. This notebook will necessary contain some math, but it will be kept to an absolute minimum. I will only present the math and mathematical concepts that are absolutely necessary.
# 
# Before moving forward, I also recommend this brief video on deep learning from my series on Neural Networks for DH.

# In[3]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/G0hvxnb7hHM" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# ## Types of Machine Learning

# There are several different types of machine learning: supervised learning, unsupervised learning, and semi-supervised learning. There are others (such as reinforcement learning), but these are the three essential forms.
# 
# **Supervised learning** is when we train a system with known data. In the case of NER, we train a system with a series of texts with the entities appropriately annotated with their corresponding labels. **Unsupervised learning** occurs when you don't know the categories of your data. You give the system a series of data and allow it to learn and identify patterns on its own. This is most popularly used for topic modeling and k-means (beyond the scope of this notebook). Finally, there is **semi-supervised learning** which falls between these two.
# 
# 
# Throughout this series, we will be using supervised learning and for that reason, I would like to explain this process from start to finish and then explain how it works.

# ## Supervised Learning in NER

# As noted above, supervised learning is the process by which a system learns from a set of inputs that have known labels. In order to train properly, the input data is divided into three categories: training data, validation data, and testing data. There is no set percentage to asign to each of these categories. A good rule of thumb, however, is save 20% of all annotated data for testing and then divide the remaining 80% 80/20 (testing/validation) ratio.
# 
# The first two, training data and validation data, are given to the system that is trying to learn. It uses the training data to hone a statistical model via predetermined algorithms. It does this by making guesses about what the proper labels are. It then checks its accuracy against the labels provided and makes adjustments accordingly.
# 
# Once it is finished viewing and guessing across all the training data, the first epoch, or iteration over the data, is finished. At this stage, the model then tests its accuracy against the validation data. These are left out of the training process and give the system a sense of its overall performance.
# 
# Because the validation data is left out of the training process, it able to be used for mid-training testing (or validation) of its accuracy. The training data is then randomized and given back to the system for x number of epochs. Again, there is no standard for the number of epochs, but a good rule of thumb is to start at 10 and study the results.
# 
# Once the model repeats this process for the set number of epochs, it is finished training. The model's accuracy can then be tested against the testing dataset to see how well it performs. The reason you want to keep the testing data separate from the validation data is because, despite being not include in the training, some of the validation data seeps into the training process. Because the testing data is well-annotated, the researcher can get an accurate sense of how well that model performs.
# 
# With that first model saved, it is common practice to adjust the parameters of the model multiple times to try to create a more accurate model. All models will be tested against the same testing data.
# 
# At this stage, depending on the results, more training data may need to be obtained, another test may be called for, or the researcher can begin deploying the model on unseen data and examine the results. Unseen data will be data that does not have annotations.
# 
# A good way to describe it is via the image below from https://bigdata-madesimple.com/. In the image, we see the input of raw data to an algorithm.

# <img src="https://bigdata-madesimple.com/wp-content/uploads/2018/02/Machine-Learning-Explained1.png">

# ## How does Supervised Learning Work? (MATH ALERT!)

# As the heading indicates, this section will venture into the realm of math, specifically statistics and linear algebra. Even if you are not a fan of math, please do read this section as it contains the foundational principals behind machine learning. I will keep the math to a minimum in order to simply explain *how* machine learning works and, even more importantly *why*. This will give you a better sense of not only when to use a machine learning approach to NER, but why you might not get the results you want to see and how to improve them.
# 
# The core concept behind supervised learning is the statistical model, a saved and usable system that can be given an input (a text) and output some sort of structured data (labels for entities). In order to understand what models are and how they work, I recommend watching the brief video below:

# In[4]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/I9Nl8QIIP54" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# Through spaCy, NLP practitioners do not have to engage in the tedious structure of neural networks. Instead, they can take advantage of the state-of-the-art neural network architectures developed by spaCy and easily train spaCy models with just a few lines of code. If you are curious about how training works, I recommend the video below:

# In[5]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/s8yQ4lRrEIY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')


# ## When to use Machine Learning NER

# In the last notebook, I explained when to use rules-based NER. Machine learning NER is useful when you cannot possible account for all variances of the entities in a corpus or creating such patterns would be so computationally expensive that its accuracy is not worth its use. A good example of this is every potential variation of a person's name. Consider the immense quantity of names that exist in the world and the combinations and various ways those names can be combined to create a unique entity. Even if we only have 10,000 first names and 10,000 last names, to account for all variations would be 100,000,000 million patterns to match. And there are far more than simple 10,000 of each in the world.
# 
# Another time to consider machine learning is when the data that will be fed to your system will not be entirely cleaned. Consider the example of names once again. Even if you had a system that could account for all 100,000,000 forms of those names, it will miss ones that have poor OCR or ones that have different text encoding because it was a text created prior to UTF-8.
# 
# In these instances machine learning is the right choice because machine learning NER models do not memorize entities. They learn entities. This means that if a model encounters an entity it has never seen before (even if poorly OCRed), it has the ability to **generalize** and identify that entity with the correct label.

# ## Using spaCy's Machine Learning Models

# Fortunately, as we will see in this series, spaCy makes not only using machine learning models easy, but drastically reduces the complexity of training custom machine learning NER models. 

# In[5]:


#We import the necessary library
import spacy

#load the machine learning model
nlp = spacy.load("en_core_web_sm")

#create a sample text
text = "Jon Stewart hosted The Daily Show that aired in New York City."

#create the spaCy doc
doc = nlp(text)

#extract all the entities from the doc with their labels
for ent in doc.ents:
    print (ent.text, ent.label_)


# In the example above, we seethe small English model Correctly identify John Stewart as a person. It identified The Daily Show as a WORK_OF_ART which is interesting and arguably true. Finally, it correctly identified New York City as a GPE (Geopolitical Entity). Now, let's introduce some textual problems to see how the model performs.

# In[10]:


#We import the necessary library
import spacy

#load the machine learning model
nlp = spacy.load("en_core_web_sm")

#create a sample text
text = "Jon Stewwasrt hosted The Daily Show that aired in New Yasdfasasdfrk City."

#create the spaCy doc
doc = nlp(text)

#extract all the entities from the doc with their labels
for ent in doc.ents:
    print (ent.text, ent.label_)


# Notice that despite introducing textual corruption, the model performs precisely the same way. The reason? Because it has learned from context. It has likely seen the word "hosted" before and knows that people typically host. It has seen the word City capitalized often used to describe a GPE. This is why machine learning offers the solution for inconsistent entities or entities that are so vast that incorperating them all into an EntityRuler would be impossible.

# ## Exercise

# In the code space provided below try to push the small English model. Make some guesses based on what you've learned why the model either succeeds or fails to identify entities despite the textual corruptions you introduce. As you do this, keep in mind that this is the *small* model. The larger models perform better for reasons that we will explore later in this series.

# In[ ]:





# ## Video for Machine Learning NER

# In[1]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/2Ny0yATnuxY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')

