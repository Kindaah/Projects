from cgitb import html
from html.entities import html5
from lib2to3.pytree import convert
from bs4 import BeautifulSoup
import requests
import json
from random import randint
from time import sleep
from datetime import datetime


# I want to grab a 100 pages, parse and extract the data
# I want to organize the data in dicts 
# Save the data to json file
# # insert a function for time-sleep  


# grab the first url and write the loop for the rest of the urls
# need to revise the code in all methods to incude scrapping the home_page or excluding page 1 
# home_page= "https://fuckinghomepage.com/"

#method 1: 
page = []
dates = []
for i in range(10):
    url = "https://fuckinghomepage.com/page/"  + str(i)
    page.append(url)
    r = requests.get(url)
    soup = BeautifulSoup(r.content, "html.parser")
    #print(page)

    page_date= soup.findAll('a')[0] .getText()
    datetime_object = datetime.strptime(page_date, '%B %d, %Y')
    strg_date= f"{datetime_object.year}{'{:02d}'.format(datetime_object.month)}{'{:02d}'.format(datetime_object.day)}"
    #print(strg_date)
    dates.append(strg_date)
    


# print(soup.prettify())


# def page_posts():


    # print(page_date)
    # page_day = soup.findAll('b')
    # print(page_day)
    titles = soup.findAll('small') 
    # #need to create a for loop to only pull the text and not the links  
    print(titles)
    # content = soup.findAll('p')[2]
    # # # # #need to only print the 2, 4, 6, 8, 10 and only get the text 
    # print(content)
    # links = soup.select('a', class_= "PostBody") 
    # # # # #need to only get the a tags in the post body class only 
    # print(links)

# sleep(randint(2, 101))

#Method 2: 
# for i in range(101):
#     url = "https://fuckinghomepage.com/page={}".format(i)
#     r = requests.get(url)
#     soup = BeautifulSoup(r.content, 'html.parser')
#     print(soup.prettify())



# #check if you can build nested dictionary 

# pages_data = {}


#     # label5 = "WOD"
#     # title5 = soup.findAll('small')[4].getText()
#     # content_section5 = soup.findAll('p')[10].getText()
#     # link_section5 = soup.findAll('a')[4]['href']

# with open('100_data.json', 'w') as f:
#     json.dump(pages_data, f)
# # need to loop in the page date 
# # page_date= print(soup.findAll('a')[0] .getText())

# # print(soup.findAll('a')[0])
# #print(soup.findAll('a')[0] .getText())
# # print(soup.findAll('p')[0].getText())
# # print(soup.findAll('p')[2].getText())