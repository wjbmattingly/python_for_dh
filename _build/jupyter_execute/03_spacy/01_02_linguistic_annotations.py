#!/usr/bin/env python
# coding: utf-8

# # <center>Getting Started with spaCy and its Linguistic Annotations</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>August 2021</center>

# In this chapter, we will start working with spaCy directly. The goals of this chapter are twofold. First, it is my hope that you understand the basic spaCy syntax for creating a Doc container and how to call specific attributes of that container. Second, it is my hope that you leave this chapter with a basic understanding of the vast linguistic annotations available in spaCy. While we will not explore all attributes, we will deal with many of the most important ones, such as lemmas, parts-of-speech, and named entities. By the time you are finished with this chapter, you should have enough of a basic understanding of spaCy to begin applying it to your own texts.

# ## Importing spaCy and Loading Data

# As with all Python libraries, the first thing we need to do is import spaCy. In the last notebook, I walked you through how to install it and download the small English model. If you have followed those steps, you should be able to import it like so:

# In[1]:


import spacy


# With spaCy imported, we can now create our nlp object. This is the standard Pythonic way to create your model in a Python script. Unless you are working with multiple models in a script, try to always name your model, nlp. It will make your script much easier to read. To do this, we will use spacy.load(). This command tells spaCy to load up a model. In order to know which model to load, it needs a string argument that corresponds to the model name. Since we will be working with the small English model, we will use "en_core_web_sm". This function can take keyword arguments to identify which parts of the model you want to load, but we will get to that later. For now, we want to import the whole thing.

# In[2]:


nlp = spacy.load("en_core_web_sm")


# Great! With the model loaded, let's go ahead and import our text. For this chapter, we will be working with the opening description from the Wikipedia article on the United States. In this repo, it is found in the subfolder data and is entitled wiki_us.txt.

# In[3]:


with open ("data/wiki_us.txt", "r") as f:
    text = f.read()


# Now, let's see what this text looks like. It can be a bit difficult to read in a JupyterBook, but notice the horizontal slider below. You don't neeed to read this in its entirety.

# In[4]:


print (text)


# ## Creating a Doc Container

# With the data loaded in, it's time to make our first Doc container. Unless you are working with multiple Doc containers, it is best practice to always call this object "doc", all lowercase. To create a doc container, we will usually just call our nlp object and pass our text to it as a single argument.

# In[5]:


doc = nlp(text)


# Great! Let's see what this looks like.

# In[6]:


print (doc)


# If you are trying to spot the difference between this and the text above, good luck. You will not see a difference when printing off the doc container. But I promise you, it is quite different behind the scenes. The Doc container, unlike the text object, contains a lot of valuable metadata, or attributes, hidden behind it. To prove this, let's examine the length of the doc object and the text object.

# In[7]:


print (len(doc))
print (len(text))


# Hmm... What's going on here? Same text, but different length. Why does this occur? To answer that, let's explore it more deeply and try and print off each item in each object.

# In[8]:


for token in text[:10]:
    print (token)


# As we would expect. We have printed off each character, including white spaces. Let's try and do the same with the Doc container.

# In[9]:


for token in doc[:10]:
    print (token)


# And now we see the magical difference. While on the surface it may seem that the Doc container's length is dependent on the quantity of words, look more closely. You should notice that the open and close parentheses are also considered an item in the container. These are all known as tokens. **Tokens** are a fundamental building block of spaCy or any NLP framework. They can be words or punctuation marks. Tokens are something that has syntactic purpose in a sentence and is self-contained. A good example of this is the contraction "don't" in English. When tokenized, or the process of converting the text into tokens, we will have two tokens. "do" and "n't" because the contraction represents two words, "do" and "not".
# 
# On the surface, this may not seem exceptional. But it is. You may be thinking to yourself that you could easily use the split method in Python to split by whitespace and have the same result. But you'd be wrong. Let's see why.

# In[10]:


for token in text.split()[:10]:
    print (token)


# Notice that the parentheses are not removed or handled individually. To see this more clearly, let's print off all tokens from index 5 to 8 in both the text and doc objects.

# In[11]:


words = text.split()[:10]


# In[12]:


i=5
for token in doc[i:8]:
    print (f"SpaCy Token {i}:\n{token}\nWord Split {i}:\n{words[i]}\n\n")
    i=i+1


# We can see clearly now how the spaCy Doc container does much more with its tokenization than a simple split method. We could, surely, write complex rules for a language to achieve the same results, but why bother? SpaCy does it exceptionally well for all languages. In my entire time using spaCy, I have never seen the tokenizer make a mistake. I am sure that mistakes may occur, but these are probably rare exceptions.
# 
# Let's see what else this Doc Container holds.

# ## Sentence Boundary Detection (SBD)

# In NLP, sentence boundary detection, or SBD, is the identification of sentences in a text. Again, this may seem fairly easy to do with rules. One could use split("."), but in English we use the period to also denote abbreviation. You could, again, write rules to look for periods not proceeded by a lowercase word, but again, I ask the question, "why bother?". We can use spaCy and in seconds have all sentences fully separated through SBD.
# 
# To access the sentences in the Doc container, we can use the attribute sents, like so:

# In[13]:


for sent in doc.sents:
    print (sent)


