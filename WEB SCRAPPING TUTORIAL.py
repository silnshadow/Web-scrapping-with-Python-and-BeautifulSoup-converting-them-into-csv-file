#!/usr/bin/env python
# coding: utf-8

# In[8]:


pwd


# In[9]:


mkdir Web_Scrapping


# In[10]:


cd Web_Scrapping


# In[11]:


pip install virtualenv


# In[14]:


virtualenv --version


# In[15]:


conda - v


# In[16]:


pwd


#  how to scrape data in Python using BeautifulSoup.

# In[17]:


import requests


# In[27]:


import requests

website_url =requests.get("https://en.wikipedia.org/wiki/List of Asian countries by area").text

from bs4 import BeautifulSoup

#Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. 
#Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document.
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())


# In[28]:


#sara data table ke class wikitable sortable me h 
My_table = soup.find("table",{"class":"wikitable sortable"})
My_table


# In[29]:


links=My_table.findAll("a")
links


# In[30]:


Countries=[]
for link in links :
    Countries.append(link.get("title"))
    
print(Countries)


# In[34]:


#converting list in dataframe 
import pandas as pd
df=pd.DataFrame()
df['Country']=Countries
df


# In[36]:


df.to_csv("countriesss.csv")
df


# In[ ]:




