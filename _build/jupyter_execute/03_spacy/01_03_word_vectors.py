#!/usr/bin/env python
# coding: utf-8

# # <center>Word Vectors and spaCy</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# In this notebook is word vectors, or word embeddings. Because the English small model does not have these saved, we will be working with the next largest model, the English medium model, en_core_web_md. Let's import spaCy and download the medium model.

# In[3]:


import spacy
get_ipython().system('python -m spacy download en_core_web_md')


# In[30]:


nlp = spacy.load("en_core_web_md")
with open ("data/wiki_us.txt", "r") as f:
    text = f.read()
doc = nlp(text)
sentence1 = list(doc.sents)[0]


# ## Word Vectors

# Word vectors, or word embeddings, are numerical representations of words in multidimensional space through matrices. The purpose of the word vector is to get a computer system to understand a word. Computers cannot understand text efficiently. They can, however, process numbers quickly and well. For this reason, it is important to convert a word into a number.
# 
# Initial methods for creating word vectors in a pipeline take all words in a corpus and convert them into a single, unique number. These words are then stored in a dictionary that would look like this: {“the”: 1, “a”, 2} etc. This is known as a bag of words. This approach to representing words numerically, however, only allow a computer to understand words numerically to identify unique words. It does not, however, allow a computer to understand meaning.
# 
# Imagine this scenario:
# 
# Tom loves to eat chocolate.
# 
# Tom likes to eat chocolate.
# 
# These sentences represented as a numerical array (list) would look like this:
# 
# 1, 2, 3, 4, 5
# 
# 1, 6, 3, 4, 5
# 
# As we can see, as humans both sentences are nearly identical. The only difference is the degree to which Tom appreciates eating chocolate. If we examine the numbers, however, these two sentences seem quite close, but their semantical meaning is impossible to know for certain. How similar is 2 to 6? The number 6 could represent “hates” as much as it could represent “likes”. This is where word vectors come in.
# 
# Word vectors take these one dimensional bag of words and gives them multidimensional meaning by representing them in higher dimensional space, noted above. This is achieved through machine learning and can be easily achieved via Python libraries, such as Gensim, which we will explore more closely in the next notebook.

# ### Why use Word Vectors?

# The goal of word vectors is to achieve numerical understanding of language so that a computer can perform more complex tasks on that corpus. Let’s consider the example above. How do we get a computer to understand 2 and 6 are synonyms or mean something similar? One option you might be thinking is to simply give the computer a synonym dictionary. It can look up synonyms and then know what words mean. This approach, on the surface, makes perfect sense, but let’s explore that option and see why it cannot possibly work.
# 
# For the example below, we will be using the Python library PyDictionary which allows us to look up definitions and synonyms of words.

# In[17]:


from PyDictionary import PyDictionary

dictionary=PyDictionary()
text = "Tom loves to eat chocolate"

words = text.split()
for word in words:
    syns = dictionary.synonym(word)
    print (f"{word}: {syns[0:5]}\n")


# Even with the simple sentence, the results are comically bad. Why? The reason is because synonym substitution, a common method of data augmentation, does not take into account syntactical differences of synonyms. I do not believe anyone would think “Felis domesticus”, the Latin name of the common house cat, would be an adequite substitution for the name Tom. Nor is “garbage down” a really proper synonym for eat.
# 
# Perhaps, then we could use synonyms to find words that have cross-terms, or terms that appear in both synonym sets.

# In[18]:


from PyDictionary import PyDictionary

dictionary=PyDictionary()

words  = ["like", "love"]
for word in words:
    syns = dictionary.synonym(word)
    print (f"{word}: {syns[0:5]}\n")


# This, as we can see, has some potential to work, but again it is not entirely reliable and to work with such a list would be computationally expensive. For both of these reasons, word vectors are prefered. The reason? Because they are formed by the computer on corpora for a specific task. Further, they are numerical in nature (not a dictionary of words), meaning the computer can process them more quickly.

# ###  What do Word Vectors Look Like?

# Word vectors have a preset number of dimensions. These dimensions are honed via machine learned. Models take into account word frequency alongside words across a corpus and the appearance of other words in similar contexts. This allows for the the computer to determine the syntactical similarity of words numerically. It then needs to represent these relationships numerically. It does this through the vector, or a matrix of matrices. To represent these more concisely, models flatten a matrix to a float (decimal number). The number of dimensions represent the number of floats in the matrix.
# 
# Let's take a look at the first word in our sentence. Specifically, let's look at its vector.

# In[19]:


sentence1[0].vector


# ### Why use Word Vectors?

# Once a word vector model is trained, we can do similarity matches very quickly and very reliably. Let's explore some vectors from our medium sized model. Let's specifically try and find the words most closely related to the word dog.

# In[33]:


#https://stackoverflow.com/questions/54717449/mapping-word-vector-to-the-most-similar-closest-word-using-spacy
your_word = "dog"

ms = nlp.vocab.vectors.most_similar(
    np.asarray([nlp.vocab.vectors[nlp.vocab.strings[your_word]]]), n=10)
words = [nlp.vocab.strings[w] for w in ms[0][0]]
distances = ms[2]
print(words)


# ## Doc Similarity

# In spaCy we can do this same thing at the document level. Through word vectors we can calculate the similarity between two documents. Let's look at the example from spaCy's documentation.

# In[8]:


nlp = spacy.load("en_core_web_md")  # make sure to use larger package!
doc1 = nlp("I like salty fries and hamburgers.")
doc2 = nlp("Fast food tastes very good.")

# Similarity of two documents
print(doc1, "<->", doc2, doc1.similarity(doc2))


# ## Word Similarity

# We can also calculate the similarity between two given words.

# In[9]:


# Similarity of tokens and spans
french_fries = doc1[2:4]
burgers = doc1[5]
print(french_fries, "<->", burgers, french_fries.similarity(burgers))


# ## Conclusion

# As we have seen in this notebook, spaCy is made up of a series of complex P
