# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 13:25:32 2018

@author: deadp
"""

from bs4 import BeautifulSoup 
import urllib
html = urllib.urlopen(raw_input('Enter the url')).read()
soup = BeautifulSoup(html, 'html.parser')
sale_order = soup.find('ul' ,class_='rows')
total_sales= sale_order.find_all('li', class_='result-row')
URL = []
Title =[]
Price =[]
city = []
state=[]
for i in range (len(total_sales)):
    first_sale = total_sales[i]
    url= first_sale.p.a.get('href')
    URL.append(url)
    title=first_sale.p.a.text
    Title.append(title)
    first_year= first_sale.p.find('span',class_='result-price')
    if first_year is not None:
            price = first_year.text.replace("$","")
    else:
            price= first_year= 'NA'
    Price.append(price)

    first_city= first_sale.p.find('span',class_='result-hood')
    if first_city is not None:
        first_city= first_city.text
        first_city=first_city[2:-1]
        try:
            first_city,first_state= first_city.split(',')
        except:
            first_state='NA'
    else:
        first_city= 'NA'
        first_state= 'NA'
    
    city.append(first_city)
    state.append(first_state)
    

        
            
import pandas as pd 
test_df = pd.DataFrame({ 'url' : URL,
                         'title': Title,
                         'price' : Price,
                         'City': city,
                         'State':state})
print test_df
test_df

test_df.to_csv('part_1.tsv',sep="\t", encoding='utf-8', index=False)       
        
      
        
        