# Let's move forward with just one of these sentences. Let's try and grab index 0 in this attribute.

# In[14]:


sentence1 = doc.sents[0]
print (sentence1)


# Uh oh! We got an error. That is because the sents attribute is a generator. In python, we can usually iterate over generators by converting them into a list. So, let's do that.

# In[15]:


sentence1 = list(doc.sents)[0]
print (sentence1)


# Now we have the first sentence. Now that we have a smaller text, let's explore spaCy's other building block, the token.

# ## Token Attributes

# The token object contains a lot of different attributes that are VITAL do performing NLP in spaCy. We will be working with a few of them, such as:
# 
# * .text
# * .head
# * .left_edge
# * .right_edge
# * .ent_type_
# * .iob_
# * .lemma_
# * .morph
# * .pos_
# * .dep_
# * .lang_
# 
# I will briefly describe these here and show you how to grab each one and what they look like. We will be exploring each of these attributes more deeply in this chapter and future chapters. To demonstrate each of these attributes, we will use one token, "States" which is part of a sequence of tokens that make up "The United States of America"

# In[16]:


token2 = sentence1[2]
print (token2)


# ### Text

# ```Verbatim text content.``` -spaCy docs

# In[17]:


token2.text


# ### Head

# ```The syntactic parent, or “governor”, of this token.``` -spaCy docs

# In[18]:


token2.head


# This tells to which word it is governed by, in this case, the primary verb, "is", as it is part of the noun subject.

# ### Left Edge

# ``` The leftmost token of this token’s syntactic descendants.``` -spaCy docs

# In[19]:


token2.left_edge


# If part of a sequence of tokens that are collectively meaningful, known as **multi-word tokens**, this will tell us where the multi-word token begins.

# ### Right Edge

# ``` The rightmost token of this token’s syntactic descendants.``` -spaCy docs

# In[20]:


token2.right_edge


# This will tell us where the multi-word token ends.

# ### Entity Type

# ``` Named entity type.``` -spaCy docs

# In[21]:


token2.ent_type


# Note the absence of the _ at the end of the attribute. This will return an integer that corresponds to an entity type, where as _ will give you the string equivalent., as in below.

# In[22]:


token2.ent_type_


# We will learn all about types of entities in our chapter on named entity recognition, or NER. For now, simply understand that GPE is geopolitical entity and is correct.

# ### Ent IOB

# ```IOB code of named entity tag. “B” means the token begins an entity, “I” means it is inside an entity, “O” means it is outside an entity, and "" means no entity tag is set.```

# In[23]:


token2.ent_iob_


# IOB is a method of annotating a text. In this case, we see "I" because states is inside an entity, that is to say that it is part of the United States of America.

# ### Lemma

# ```Base form of the token, with no inflectional suffixes.``` -spaCy docs

# In[24]:


token2.lemma_


# In[25]:


sentence1[12].lemma_


# ### Morph

# ```Morphological analysis``` -spaCy docs

# In[26]:


sentence1[12].morph


# ### Part of Speech

# ```Coarse-grained part-of-speech from the Universal POS tag set.``` -spaCy docs

# In[27]:


token2.pos_


# ### Syntactic Dependency

# ```Syntactic dependency relation.``` -spaCy docs

# In[28]:


token2.dep_


# ### Language

# ```Language of the parent document’s vocabulary.``` -spaCy docs

# In[29]:


token2.lang_


# ## Part of Speech Tagging (POS)

# In the field of computational linguistics, understanding parts-of-speech is essential. SpaCy offers an easy way to parse a text and identify its parts of speech. Below, we will iterate across each token (word or punctuation) in the text and identify its part of speech.

# In[30]:


for token in sentence1:
    print (token.text, token.pos_, token.dep_)


# Here, we can see two vital pieces of information: the string and the corresponding part-of-speech (pos). For a complete list of the pos labels, see the spaCy documentation (https://spacy.io/api/annotation#pos-tagging). Most of these, however, should be apparent, i.e. PROPN is proper noun, AUX is an auxiliary verb, ADJ, is adjective, etc. We can visualize this sentence with a diagram through spaCy's displaCy Notebook feature.

# In[31]:


from spacy import displacy
displacy.render(sentence1, style="dep")


# ## Named Entity Recognition

# Another essential task of NLP, is named entity recognition, or NER. I spoke about NER in the last notebook. Here, I’d like to demonstrate how to perform basic NER via spaCy. Again, we will iterate over the doc object as we did above, but instead of iterating over doc.sents, we will iterate over doc.ents. For our purposes right now, I simply want to print off each entity’s text (the string itself) and its corresponding label (note the _ after label). I will be explaining this process in much greater detail in the next two notebooks.

# In[32]:


for ent in doc.ents:
    print (ent.text, ent.label_)


# Sometimes it can be difficult to read this output as raw data. In this case, we can again leverage spaCy's displaCy feature. Notice that this time we are altering the keyword argument, style, with the string "ent". This tells displaCy to display the text as NER annotations

# In[33]:


displacy.render(doc, style="ent")


# ## Conclusion

# I recommend spending a little bit of time going through this notebook a few times. The information covered throughout this notebook will be reinforced as we explore each of these areas in more depth with real-world examples of how to implement them to tackle different problems.

# In[ ]:




