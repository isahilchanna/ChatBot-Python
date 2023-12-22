# import requests
#
# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
#
# # check status code for response received
# # success code - 200
# print(r)
#
# # print content of request
# print(r.content)

#
# import requests
#
# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
#
# # print request object
# print(r.url)
#
# # print status code
# print(r.status_code)


# import requests
# from bs4 import BeautifulSoup
#
# # Making a GET request
# r = requests.get('https://www.geeksforgeeks.org/python-programming-language/')
#
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
#
# s = soup.find('div', class_='entry-content')
#
# lines = s.find_all('p')
#
# for line in lines:
#     print(line.text)


# import requests
# from bs4 import BeautifulSoup
#
# # Making a GET request
# r = requests.get('https://www.instagram.com/talwiinder')
#
# # Parsing the HTML
# soup = BeautifulSoup(r.content, 'html.parser')
#
# # find all the anchor tags with "href"
# for link in soup.find_all('a'):
#     print(link.get('href'))
from bs4 import BeautifulSoup as bs
import pandas as pd
pd.set_option('display.max_colwidth', 500)
import time
import requests
import random

# List of Authors and Quotes
authors = []

quotes = []

# List of URLs
urls = [f"http://quotes.toscrape.com/page/{i}/" for i in range(1, 11)]

# List for Randomizing our request rate
rate = [i / 10 for i in range(10)]

# Iterating through the URLS
for url in urls:

    # Accessing the Webpage
    page = requests.get(url)

    # Getting the webpage's content in pure html
    soup = bs(page.content)

    # Adding the authors and quotes to their lists
    authors.extend([i.text for i in soup.find_all(class_='author')])

    quotes.extend([i.text for i in soup.find_all(class_='text')])

    # Checking to see if we hit our required number of quotes then breaking the loop
    if len(quotes) >= 52:
        break

    # Randomizing our request rate
    time.sleep(random.choice(rate))