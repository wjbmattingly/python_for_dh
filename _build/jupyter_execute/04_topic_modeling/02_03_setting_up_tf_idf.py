#!/usr/bin/env python
# coding: utf-8

# # <center>Setting up TF-IDF in Python and Scikit Learn</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>February 2021</center>

# ## Key Concepts in this Notebook

# 1) Importing the required libraries<br>
# 2) Preparing the data properly<br>
# 3) Setting up TF-IDF with Scikit Learn<br>

# ## Introduction

#  In the last notebook, we learned about Scikit-Learn. In this notebook, we are going to take that knowledge and implement the TF-IDF algorithm from Scikit-Learn, but before we do that, we have to consider one very important thing: the state of our data. Whenever you are using algorithms, it is always *essential* to think about what form does the algorithm expect. The first part of this notebook will, therefore, be dedicated to explaining the data and preparing it for the TF-IDF algorithm. It is important to note that this notebook will be code-centric.
#  
# Finally, because this notebook is designed to be from beginning to end of a TF-IDF implementation, from preparing the data to cleaning to TF-IDF to Clustering to data visualization, this notebook will be longer than the previous ones.

# ## The TRC Data

# In every real world scenario you will know the data that you are working with. In this section I think it's worthwhile to spend a little bit of time talking about the data that we are going to be working with throughout this notebook. The first bit of data that we're going to be working with is a collection of descriptions of violence from apartheid South Africa from the 20th century. They come out of the Truth and Reconciliation Commission in the early 2000s. The Truth and Reconciliation Commission or the TRC was a body put together at the end of the twentieth century to catalog the violence that befell victims during the apartheid period. The first dataset is what is known as Volume 7 of the TRC Final Report. It is organized as a collection of individuals and a brief description of the violence that befell them and the victim's age. Descriptions of violence are not structured in any way. Instead they have rich metadata within them. This metadata consists of things like dates, places, and other organizations during the 20th century.
# 
# The data that I have prepared for you is a JSON file of the TRC Volume 7 report. The JSON file is structured as a dictionary with two keys the first key is names and that corresponds to a list of the victim names. The second key is descriptions. This is the key piece of the data that we will be working with. These are the descriptions of violence and we are trying to identify topics within these descriptions.

# ## Preparing the Data

# In this section of the notebook we will begin importing and manipulating and working with our TRC dataset and in order to do that you need to be familiar with how to import JSON data in Python so in this first block of code we will be doing just that.  I always find that writing out a basic function for reading Json data is always useful because you can use the function throughout your script without having to write 3 lines of code and instead simply writing one. We are going to call this function load_data.

# In[2]:


import json


def load_data(file):
    with open (file, "r", encoding="utf-8") as f:
        data = json.load(f) 
    return (data)


# With this function now in place we can import our JSON data that contains our TRC data set which is under the data subfolder. In the next line, we call this function to achieve that task.

# In[4]:


trc_data = load_data("data/trc_dn.json")


# Now that we have loaded the data, let's create two separate objects, one for the anmes in the dataset and another for the descriptions. There are better ways to do this in Python with libraries like Pandas, but I do not want to introduce another library into the mix in this textbook.

# In[5]:


names = trc_data["names"]
descriptions = trc_data["descriptions"]


# Now that we have the objects created, it's probably a good idea to print of the first index of each to make sure that they are what we expect and to print off the length of each list to make sure that they are the same length.

# In[7]:


print (names[0])
print (descriptions[0])
print (len(names))
print (len(descriptions))


# This is precisely what we want to see. Both lists are the same length and index 0 for names aligns with the correct corresponding description. This is also a good chance to see what this data looks like. This description is a fair representation of the format and length of all other descriptions in this dataset.
# 
# Below, we will use the names to plot the data on a graph, but for now we will strictly be working with the descriptions list. The reason for this is because these are the texts that we want to cluster through TF-IDF and K-Means.

# ## Cleaning the Data

# Now that we have the data that we need for processing, it is time to start cleaning the data. When cleaning text for TF-IDF and topic modeling, it is often good practice to remove certain things from the text that may throw off the algorithms. The specific things you choose to remove from texts will vary depending on the texts you are working with, but there are generally certain words for each language that you will want to remove. These are called **stop words**.
# 
# In English, stop words will be articles, such as 'the', 'an', and 'a' or the verb "to be". These words are often removed from texts because they occur so frequently that they offer nothing unique about the texts at hand. In other words, they are so common that they do not aid in the clustering of texts. This is because clustering seeks to find particular features of texts and then identify the texts with common overlapping features. Stop words would make all texts overlap significantly. We remove these words to force clustering to focus on the more important words.
# 
# In addition to this, we also often need to develop our own stop words for these specific texts, or a general domain. In our case, these texts have a lot of dates and AC numbers that correspond to other records. While these are significant pieces of metadata, these both throw off the clustering. If we were interested in seeing how dates overlap, there are better ways of performing that task. For those interested, see my <a href="ner.pythonhumanities.com">Named Entity Recognition Textbook</a>.
# 
# The functions below will clean our text in the above mentioned manner. There are annotations to explain each section of the code. If more explanation is needed, please leave a comment on GitHub.

