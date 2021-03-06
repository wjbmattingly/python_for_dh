#!/usr/bin/env python
# coding: utf-8

# # <center>Introduction to Python</center>

# ## Why Should Humanists Learn to Code?

# As a humanist who had a rather traditional education, I know all too well the skepticism that is placed on digital approaches to humanist inquiry. This skepticism, believe it or not, is well earned and should not be scoffed at. Learning to code will mean that you, as a humanist, can do things that other humanist who cannot code will not be able to do. You will be able to analyze thousands of texts in minutes. You will be able to find relevant images among 300,000. You will be able to clean texts so that you can perform more complex searches. All of these benefits, however, come at a cost. You must, by default, surrender some tasks to a machine and this means that the tasks you are performing may not be 100% accurate. As a result, you may miss certain key pieces of information. If you decide to learn to code as a humanist, you must become familiar and comfortable with these concepts.
# 
# In computer science and data science, this caveat is well-understood and accepted. In the humanities, however, it is and should be met with skepticism. Humanists are researchers who pride themselves in close reading of texts. In some cases, a historian writing a PhD may spend years with only a handful of documents. So how then do we handle this seemingly paradoxical position. The answer is understanding and not ignoring the weaknesses coding presents in a research workflow. In understanding that weakness, you, as a humanist, must make it known to your audience that your methods are not 100% accurate, but you have taken steps necessary to ensure as high an accuracy as possible. Further, should you use coding to engage in other adventures, such as machine learning, you should be reluctant to rest conclusions strongly on the results of your computational approaches unless you are well-acquainted with the mathematics and statistics behind them.
# 
# With this scary warning out of the way, let us then consider the benefits of coding. We, as humans, are fundamentally flawed. We must sleep, eat, socialize, enjoy relationships with loved ones; essentially, we must live our lives. We are mortal beings who will die. Our time is one of our greatest commodities. All of these things mean that we cannot operate 24/7 on a single task for 365 days a year. Furthermore, we are terrible at performing repetitive tasks. We, as humans, make mistakes.
# 
# Coding allows us to pass tasks to a computer that could otherwise be done by a human. Many of the tasks we need to perform as humanists are repetitive and we, as humans, are prone to make mistakes. Coding a solution to perform a repetitive specific task is known as **automation**. Being able to automate these tasks can radically reduce the amount of time we use to do these tasks, from hours, weeks, or even years, to seconds, minutes, or hours. Imagine having to grab data from an archive website. Imagine that the information you need is found on 2,000 different pages. How long would it take you to go to each of those pages and copy and paste the text into a Word Document? In Python, that task can be coded in minutes and left to run for an hour. This allows you, the researcher to go off and do some other task more essential or, perhaps, enjoy a nice tea break in a hammock so that when you return to analyze the documents, you will be well-rested.
# 
# But coding does not just allow us to automate tasks like this. It also allows us to systematically clean data. Imagine you wanted to search across PDF scans of medieval Latin. This problem presents many key issues that make such a task impossible or unreliable. First, medieval Latin did not have any firm spelling convention. This means that some scans may have variant spelling of words. Second, Latin is a highly inflected language, meaning word order is not important, rather the ending of a given word is. This means that each word can have as many as 8 forms in nouns and sometimes as many as 25+ forms if it is a verb. In addition to this, your texts are scans. Are those scans even searchable? If they are, was the OCR, or Optical Character Recognition, accurate? If it was done prior to 2015, it likely is not. If after, then the scans may be in a bad enough state where the OCR is not accurate. In addition to these problems, any OCR system will retain line breaks, meaning if the key word that you want to search for is hyphenated because the word is broken up between two lines, you need to account for that in your search. Next, we need to take into account editor notations, which often are noted in brackets, parentheses, and carrots. While this example is certainly a complex one, it is perfectly common. And while I am using Latin to demonstrate a greater issue with inflected languages, these same issues, especially those around OCR, surface with English texts. Coding allows us to address each and every one of these issues, some more easily than others.
# 
# The issue of searching is further complicated when this needs to be done for many documents simultaneously. Imagine if these issues surfaced in 5,000 different PDFs that you needed to analyze. Could you realistically run all these searches across 5,000 documents? If you could, would your results be good? To answer the former, yes, if you are willing to spend months doing it; to answer the latter, likely not. Programming allows for you to develop programs that perform all these tasks across all 5,000 documents. It may take a few days to run, but in the end you will have cleaned, structured data, that searchable. Further, when you run a search, you will not simply hit ctrl+f. You will code your own search method so that your simple search can return very complex results that accounts for variance in the text. 

# ## What is Python?

# Python is a programming language. Programming languages are ways that we, as humans, can write commands that will then be executed by a computer. There are many different programming languages available for humanists to choose from:
# 
# 1. C
# 2. Python
# 3. JavaScript
# 4. R
# 5. HTML (this is debatable)
# 
# Not all programming languages are created equal. Some are best used for developing software, such as C; others are best suited for web development, such as HTML and JavaScript. And others are great at statistical analysis, R (and Python). Where does Python excel? Python excels in many areas. One thing that sets it apart from other programming languages for new coders is that it is easy to read and easy to write.
# 
# It is relatively easy to write compared to other programming languages because the syntax, or way in which you write tasks in code, is straightforward. It is easy to read because Python uses forced indentation.
# 
# Since it's creation in the early 1990s, Python has soared in popularity which has, in turn, resulted in a large community of programmers and a large number of libraries available. We will learn about libraries later in this textbook. For now, think of libraries as large quantities of code that have already been written for you so that you can write 1 line of code rather than hundreds or even thousands!
# 
# Today, Python is one of the most widely used programming languages and is considered the essential language for text analysis, machine learning, data analysis (alongside R), web scrapping, and much more.
# 
# Python (as of this writing) is currently in version 3.10.2. Let's break each of these numbers down. The 3 refers to the main Python language. Python 2 still exists (in fact it comes standard on all Macs), but it is no longer supported and is slowly being replaced by Python 3. You should not invest time in learning Python 2 as it is only used to support legacy software and has a high number of security issues due to its depreciated status. This is important to note because certain things are coded differently between the two programming languages. If you were to look for help on a coding forum, such as StackOverflow, it is important to know about these distinctions.
# 
# The 10.2 in Python 3.10.2, tells us specifically what version of Python 3. Not all code from certain libraries is backwards compatible, meaning some libraries require a specific version of Python, so understanding this now as a concept will save confusion later. Each time a new version comes out, new features are available, so it is important to stay up-to-date with current versions, but it is not always essential.

# ## Why Python?

# For all the above reasons, I encourage humanists to learn Python as their first programming language. It is one of the easiest languages to learn, straightforward to write, and can solve most of the programmatic problems a humanist may face. The large quantities of libraries and tutorials mean that there are few tasks that will prove impossible to do.
# 
# If you are sold on Python, then continue reading this textbook as we learn how to install it and use it as humanists.

# In[ ]:




