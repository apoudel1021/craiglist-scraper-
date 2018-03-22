# -*- coding: utf-8 -*-
"""
Created on Wed Jan 31 12:54:28 2018

@author: deadp
"""
from bs4 import BeautifulSoup 
import pandas as pd # Pandas helps you with managing Data (csv, excel, txt, etc.)
import urllib
import time

html = urllib.urlopen('https://northmiss.craigslist.org/search/cta?s=').read()
soup = BeautifulSoup(html, 'html.parser')
paginationtag = soup.find('div', class_='paginator buttongroup firstpage')
pagerange_tags=  paginationtag.find('span',class_='totalcount')
totalitems =int(pagerange_tags.text)

itemsperpage = 120
totalpages = int(totalitems/itemsperpage)

data = pd.DataFrame(columns=['url','Postingdate','Numimage', 'Description', 'Year', 'Makemodels', 'Conditions', 'Cylinders', 'Drive' ,'Fuel', 'Odometer','paintcolor','Size','Titlestatus','Transmission','Vin'])
time.sleep(2)
#extracting filles from only first page 
for i in range(0,1): #for i in range(0,totalitems,120)---to run all the files-running only one page 
   print '(**************************************************)'
   html = urllib.urlopen('https://northmiss.craigslist.org/search/cta?s='+ str(i)).read()
   soup = BeautifulSoup(html, 'html.parser')
   sale_order = soup.find('ul' ,class_='rows')
   total_sales= sale_order.find_all('li', class_='result-row')
   urls,postingdate,sliderinfo,final,finalyear,makeandmodel,condition,cylinder,drive,fuel,odometer,PaintColor,size,title_status,transmission,vin =[None]*16

   for i in range (0,(len(total_sales))):
        print len(total_sales)
        first_sale = total_sales[i]
        urls= (first_sale.p.a.get('href'))
        html = urllib.urlopen(urls).read()
        soup = BeautifulSoup(html, 'html.parser')
        try:
            date_update = soup.find('section', class_='page-container')
            finaldate= date_update.find('header',class_='dateReplyBar')
            posteddate=finaldate.p.find('time',class_='date timeago')
            try:
                postingdate= posteddate.text
            except:
                postingdate=None
            print postingdate
    
            count_thumbs= soup.find('section',class_='userbody')
            count_thumb= count_thumbs.find('figure',class_='iw multiimage')
            
            try:
               
               totalimages = count_thumb.find('div',class_='gallery')
               totalcount= totalimages.find('span',class_='slider-info')
               a,b,c,total = totalcount.text.split(" ")
               sliderinfo= total
               
            except:
               sliderinfo= None
            
            try:
                
                description = count_thumbs.section.extract()
                final= description.text.lstrip().lstrip('QR Code Link to This Post').lstrip()
            except:
                final = None 
           
            try:
                year= count_thumbs.find('div',class_='mapAndAttrs')
                finalyear= year.find('p',class_='attrgroup').span.b.text[:4]
            except:
                finalyear='NA'
            print finalyear     
            
            try:
            
                makeandmodel= year.find('p',class_='attrgroup').span.b.text[4:]
            except:
                makeandmodel='NA'
            
        
            try:
                 con=year.find_all("p",{"class":"attrgroup"})[1]
                 spanlink= con.find_all('span')
                 for span in spanlink:
#                     try:
                          if span.text.split(':')[0]=="condition": 
                              condition= span.text.split(':')[1]
                              print condition
                          elif span.text.split(':')[0]=="cylinders": 
                              cylinder= span.text.split(':')[1]
                              print cylinder
                          elif span.text.split(':')[0]=="drive": 
                              drive= span.text.split(':')[1]
                              print drive
                          elif span.text.split(':')[0]=="fuel": 
                              fuel= span.text.split(':')[1]
                              print fuel
                          elif span.text.split(':')[0]=="odometer": 
                              odometer= span.text.split(':')[1]
                              print odometer
                          elif span.text.split(':')[0]=="paint color": 
                              PaintColor= span.text.split(':')[1]
                              print PaintColor
                          elif span.text.split(':')[0]=="size": 
                              size= span.text.split(':')[1]
                              print size
                          elif span.text.split(':')[0]=="title status": 
                              title_status= span.text.split(':')[1]
                              print title_status
                          elif span.text.split(':')[0]=="transmission": 
                              transmission= span.text.split(':')[1]
                              print transmission
                          elif span.text.split(':')[0]=="VIN": 
                              vin= span.text.split(':')[1]
                              print vin
                          
#                     except: 
#                          a=0
            
            
            except:
                    b=0
            j = data.shape[0]
            data.loc[j]=  [urls,postingdate,sliderinfo,final,finalyear,makeandmodel,condition,cylinder,drive,fuel,odometer,PaintColor,size,title_status,transmission,vin]         
#            data.to_csv('part_3.tsv',sep="\t", encoding='utf-8', index=False)
        except: 
            a=0
            j = data.shape[0]
            data.loc[j]= [urls,postingdate,sliderinfo,final,finalyear,makeandmodel,condition,cylinder,drive,fuel,odometer,PaintColor,size,title_status,transmission,vin] 
#            
                     
             
   
j = data.shape[0]
data.loc[j]=  [urls,postingdate,sliderinfo,final,finalyear,makeandmodel,condition,cylinder,drive,fuel,odometer,PaintColor,size,title_status,transmission,vin]
print data.describe()
data.to_csv('part_3.tsv',sep="\t", encoding='utf-8', index=False)
print 'end' 
        
    
    
   
