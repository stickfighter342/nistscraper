# -*- coding: utf-8 -*-
"""
Created on Sat Feb 15 15:58:34 2020

@author: 21EthanD
"""

from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

products = [] # List to store name of the product
prices = [] # List to store price of the product
ratings = [] # List to store rating of the products

driver.get('https://webbook.nist.gov/cgi/cbook.cgi?Formula=N2&NoIon=on&Units=SI')

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
#print(soup.prettify())
for a in soup.find_all('main'):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class': '_1vC4OE _2rQ-NK'})
    print(a)