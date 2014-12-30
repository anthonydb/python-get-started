# Fetch and print web page contents
# We're looking at the U.S. Nuclear Regulatory Commission
# list of power reactor units

import re
import csv
import requests
from bs4 import BeautifulSoup

main_url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'
base_url = 'http://www.nrc.gov'

# fetch the main page and run through BS4
r = requests.get(main_url)
html_soup = BeautifulSoup(r.text)

# output the columns as a CSV
csvfile = open('reactors.csv', 'wb')
csvwriter = csv.writer(csvfile, delimiter=',')

# create headers for the CSV
headers = ('LINK', 'PLANT NAME', 'REACTOR TYPE', 'LOCATION',
           'OWNER', 'NRC REGION', 'LICENSED MWt')
csvwriter.writerow(headers)

# find the table and extract the columns from each row
table = html_soup.find('table')
for row in table.find_all('tr')[1:]:
    col = row.find_all('td')
    link = col[0].find('a').get('href')  # link to detail page
    reactor_name = col[0].find('a').contents[0]  # name
    reactor_type = col[1].string
    location = col[2].string.encode('Latin')  # encoding to fix character issues
    owner_scrape = col[3].string
    if owner_scrape is None:
        owner = ''
    else:
        owner = col[3].string.encode('Latin')
    region = col[4].string

    # follow the hyperlink for the reactor to the detail page
    print 'Following ' + link
    r_follow = requests.get(base_url + link)

    # regex search to pull mega watts data
    mega_watts = re.search('Licensed (MWt: |MWt:)</strong>(.*)<br />', r_follow.text)

    # a tuple for the final parsed row
    parsed_row = (link, reactor_name, reactor_type, location,
                  owner, region, mega_watts.group(2))

    csvwriter.writerow(parsed_row)

csvfile.close()
