#! usr/bin/python3
'''

Grab the Scripts of 'Friends' from the resource website.

All the resources of the scripts are provided by Crazy For Friends.   
    Resource website URL: http://www.livesinabox.com/friends/scripts.shtml

The resources are divided into each episode.

usage: grab-webcontents.py [directory name]


'''

import sys
import re
import os
import requests
from urllib.parse import urljoin
from bs4 import BeautifulSoup

# Assign Header information of your User-Agent.
headers = {'User-Agent': 'Mozilla/5.0 (Linux; Android 9; Lenovo TB-7305F Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/81.0.4044.138 Safari/537.36'}

# Assign the main site of the resources.
url = 'http://www.livesinabox.com/friends/scripts.shtml'

# Grab the content of the main site.
resp = requests.get(url, timeout=60, headers=headers)

# Modify the encoding of the response if you need.
resp.encoding = resp.apparent_encoding

# Pass the respsonse to BeautifulSoup.
soup = BeautifulSoup(resp.text,'html.parser')

# Find out 'a' tags.
atags = soup.find_all('a')

# Assign a Regex pattern to list links of episodes.
pattern = r'Episode\s*\d+'

# List links of the episodes.
links = [urljoin(url,lnk.get('href')) for lnk in atags 
        if re.search(pattern,lnk.get_text(strip=True))]

# Create a directory to store all the script contents in it.
if len(sys.argv)>1:
    dr = sys.argv[1]
else:
    dr = '.scripts'
print('Created Directory: ',dr)
os.makedirs(dr, exist_ok=True)

# Assign file names by each of the episodes.
paths = [os.path.join(dr,os.path.basename(p)) for p in links]

#for p in paths: print(p)
#print(len(paths))

# Write the contents in local files by each of the episodes.
#print(links[0])
#print(paths[0])
#for i in range(1):
for i in range(len(links)):
    with open(paths[i],'wt') as fw:
        fw.write( requests.get(links[i], timeout=60, headers=headers).text )


