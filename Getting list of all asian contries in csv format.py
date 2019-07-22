#create a new directory 
mkdir Web_Scrapping
cd Web_Scrapping
#import library requests 
import requests

website_url =requests.get("https://en.wikipedia.org/wiki/List of Asian countries by area").text

from bs4 import BeautifulSoup

#Soup is a Python package for parsing HTML and XML documents. It creates a parse tree for parsed pages that can be used to extract data from HTML, which is useful for web scraping. 
#Prettify() function in BeautifulSoup will enable us to view how the tags are nested in the document.
soup = BeautifulSoup(website_url,'lxml')
print(soup.prettify())

#sara data table ke class wikitable sortable me h 

My_table = soup.find("table",{"class":"wikitable sortable"})
My_table


# To find all links in My_table 


links=My_table.findAll("a")
links


# Save all data in List name countries

Countries=[]
for link in links :
    Countries.append(link.get("title"))
    
print(Countries)


#converting list in dataframe 

import pandas as pd
df=pd.DataFrame()
df['Country']=Countries
df


# Converting pandas datadrame into csv file and exporting it .


df.to_csv("countriesss.csv")
df



