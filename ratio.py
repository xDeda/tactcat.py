#!/usr/bin/env python

import sys
import urllib
import urllib.request
from urllib.request import Request, urlopen
from urllib.parse import quote
from bs4 import BeautifulSoup
import clipboard

player = sys.argv[1]
req = Request('http://api.micetigri.fr/player/' + player, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
cheeseratio = soup.findAll('td')[7].string
firstratio = soup.findAll('td')[12].string
print(player + ' - cheese ratio: ' + cheeseratio + ' | first ratio: ' + firstratio)
clipboard.copy(player + ' - cheese ratio: ' + cheeseratio + ' | first ratio: ' + firstratio)
