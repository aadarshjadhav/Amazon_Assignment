#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import requests
from bs4 import BeautifulSoup
import urllib
import json
import html5lib
from csv import reader
import xlrd 




df_csv= pd.read_csv(r"C:\\Users\\aadar\\OneDrive\\Documents\\Amazon Web Scrapping\\Amazon Scraping.csv")
df_csv.index
df_csv.head()

row_Asin=df_csv['Asin']
row_Asin_value=row_Asin[0]
row_Asin_value


row_country=df_csv['country']
row_country_value=row_country[0]
row_country_value

#Link='https://www.amazon.'+ row_country_value+ '/dp/' +row_Asin_value
#Link

def Data_Analysis(Link):
    
    headers = {'User-Agent1': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.844 Safari/537.36'}
    page = requests.get(url=Link, headers=headers)
    page.content
    soup = BeautifulSoup(page.content, 'html.parser')
    
    soup.extend
    return soup

    error=soup2.find(attrs={'accept-charset':"utf-8"})
    error_message=error['action']
    error_messaga='/s/ref=404_search'

    #soup

    
    if error_message != error_messaga:
        product_title= soup.find("span",{'class':"a-size-large product-title-word-break"})
        #product_image_URL
        #price_of_product
        #product_details
        #product_title=product_title.string
        #product_title

        product_image_URL= soup.find(attrs={"class":"imgTagWrapper","id":"imgTagWrapperId"})
        #product_image_URL


        p = product_image_URL.find('img')
        #print(p['src'])


        product_image_link_string= p['src']

        price_of_product=soup.find(attrs={'class':"a-offscreen"})
        price_of_product=price_of_product.string
        #price_of_product


        product_details=soup.find(attrs= {'class':"a-list-item",'class':"a-section a-spacing-medium a-spacing-top-small", "id":"feature-bullets"})
        p = product_details.find('span')
        p=p.string
        #p

        dictionary = {

          "Product_URL":Link,
          "Product_Title": product_title,
          "Product_Image_URL": product_image_link_string,
          "Price_of_the_Product": price_of_product,
          "Product_Details": p
        }
        #print(dictionary)
        return(dictionary)

    
    return("not available")


df_out_main=pd.DataFrame()


index=0
#df_csv.index

for index in range(0,101) :
        asin=(df_csv["Asin"][index]) 
        country=(df_csv["country"][index])
        Link='https://www.amazon.'+ country + '/dp/' + asin
        d_result=Data_Analysis(Link)
        dt_result=pd.DataFrame(list((d_result)))
        df_out_main=pd.concat([df_out_main,dt_result], ignore_index=True, axis=0)
        

        

dictionary=df_out_main.to_dict('dict')
dictionary

with open('results.json', 'w') as fp:
    json.dump(dictionary, fp)


# In[ ]:




