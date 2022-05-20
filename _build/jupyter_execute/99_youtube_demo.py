#!/usr/bin/env python
# coding: utf-8

# In[1]:


str8 = "Hello my name is William Mattingly"


# In[2]:


print (str8)


# In[3]:


print ("Hello")


# In[4]:


str8 = "asdfasdadsfasdf"


# In[5]:


print (str8)


# In[6]:


print (STR8)


# In[7]:


STR8 = "This is a new string."


# In[8]:


print (STR8)


# In[9]:


string1 = "This is some text."


# In[11]:


print (string1)


# In[12]:


string2 = 'This is another bit of text.'


# In[13]:


print (string2)


# In[14]:


string3  = """
This is a third kind of string.

"""


# In[15]:


print (string3)


# In[17]:


string4 = "This is a bad string"


# In[18]:


print (string4)


# In[19]:


int1 = 1


# In[20]:


print (int1)


# In[21]:


float1 = 1.1


# In[22]:


print (float1)


# In[23]:


boolean1 = True


# In[24]:


print (boolean1)


# In[25]:


boolean2 = False


# In[26]:


print (boolean2)


# In[30]:


name = "William Mattingly... william mattingly..."


# In[28]:


print (name.upper())


# In[29]:


print (name.lower())


# In[31]:


print (name)


# In[32]:


name2 = "william"


# In[33]:


print (name2.capitalize())


# In[37]:


print (name2.replace("iam"," is not my name."))


# In[38]:


print (name2)


# In[39]:


name2 = name2.replace("iam", " is not my name.")


# In[40]:


print (name2)


# In[41]:


name2 = name2.capitalize()


# In[42]:


print (name2)


# In[43]:


name1 = 'William is my name.'


# In[50]:


name3 = name1.replace("William", "Tom")
print (name3)
name3 = name3.lower()
print (name3)
name3 = name3.upper()
print (name3)


# In[55]:


name5 = " William Mattingly    "
print (name5)


# In[56]:


name5


# In[57]:


name5 = name5.strip()
print (name5)


# In[58]:


name5


# In[59]:


name5 = name.split()
print (name5)


# In[64]:


name6 = "William James Mattingly"
print (name6.split("i")[0])


# In[65]:


num1 = 1
num2 = 2


# In[66]:


print (num1+num2)


# In[67]:


print (num1-num2)


# In[68]:


print (num1*num2)


# In[69]:


print (num1%num2)


# In[70]:


