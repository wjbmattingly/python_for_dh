#!/usr/bin/env python
# coding: utf-8

# # <center>Cultivating Good Datasets for Entities</center>

# <center>Dr. W.J.B. Mattingly</center>
# 
# <center>Smithsonian Data Science Lab and United States Holocaust Memorial Museum</center>
# 
# <center>January 2021</center>

# ## Key Concepts in this Notebook

# 1) Where to find good datasets<br>
# 2) How to clean datasets<br>

# ## Introduction to Datasets

# The previous notebooks have covered the basics of named entity recognition and provided lessons on how to work with spaCy. With all of this in place, it is time to shift this series towards gathering and cleaning the data. This notebook, 09.01, will be on acquiring the requisite data for named entities relevant to the Holocaust. In Notebook 09.02 will be dedicated to cultivating a corpus to automate an the creation of a training set via the spaCy EntityRuler.
# 
# In this notebook we will cover where to find data for good datasets. How to clean that data. And how to run some preliminary tests to make sure you have optimized the data for the purpose of creating a rules-based NER via spaCy's EntityRuler. This will allow you to have a good rules-based NER that can either be used on its own or leveraged to cultivate a good training set for a machine learning model.

# ## Acquiring the Data

# One of the first questions you will ask yourself in this pursuit, is "where can I acquire lists?" The answer is, unfortunately, "it depends." Sometimes good datasets exist. There are a few good places to look, such as GitHub, Wikipedia, and academic digital projects. For each project, you must don your detective goggles and explore the web to find these datasets. Most times, it will take a bit of work (and some Python code) to get the data into a structured form. In this notebook, we will try to cultivate a good dataset for concentration camps.
# 
# If we are looking to generate entities for concentration camps, we have a wealth of data, but this data is not necessary cleaned or structured. Let's examine three different locations where we can collate a list of concentration camps from the web and the strengths and weaknesses of those sources.

# ## Wikipedia

# Chances are, you will often begin your search by simply typing into Google, "List of [X]". If you do this with concentration camp, then you will likely first encounter Wikipedia (https://en.wikipedia.org/wiki/List_of_Nazi_concentration_camps).
# 
# This page is particularly useful for a few reasons. First, you have a list of the major camps, such as Auschwitz and Dachau. More importantly, however, you also have access to linked pages of subcamps, i.e. for Auchwitz, one can acess this page: https://en.wikipedia.org/wiki/List_of_subcamps_of_Auschwitz. With a little bit of Python, requests, and BeautifulSoup, we can easily compile a quick list.

# In[43]:


#Code for gathering subcamps

#import web scraping libraries
import requests
from bs4 import BeautifulSoup

def grab_subcamps(url, start_row, cell, t_class=False):
    '''
    This function will grab table data from Wikipedia.
    It allows you to grab specific rows and specific cells of data to cultivate lists of entities
    
    url       >> the Wikipedia url for grabbing data
    start_row >> Where the data starts in the table
    cell      >> The cell that you desire to grab from the table
    t_class   >> Some Wikipedia tables have a specific class of table that you need to grab, i.e. "wikipedia sortable".
    '''
    #url of the page
    
    #create the html object
    s = requests.get(url).content

    #set up the soup so that the html object can be parsed
    soup = BeautifulSoup(s)

    #grab the first table
    if t_class == True:
        table = soup.find("table", {"class": "wikitable sortable"})
    else:
         table = soup.find("table")

    #create a blank list to append to for gathering camps
    camps = []

    #iterate over rows in table, beginning with row 3
    for row in table.find_all("tr")[start_row:]:
        #one of the rows has only one cell, so we set up an index exception
        try:
            #grabs the 2nd cell in each row and cleans the data, splits off the cases of parentheses
            #and grabs the first index from that split list
            camp = row.find_all("td")[cell].text.strip().split("(")[0].split("/")[0].strip()
            camps.append(camp)
        except:
            IndexError
    return (camps)
        
#print off the subcamps of Auschwitz
ausch_subcamps = grab_subcamps("https://en.wikipedia.org/wiki/List_of_subcamps_of_Auschwitz", 2, 1)
buch_subcamps = grab_subcamps("https://en.wikipedia.org/wiki/List_of_subcamps_of_Buchenwald", 1, 1, t_class=True)

print (ausch_subcamps)
print ("")
print (buch_subcamps)


# The above list is a cleaned list of the subcamps of Auschwitz and Buchenwald. We gathered it and cleaned it with minimal code from our first Google search. The benefits of acquring the data in this manner is that we have some sense of structure as well. We know that these are the subcamps of Auschwitz, meaning we can link them in our data structure to their corresponding main camp.
# 
# This data does, however, come at a cost. It is data gathered from Wikipedia. In order to ensure that this data is proper, a content expert should be consulted. If a content expert is not a hand, I would recommend acquiring data from more reputable sites, such as nationally-funded museums or academic institutions.

# ## United States Holocaust Memorial Museum

# One such institution is the United States Holocaust Memorial Museum (USHMM), located in Washington, D.C. in the United States. When searching the USHMM collections, one way to limit your search is by Key Camps (https://www.ushmm.org/)
# 
# Which looks like this:

# In[49]:


