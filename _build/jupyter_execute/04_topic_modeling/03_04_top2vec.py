#!/usr/bin/env python
# coding: utf-8

# # <center>Top2Vec in Python</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>February 2021</center>

# ## Importing the Required Libraries

# In[17]:


import pandas as pd


# In[18]:


df = pd.read_json("data/vol7.json")
df


# In[19]:


docs = df.descriptions.tolist()
docs[0]


# In[20]:


from top2vec import Top2Vec


# In[21]:


model = Top2Vec(docs)


# In[22]:


topic_sizes, topic_nums = model.get_topic_sizes()
print (topic_sizes)


# In[23]:


print (topic_nums)


# In[28]:


topic_words, word_scores, topic_nums = model.get_topics(1)


# In[29]:


for words, scores, num in zip(topic_words, word_scores, topic_nums):
    print (num)
    print (f"Words: {words}")


# In[30]:


documents, document_scores, document_ids = model.search_documents_by_topic(topic_num=0, num_docs=10)
for doc, score, doc_id in zip(documents, document_scores, document_ids):
    print(f"Document: {doc_id}, Score: {score}")
    print("-----------")
    print(doc)
    print("-----------")
    print()


# In[ ]:




