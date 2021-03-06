#!/usr/bin/env python

from subprocess import Popen, PIPE
import re
import urllib
import urllib.request
import clipboard
from urllib.parse import quote
from bs4 import BeautifulSoup
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

Notify.init('Result')

proc = Popen('sudo ngrep -i -W single \'tactcat|Tactcat|Ostronnyllet|ostronnyllet\'', stdout=PIPE, shell=True)
for line in proc.stdout:
	line = line.decode(encoding='UTF-8')
	line = re.search(r'\[\[(.*)\]\]', line)
	if line:
		line = line.group().strip('[]')
		print(line)
		query = urllib.parse.quote(line)
		with urllib.request.urlopen('https://www.youtube.com/results?search_query=' + query) as url:
			html = url.read()
		soup = BeautifulSoup(html, 'html.parser')
		for vid in soup.findAll(attrs={'class':'yt-uix-tile-link'}):
				link = 'https://www.youtube.com' + vid['href']
				if vid.string != None:
					clipboard.copy('[ ' + vid.string + ' ] ' + link)
					print('Found!')
					print('[' + vid.string + '] = ' + link)
					Hello=Notify.Notification.new(vid.string, link, 'face-wink')
					Hello.show()
					break
				else:
					Hello=Notify.Notification.new('No, sorry', 'No result!	', 'face-wink')
					Hello.show()
					break
