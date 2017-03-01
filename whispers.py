#!/usr/bin/env python

from subprocess import Popen, PIPE, call
import re
from gtts import gTTS
import os
import pygame
pygame.init()

# port = input('What\'s the port today?\n> ')

proc = Popen('sudo ngrep -i -W single', stdout=PIPE, shell=True)
for line in proc.stdout:
	line = line.decode(encoding='UTF-8')
	if "<..$.." in line:
		if ".." in line:
			line = line[57:-3]
			line = line.split("..")
		else:
			line = line[58:-3]
			line = line.split(".")
			line[1] = line[1][1:]
		print(line[0].capitalize(), " says: ")
		print(line[1])
		tts = gTTS(text=line[1], lang='en-uk')
		tts.save('/tmp/whisper.mp3')
		pygame.mixer.music.load('/tmp/whisper.mp3')
		pygame.mixer.music.play(0)