# In[9]:


import string
from nltk.corpus import stopwords
import re

def remove_stops(text, stops):
    #uses regex to remove all AC numbers
    text = re.sub(r"AC\/\d{1,4}\/\d{1,4}", "", text)
    
    #removes all stop words, including months
    words = text.split()
    final = []
    for word in words:
        if word not in stops:
            final.append(word)
            
    #reassembles the text without stop words
    final = " ".join(final)
    
    #removes all punctuation
    final = final.translate(str.maketrans("", "", string.punctuation))
    
    #removes all numbers
    final = "".join([i for i in final if not i.isdigit()])
    
    #eliminates double white spaces
    while "  " in final:
        final = final.replace("  ", " ")
    return (final)

def clean_docs(docs):
    #gets the NLTK's stopword list for English
    stops = stopwords.words("english")
    
    #Grabs all the months from data/months.json
    months = load_data("data/months.json")
    
    #combines the two to make a master stopword list
    stops = stops+months
    
    #empty new list to store the cleaned docs
    final = []
    
    #iterate over all docs and cleans them to be a
    #single sentence with no unwanted words
    for doc in docs:
        clean_doc = remove_stops(doc, stops)
        final.append(clean_doc)
    
    return (final)


# Now comes the time to clean all of our documents. We will use one line of code to pass all descriptions to clean_docs().

# In[10]:


cleaned_docs = clean_docs(descriptions)


# After cleaning my documents, I always find it is good to print off a sample of the before and after to see that my functions are working as intended. So, let's do that here.

# In[13]:


print ("Original Text:")
print (descriptions[0]+"\n")

print ("Cleaned Text:")
print (cleaned_docs[0])


# As we can see from these two outputs, the original text has been heavily altered and cleaned. Notice, for example, the removal of the date. Now that we have the data fully cleaned, it is time to begin setting up the TF-IDF algorithm with Scikit-Learn.

# ## Implementing TF-IDF in Python

# Implementing TF-IDF in Python requires us to import a few things from the Scikit Learn library. Remember, in Python Scikit Learn is "sklearn". So, let's import those things now.

# In[16]:


# A lot of this section comes from the Scikit Learn documentation and various blogs including the following:
#https://towardsdatascience.com/applying-machine-learning-to-classify-an-unsupervised-text-document-e7bb6265f52
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans


# First, we import the TfidfVectorizer. This is going to be what allows us to perform TF-IDF in just a few lines of code. Second, we import KMeans. This will be what allows us to cluster the TF-IDF of each key word in each text.
# 
# Now that we have the libraries imported, we can begin to work with them. First, let's make our vectorizer. This will be our TF-IDF algorithm. It will have several functions that we can call. For now, though, let's focus on the parameters.
# 
# 1) lowercase => allows us to lowercase our data.
# 2) max_features => this is how many words out of the entire corpus we want to take into account. Here, we will use 100. The higher the number, the more computational expensive the tasks are to run. I have chosen 100 for this demonstration somewhat at random, but it works fairly well for our purposes.
# 3) max_df => this is a float that tells the algorithm to ignore any word that occurs in 80% of the documents.
# 4) min_df => this is an integer that tells the algorithm to ignore words that do not occur more than 5 times in the entire corpus.
# 5) ngram_range => this is a tuple with index 0 being the smallest number of words to consider with the second index being the largest, i.e. 2 for bigram and 3 for trigrams. (1, 3) means the algorithm should consider anything from a unigram (one word) to trigram (three words) as a concept.
# 6) stop_words => this is the language you are working with and you are telling the algorithm to ignore the predefined set of stopwords. This is a bit excessive since we already did this with NLTK.

# In[17]:


vectorizer = TfidfVectorizer(
                                lowercase=True,
                                max_features=100,
                                max_df=0.8,
                                min_df=5,
                                ngram_range = (1,3),
                                stop_words = "english"

                            )


# Now that we have created the vectorizer, let's pass our documents to the algorithm with the method fit_transform(). This will pass all documents to the algorithm and vectorize them.

# In[18]:


vectors = vectorizer.fit_transform(cleaned_docs)


# Here, we can see the results of the vectors of the first document. This output is a tuple which indicates the keyword and the TF-IDF score. In this form, however, it is a bit hard to decipher. 

# In[72]:


print (vectors[0])


# In[23]:


