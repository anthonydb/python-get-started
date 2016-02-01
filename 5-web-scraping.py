#!/usr/bin/env python

"""
Getting Started with Python:
Web Scraping

Fetch and print web page contents
We're looking at the U.S. Nuclear Regulatory Commission's
list of power reactor units
"""

import csv
import requests
from bs4 import BeautifulSoup

url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'

r = requests.get(url)
html_soup = BeautifulSoup(r.text, 'html.parser')
print html_soup.prettify().encode('UTF-8')

# find all links on the page and print first 20
links = html_soup.find_all('a')
for a in links[0:20]:
    print a

for a in links[0:10]:
    print a.get('href')


# locate and print a particular link
t_link = html_soup.find(title="NRC Twitter Feed")
print t_link
print t_link.get('href')


# find and print table
table = html_soup.find('table')
print table.prettify().encode('UTF-8')


# find and print all the table's rows
table = html_soup.find('table')
for row in table.find_all('tr'):
    print row


# print table's column values
table = html_soup.find('table')
for row in table.find_all('tr')[1:]:
    col = row.find_all('td')
    print col[0].find('a').get('href')  # link
    print col[0].find('a').contents[0]  # name
    print col[1].string
    print col[2].string
    try:                                # sometimes this field is blank
        print col[3].string
    except:
        print ''
    print col[4].string


# output the columns as a CSV
csvfile = open('reactors.csv', 'wb')
csvwriter = csv.writer(csvfile, delimiter=',')

headers = ('LINK', 'PLANT NAME', 'REACTOR TYPE',
           'LOCATION', 'OWNER', 'NRC REGION')
csvwriter.writerow(headers)

table = html_soup.find('table')
for row in table.find_all('tr')[1:]:
    col = row.find_all('td')
    link = col[0].find('a').get('href')  # link
    reactor_name = col[0].find('a').contents[0]  # name
    reactor_type = col[1].string
    location = col[2].string.encode('Latin')
    owner_scrape = col[3].string
    if owner_scrape is None:
        owner = ''
    else:
        owner = col[3].string.encode('Latin')
    region = col[4].string

    parsed_row = (link, reactor_name, reactor_type, location, owner, region)

    csvwriter.writerow(parsed_row)

csvfile.close()
