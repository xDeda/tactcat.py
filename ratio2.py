#!/usr/bin/env python

import sys
from urllib.request import Request, urlopen
from urllib.parse import urlparse
from bs4 import BeautifulSoup

player = sys.argv[1]
url = 'https://cheese.formice.com/transformice/mouse/' + player.replace("#", "%23")
req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
html = urlopen(req).read()
soup = BeautifulSoup(html, 'html.parser')
cg = soup.findAll('td')[5].text		# cheesegathered
f = soup.findAll('td')[9].text		# firsts
cr = soup.findAll('td')[7].text		# cheeseratio
fr = soup.findAll('td')[11].text	# firstratio

if '(' in cg:
	cg = cg.split('(')[0]
if '(' in f:
	f = f.split('(')[0]

print(
    f"\033[93m\n{'cheese gathered:':<16}", f"\033[00m{cg:>11}",
    f"\033[96m\n{'f:':<16}", f"\033[00m{f:>11}",
    f"\033[95m\n{'cheese ratio:':<16}", f"\033[00m{cr:>10}",
    f"\033[92m\n{'first ratio:':<16}", f"\033[00m{fr:>10}",
)

print("cg: {}, f: {}, cr: {}, fr: {}".format(cg, f, cr, fr))