feature_names = vectorizer.get_feature_names()


# By using the method get_feature_names(), we can get an easier to read text representation of our key words. Let's look at the most common first.

# In[24]:


print (feature_names[0])


# In[26]:


dense = vectors.todense()


# By using the method todense(), we can convert that vector into a larger representation and each word's TF-IDF score. Each number corresponds to a word. Those words that are keywords have a TF-IDF score, while those represented by 0 are words that did not make it into our max_features. In other words, they are irrelevant words.

# In[27]:


print (dense[0])


# To work with this data, let's reconvert it into a list with the command below.

# In[28]:


denselist = dense.tolist()


# This is what that same data looks like when printed off as a list. Again, this is our first document represented with its TF-IDF scores for each word.

# In[30]:


print (denselist[0])


# Now, let's convert every document from its TF-IDF scores to a list of key words. This will be essential for clustering below. In the code below, we run each description across the denselist and check if each word appears in the denselist. If it does (i.e. if it is one of the 100 important max feature words), then we keep it and append that list of words to all_keywords. This object will be all the documents in a list. Each index (document) will now be a list of words.

# In[31]:


all_keywords = []
for description in denselist:
    x=0
    keywords = []
    for word in description:
        if word > 0:
            keywords.append(feature_names[x])
        x=x+1
    all_keywords.append(keywords)


# Let's take a look at what we have been able to do to our document 0 by looking at its original state, cleaned state, and just the key words.

# In[73]:


print ("Original Text:")
print (descriptions[0]+"\n")

print ("Cleaned Text:")
print (cleaned_docs[0]+"\n")

print ("Only Keywords Text:")
print (all_keywords[0])


# ## K-Means Clustering

# Now that our data is nothing more than a list of lists of key words for each document, we can use these features to see where there is overlap. This is called clustering and one method of clustering is K-Means which seeks to place every document into a cluster to which it has the most similarity. In the below code, we define true_k as the number of clusters. In this example, I am telling it to find 5 clusters. In the video below, I used 20, but as we will see for plotting it is easier to have 5.

# In[34]:


true_k = 5

model = KMeans(n_clusters=true_k, init="k-means++", max_iter=100, n_init=1)


# Now that we have created the K-Means model, its time to cluster the data. We will do this by fitting the vectors to the model. In this scenario, we are using the TF-IDF scores from the descriptions to formulate the basis for our clusters.

# In[35]:


model.fit(vectors)

order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizer.get_feature_names()


# Now that we have done that, let's see what our 5 clusters look like as arrays. These arrays are a list of the keywords most associated with each cluster represented by their numerical value.

# In[45]:


print (order_centroids)


# Let's look at the first word from the first cluster, number 92. We can find that word by looking it up in our terms list.

# In[70]:


print (terms[92])


# Since we can do that with one word, we can automate the entire process of converting all numbers into a list of key words for each cluster with the below code. Here, I am limiting the list to just the first 10 words for each cluster.

# In[52]:


i = 0
for cluster in order_centroids:
    print (f"Cluster {i}")
    for keyword in cluster[0:10]:
        print (terms[keyword])
    print ("")
    i=i+1


# And Viola, just like that we have all 22,000 descriptions clusterd into 5 categories. I know what you may be thinking, though. How do we see where those documents are. The answer is addressed below when we plot the data. In order to walk through this portion of notebook, check out the video below.

# In[8]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/i74DVqMsRWY" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>')


# ## Plotting the Data

# This portion of the notebook is perhaps best illustrated with the video below. The code below has already been executed so that you can see the data plotted out on a graph. Each node on the graph represents a description. Each color represents a cluster.

# In[1]:


#A lot of this section was obtained from https://stackoverflow.com/questions/27494202/how-do-i-visualize-data-points-of-tf-idf-vectors-for-kmeans-clustering

import matplotlib.pyplot as plt
from sklearn.decomposition import PCA


# In[55]:


kmean_indices = model.fit_predict(vectors)

pca = PCA(n_components=2)
scatter_plot_points = pca.fit_transform(vectors.toarray())


# In[65]:


colors = ["r", "b", "m", "y", "c"]

x_axis = [o[0] for o in scatter_plot_points]
y_axis = [o[1] for o in scatter_plot_points]


# In[66]:


fig, ax = plt.subplots(figsize=(50, 50))
ax.scatter(x_axis, y_axis, c=[colors[d] for d in kmean_indices])


# In[67]:


fig, ax = plt.subplots(figsize=(50, 50))
ax.scatter(x_axis, y_axis, c=[colors[d] for d in kmean_indices])
for i, txt in enumerate(names):
    ax.annotate(txt[0:5], (x_axis[i], y_axis[i]))


# In[68]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/B0BkUNMqfSo" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>')