print (num1//num2)


# In[71]:


print (7*8)


# In[74]:


print (7//2)


# In[75]:


print (7%2)


# In[80]:


list1 = ["one", 1, 1.0, [1, 2, 3]]


# In[81]:


print (list1)


# In[82]:


tuple2 = ("one", 1, 1.1)


# In[83]:


print (tuple2)


# In[84]:


list1.append(500)


# In[85]:


print (list1)


# In[87]:


tuple2.append(500)


# In[95]:


set1 = {1, 2, 3, 4, 1.0, "one"}


# In[96]:


print (set1)


# In[97]:


dict1 = {"hello": "hallo"}
print (dict1)


# In[106]:


dict2 = {"names": ["tina", "jerry", "bob", "marge"], "ages": [20, 22, 23, 24]}


# In[99]:


print (dict2)


# In[100]:


str8 = "This is a string."


# In[103]:


print (str8[1])


# In[104]:


print (list1[0])


# In[105]:


print (list1[1])


# In[112]:


print (dict2["ages"])


# In[113]:


names = ["tom", "marge", "bob", "cindy"]


# In[116]:


for name in names:
    name = name.capitalize()
    print (name)


# In[121]:


x=0
while x != 10:
    print (x)
    x=x+1


# In[124]:


x=1
if x == 0:
    print ("x is 0")
else:
    print ("x is not 0")


# In[125]:


names = ["tom", "bob", "marge", "cindy"]


# In[129]:


if "jerry" in names:
    print ("Jerry was found")
else:
    names.append("jerry")


# In[128]:


print (names)


# In[138]:


if "bill" in names:
    print ("Bill is in names")
elif "cindy" in names:
    print ("Cindy in names")
elif "suzzy" in names:
    print ("Suzzy in names")
else:
    print ("Neither found.")


# In[133]:


if "bill" not in names:
    print ("Bill is not in names")


# In[144]:


def multiply_three(x):
    x = x*3
    return x

y = multiply_three(6)


# In[145]:


print (x)


# In[146]:


print (y)


# In[149]:


def add_two(x, y):
    result =  x+y
    return result

n = add_two(5, 6)
print (n)


# In[151]:


def add_surname(first_name, last_name="Mattingly"):
    print (first_name, last_name)

add_surname("William", "Smith")


# In[152]:


def print_names(*names):
    for name in names:
        print (name)

print_names("William", "Marge", "Kyle", "Sally")


# In[155]:


class Emperor():
    def __init__(self, name, birth, coronation, death):
        self.name = name
        self.birth = birth
        self.coron = coronation
        self.death = death
    def birth_date(self):
        print (f"{self.name} was born in {self.birth}")

charlemagne = Emperor("Charlemagne", 742, 800, 814)
print (charlemagne)


# In[156]:


print (vars(charlemagne))


# In[157]:


charlemagne.birth_date()


# In[158]:


get_ipython().system('pip install pandas')


# In[159]:


get_ipython().system('pip install requests')


# In[161]:


get_ipython().system('pip install beautifulsoup4')


# In[162]:


import requests


# In[163]:


import pandas as pd


# In[174]:


with open ("data/sample.txt", "r") as f:
    data = f.read()
    data = data+"\nThis is a fourth line."


# In[175]:


with open ("data/sample2.txt", "w") as f:
    f.write(data)


# In[176]:


print (dict2)


# In[177]:


import json


# In[178]:


with open ("data/temp.json", "w") as f:
    json.dump(dict2, f, indent=4)


# In[179]:


with open ("data/temp.json", "r") as f:
    temp = json.load(f)


# In[180]:


print (temp)


# In[181]:


import glob


# In[190]:


files = glob.glob("data/*.txt")
print (files)


# In[191]:


for file in files:
    print (file)
    with open (file, "r") as f:
        data = f.read()
        print (data)


# In[192]:


files2 = glob.glob("data/*/*.txt")
print (files2)


# In[193]:


import os


# In[198]:


walking = os.walk("data/")


# In[195]:


print (walking)


# In[196]:


print (list(walking))


# In[199]:


walking = list(walking)
for item in walking:
    print (item)


# In[200]:


final_files = []
for item in walking:
    root = item[0]
    files = item[2]
    print ("This is the Root")
    print (root)
    print ("These are the Files")
    print (files)
    print ()
    print ()


# In[201]:


for item in walking:
    root = item[0]
    files = item[2]
    for file in files:
        if file.endswith(".txt"):
             print(os.path.join(root, file))


# In[202]:


import pandas as pd


# In[203]:


names_dict = {"names":
        [
            "Tom",
            "Mary",
            "Jeff",
            "Rose",
            "Stephanie",
            "Rodger"
        ]}


# In[204]:


print (names_dict["names"])


# In[205]:


df = pd.DataFrame(names_dict)


# In[206]:


df


# In[207]:


print (df)


# In[209]:


df.to_csv("data/names.csv", index=False)


# In[210]:


df2 = pd.read_csv("data/names.csv")


# In[211]:


df2


# In[212]:


df2["ages"] = [20, 26, 20, 18, 52, 40]


# In[213]:


df2


# In[214]:


names = df2.names
print (names)


# In[215]:


ages = df2.ages
print (ages)


# In[216]:


ages = df2.ages.tolist()
print (ages)


# In[218]:


row1 = df2.iloc[1]
print (row1)


# In[219]:


import requests
from bs4 import BeautifulSoup

url = "https://en.wikipedia.org/wiki/List_of_French_monarchs"
s = requests.get(url)

soup = BeautifulSoup(s.content)
body = soup.find("div", {"id": "mw-content-text"})
for paragraph in body.find_all("p")[:5]:
    if paragraph.text.strip() != "":
        print (paragraph.text)


# In[220]:


import requests


# In[221]:


url = "https://en.wikipedia.org/wiki/List_of_French_monarchs"


# In[222]:


s = requests.get(url)


# In[223]:


print (s)


# In[225]:


print (s.content[:500])


# In[224]:


from bs4 import BeautifulSoup


# In[226]:


soup = BeautifulSoup(s.content)


# In[228]:


toc = soup.find("div", {"id": "toc"})


# In[230]:


print (toc.text)


# In[237]:


first_div = soup.find("div", {"role": "navigation"})
print (first_div.text)


# In[238]:


p_tag = soup.find("p")
print (p_tag.text)


# In[239]:


ptags = soup.find_all("p")
print (len(ptags))


# In[ ]:





# In[251]:


table_data = []
table = soup.find("table", {"class": "wikitable"})
rows = table.find_all("tr")
for row in rows:
    headers = row.find_all("th")
    for header in headers:
        print (header.text.strip())
    cells = row.find_all("td")
    for cell in cells:
        table_data.append(cell.text.strip())


# In[252]:


# print (table_data)


# In[254]:


df3 = pd.read_html(url)[0]
df3


# In[ ]:




