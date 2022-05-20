#!/usr/bin/env python
# coding: utf-8

# # <center>Generating Custom Word Vectors with Gensim</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) Gensim library<br>
# 2) How to create word vectors in Gensim<br>
# 3) Topic modeling<br>
# 

# ## Introduction to Gensim

# Gensim is a powerful Python library that was originally designed to produce good topic models. **Topic models** are machine learning models that read over an entire corpus and cluster individual documents into clusters of similarity. In order to produce good results, Gensim (and other topic modeling methods) are reliant upon numerical represntations of words. In other words, these methods depend on word vectors. To have accurate results, therefore, Gensim is capable of generating word vectors with relatively minimal code. SpaCy, on the other hand, is an NLP library not capable of generating custom word vectors. While users can inject to words into models, spaCy is not designed to generate word vectors on its own. For this reason, even spaCy's documentation recomends using other libraries, such as Gensim to generate word vectors.
# 
# In this notebook, we will be going through the process of generating our own word vectors. In order to reduce the time to perform the task at hand, we will use a toy corpus. This process, however, can easily be scaled for a corpus of millions of documents.

# ## Preparing the Corpus

# In order to generate word vectors, we need one thing: a corpus/ Let's create one right now.

# In[2]:


corpus = "Tom is cat, while Jerry is a mouse. Tom and Jerry are characters in a cartoon series. Some of the cartoons contain words, but most are silent. Silent cartoons still have music and sound effects."


# Before we can give this corpus to Gensim, however, we need to do a few preprocessing techniques to it.
# 
# 1) First, we need to remove the stopwords from the corpus. Stopwords are words that occur frequently in a corpus, so frequently that they do not necessarily offer much meaning for distant reading and, as a result, throw off machine learning models. Other stopwords are words that occur with high frequency in a langauge as a whole. For our purposes, we will use the following stopwords available from the NLTK (natural language toolkit)

# In[3]:


stopwords = ["i","me","my","myself","we","our","ours","ourselves","you","your","yours","yourself","yourselves",
             "he","him","his","himself","she","her","hers","herself","it","its","itself","they","them","their",
             "theirs","themselves","what","which","who","whom","this","that","these","those","am","is","are","was",
             "were","be","been","being","have","has","had","having","do","does","did","doing","a","an","the","and",
             "but","if","or","because","as","until","while","of","at","by","for","with","about","against","between",
             "into","through","during","before","after","above","below","to","from","up","down","in","out","on","off",
             "over","under","again","further","then","once","here","there","when","where","why","how","all","any","both",
             "each","few","more","most","other","some","such","no","nor","not","only","own","same","so","than","too","very",
             "s","t","can","will","just","don","should","now"
            ]
corpus = corpus.lower()
words = corpus.split()

new_corpus = []
for word in words:
    if word not in stopwords:
        new_corpus.append(word)

corpus = " ".join(new_corpus)
print (corpus)


# 2) Second, this corpus should be divided into sentences. In order to do that, I recommend using spaCy's sentence tokenizer.
# 3) While we do this, we should also eliminate the punctuation from the sentences. We can do this with the standard string library from Python.
# 4) Also at this stage, we should lowercase our words (OPTIONAL)
# 5) If we wish to produce a smaller amount of word vectors, we could also consider lemmatizing our words as well (OPTIONAL)
# 6) We need to split the sentence into words and append that list of words to a new object

# In[4]:


import spacy
import string

nlp = spacy.load("en_core_web_sm")
doc = nlp(corpus)

sentences = []
for sent in doc.sents:
    sentence = sent.text.translate(str.maketrans('', '', string.punctuation))
    words = sentence.split()
    sentences.append(words)
print (sentences)


# ## Creating Word Vectors

# At this stage, we can start preparing our word vectors. To do this, we will use the function below. 

# In[5]:


def create_wordvecs(corpus, model_name):
    from gensim.models.word2vec import Word2Vec
    from gensim.models.phrases import Phrases, Phraser
    from collections import defaultdict
    
    print (len(corpus))
    

    phrases = Phrases(corpus, min_count=30, progress_per=10000)
    print ("Made Phrases")
    
    bigram = Phraser(phrases)
    print ("Made Bigrams")
    
    sentences = phrases[corpus]
    print ("Found sentences")
    word_freq = defaultdict(int)

    for sent in sentences:
        for i in sent:
            word_freq[i]+=1

    print (len(word_freq))
    
    print ("Training model now...")
    w2v_model = Word2Vec(min_count=1,
                        window=2,
                        size=10,
                        sample=6e-5,
                        alpha=0.03,
                        min_alpha=0.0007,
                        negative=20)
    w2v_model.build_vocab(sentences, progress_per=10000)
    w2v_model.train(sentences, total_examples=w2v_model.corpus_count, epochs=30, report_delay=1)
    w2v_model.wv.save_word2vec_format(f"data/{model_name}.txt")
create_wordvecs(sentences, "word_vecs")


# ## Examining Word Vectors

# Now, we can open up our word vectors and examine them. The first line in this text file will be the shape of the word vectors. This should be two integers. The first number (17) is the number of unique words in the vocabulary. The second number (10) are the number of dimensions of each word.

# In[6]:


with open ("data/word_vecs.txt", "r") as f:
    data = f.readlines()
    print (data[0])


# Let's look at the first word in our word vectors, "Tom":

# In[7]:


print (data[1])


# Here, we see two pieces of information. The first is a string and it is the word itself. In this case, "Tom". The second bit of data is a series of 10 floats. These are our dimensions for the word. This is the numerical way in which "Tom" is understood by the Gensim model. This is precisely the data that spaCy expects to recieve in order to load these vectors into a model. In the next notebook, we will do just that.

# ## Exercise

# Try to use the above code to create your own custom word vectors for your own corpus.

# ## Video

# In[52]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/eZJm7PisZvk" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')

