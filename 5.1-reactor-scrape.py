# Fetch and print web page contents
# Example of following a hyperlink to a detail page

import csv
import re
import requests
from bs4 import BeautifulSoup

main_url = 'http://www.nrc.gov/reactors/operating/list-power-reactor-units.html'
base_url = 'http://www.nrc.gov'

r = requests.get(main_url)
html_soup = BeautifulSoup(r.text)

#output the columns as a CSV
    
csvfile = open('reactors.csv', 'w')
csvwriter = csv.writer(csvfile, delimiter = ',')

headers = ('LINK', 'PLANT NAME', 'REACTOR TYPE', 'LOCATION', 'OWNER', 'NRC REGION', 'LICENSED MWt')
csvwriter.writerow(headers)

table = html_soup.find('table')
for row in table.find_all('tr')[1:]:
    col = row.find_all('td')
    link = col[0].find('a').get('href') # link
    reactor_name = col[0].find('a').contents[0] # name
    reactor_type = col[1].string
    location = col[2].string.encode('Latin')
    owner_scrape = col[3].string
    if owner_scrape == None:
        owner = ''
    else:
        owner = col[3].string.encode('Latin')
    region = col[4].string

    print 'Following ' + link
    r_follow = requests.get(base_url + link)
    mega_watts = re.search('Licensed (MWt: |MWt:)</strong>(.*)<br />', r_follow.text)

    parsed_row = (
        link, reactor_name, reactor_type, location, owner, region, mega_watts.group(2)
        )

    csvwriter.writerow(parsed_row)

csvfile.close()

