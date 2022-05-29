from cgitb import html
from html.entities import html5
from bs4 import BeautifulSoup
from hyperlink import URL
import requests
import json
from random import randint
from time import sleep
#Method 3 

page = 0 
page_date = []
while page != 10:
    url = f"https://fuckinghomepage.com/page/{page}"
    r= requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    page = page + 1
    print(url)
    #use the None condition with an if argument to append only once to each line in the list
    #create a page_posts function to list all the posts in one day 
    for dates in soup.find_all('a')[0]:
        d= dates.getText()
        page_date.append(d) 
    #print(page_date)
        page_dt = soup.find(class_= "Title")
        print(page_dt)
# page_posts = {} this is going to be a foor loop function. 
# page_date= soup.findAll('a')[0] .getText()
# title = soup.findAll('small').getText()
content = soup.select('p')[2] # need to find another method (perhaps use select function to get the data here)
print(content)
links = soup.findAll('a')[4]['href']
links = soup.find_all('a')
print(links) 
