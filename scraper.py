from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome()

products = [] # List to store name of the product
prices = [] # List to store price of the product
ratings = [] # List to store rating of the products

driver.get('https://www.flipkart.com/laptops/~buyback-guarantee-on-laptops-/pr?sid=6bo%2Cb5g&uniqBStoreParam1=val1&wid=11.productCard.PMU_V2')

content = driver.page_source
soup = BeautifulSoup(content)

for a in soup.findAll('a', href=True, attrs={'class':'_31qSD5'}):
    name=a.find('div', attrs={'class':'_3wU53n'})
    price=a.find('div', attrs={'class':'_1vC4OE _2rQ-NK'})
    print(name)