ushmm_camps = ['Alderney', 'Amersfoort', 'Auschwitz', 'Banjica', 'Bełżec', 'Bergen-Belsen,', 'Bernburg', 'Bogdanovka', 'Bolzano', 'Bor', 'Breendonk',
         'Breitenau', 'Buchenwald,', 'Chełmno', 'Dachau', 'Drancy', 'Falstad', 'Flossenbürg', 'Fort VII', 'Fossoli', 'Grini', 'Gross-Rosen',
         'Herzogenbusch', 'Hinzert', 'Janowska', 'Jasenovac', 'Kaiserwald', 'Kaunas', 'Kemna', 'Klooga', 'Le Vernet', 'Majdanek', 'Malchow',
         'Maly Trostenets', 'Mechelen', 'Mittelbau-Dora', 'Natzweiler-Struthof', 'Neuengamme', 'Niederhagen', 'Oberer Kuhberg', 'Oranienburg',
         'Osthofen', 'Płaszów', 'Ravensbruck', 'Risiera di San Sabba', 'Sachsenhausen', 'Sajmište', 'Salaspils', 'Sobibór', 'Soldau', 'Stutthof',
         'Theresienstadt,', 'Trawniki', 'Treblinka', 'Vaivara']
print (ushmm_camps)


# While this dataset is cleaned and good, it has certain limitations. First, it is not complete. This is a list of *key* camps, not all camps. Note that subcamps are left off the list. The second problem we have is that these camps of certain characters in their names that reflect the accent marks or letters that are not in the English alphabet. Some Holocaust texts, however, use only English letters and characters. Therefore, searches for certain words, such as Płaszów will not return a hit in a search for Plaszow. It is important, therefore, to make sure both forms of the word are represented in a rules-based search.
# 
# With the function below, we can produce copies of each word with and without these characters.

# In[52]:


def remove_accents(text):
    
    #Polish letters
    letters= {
    'ł':'l', 'ą':'a', 'ń':'n', 'ć':'c', 'ó':'o', 'ę':'e', 'ś':'s', 'ź':'z', 'ż':'z',
    'Ł':'L', 'Ą':'A', 'Ń':'N', 'Ć':'C', 'Ó':'O', 'Ę':'E', 'Ś':'S', 'Ź':'Z', 'Ż':'Z',

    #Accent Vowels
    "à":"a", "á":"a", "â":"a", "ã":"a", "ä":"a", "å":"a", "æ": "ae",
    "À":"A", "Á":"A", "Â":"A", "Ã":"A", "Ä":"A", "Å":"A", "Æ": "ae",

    "è":"e", "é":"e", "ê":"e", "ë":"e",
    "È":"E", "É":"E", "Ê":"E", "Ë":"E",

    "ì":"i", "í":"i", "î":"i", "ï":"i",
    "Ì":"I", "Í":"I", "Î":"I", "Ï":"I",

    "ò": "o", "ó": "o", "ô": "o",  "õ": "o",  "ö": "o", "ø": "o",
    "Ò": "O", "Ó": "O", "Ô": "O",  "Õ": "O",  "Ö": "O", "Ø": "O",

    "ù": "u", "ú": "u",  "û": "u",  "ü": "u",
    "Ù": "U", "Ú": "U",  "Û": "U",  "Ü": "U",

    "ý": "y", "ÿ": "y",
    "Ý": "Y", "Ÿ": "Y",

    #Accent Cononants
    "ç": "c", "Ç": "C",
    "ß": "ss"
    }
    
    trans=str.maketrans(letters)
    result=text.translate(trans)
    return (result)

final = []
for camp in ushmm_camps:
    final.append(camp)
    final.append(remove_accents(camp))

#Delete all duplicates
ushmm_camps = list(set(final))
ushmm_camps.sort()
print (ushmm_camps)


# Note the standardization of 'Płaszów' as 'Plaszow' in the list. Both forms are now represented in our dataset, meaning we can develop a rules-based EntityRuler that can find both forms of these words in texts. While we were able to solve the first problem, that of standardized data, we cannot solve the first, however. Should we wish, though, we could add this dataset to our Wikipedia datasets, but as we will see below, a larger dataset presents new challenges.

# ## EHRI and Toponyms in the Datasets

# Another excellent resource for datasets pertaining to the Holocaust is EHRI Project (https://portal.ehri-project.eu/). Under their authority sets and vocabularies, users have access to well-cultivated datasets, including "EHRI Camps" (https://portal.ehri-project.eu/vocabularies). This list contains 1,975 different camps. As we did with the Wikipedia data above, we can easily webscrape this data. It is here, however, that I want to raise a word of caution.
# 
# Both the EHRI dataset and the Wikipedia larger dataset (both of which include subcamps) contain toponyms, or words that have identical spelling but have different meaning in different contexts. A good example of this is "Cologne" which is in our Buchenwald subcamp dataset. Cologne, however, is not strictly a "camp", rather it can also be a GPE or LOCATION. In other words, it can also function as Cologne the city in a text. How then do we account for this when trying to prepare a rules-based NER or automate the cultivation of a good training set for an ML model?
# 
# To generate a rules-based method, we could eliminate all instances of these toponyms being used without the word "camp" nearby. We could also train a toponym model that parses all identified camps and then eliminates the ones that don't fit the typical pattern, or any number of other things. There are options. I am less interested in developing a rules-based NER approach for the purpose of deployment, however. I am interested in using a rules-based NER approach to cultivate a training set for a machine learning NER model. Because this is my objective, I would drop all instances of toponyms from my dataset, such as Cologne. The best way to do this is with a content expert and manually eliminate all toponyms.

# ## Exercise

# Whatever dataset you are trying to cultivate, see if you can find it on the web. As you prepare that dataset, think about the steps discussed in this notebook. Clean the data and consider the various ways in which your dataset could accidently be used to identify false positives. If you can't think about all the different ways that can happen, that's okay. In notebook 09.03 we will start to test our datasets against a corpus. I often do not clean datasets perfectly on my first pass. It is only after a few tests that I realize I can clean them further.

# ## Video

# In[51]:


get_ipython().run_cell_magic('html', '', '<div align="center">\n<iframe width="560" height="315" src="https://www.youtube.com/embed/XScpSI3RYQI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>\n</div>\n')

