#!/usr/bin/env python

from tkinter import *
import pyautogui
import math

A = [0,2], [3,2], [4,3], [4,8], [1,8], [0,7], [0,5], [1,4], [4,4]
B = [0,0], [0,8], [3,8], [4,7], [4,3], [3,2], [0,2]
C = [4,3], [3,2], [1,2], [0,3], [0,7], [1,8], [3,8], [4,7]
D = [4,0], [4,8], [1,8], [0,7], [0,3], [1,2], [4,2]
E = [0,5], [4,5], [4,3], [3,2], [1,2], [0,3], [0,7], [1,8], [4,8]
F = [4,0], [2,0], [1,1], [1,8], 5000, [4,3], [1,3]
G = [4,8], [1,8], [0,7], [0,3], [1,2], [3,2], [4,3], [4,9], [3,10], [0,10]
H = [0,0], [0,8], 5000, [0,2], [3,2], [4,3], [4,8]
I = [1,8], [1,2], [0,2], 5000, [2,8], [0,8]
J = [2,2], [3,2], [3,9], [2,10], [1,10], [0,9], [0,8]
K = [0,0], [0,8], 5000, [4,2], [2,4], [0,4], 5000, [4,8], [4,6], [2,4]
L = [1,8], [1,0], [0,0], 5000, [0,8], [2,8]
M = [0,8], [0,2], [3,2], [4,3], [4,8], 5000, [2,8], [2,2]
N = [0,8], [0,2], [3,2], [4,3], [4,8]
O = [1,2], [3,2], [4,3], [4,7], [3,8], [1,8], [0,7], [0,3], [1,2]
P = [0,10], [0,2], [3,2], [4,3], [4,7], [3,8], [0,8]
Q = [4,8], [1,8], [0,7], [0,3], [1,2], [4,2], [4,10]
R = [0,8], [0,2], [3,2], [4,3], [4,4]
S = [4,3], [3,2], [1,2], [0,3], [0,4], [1,5], [3,5], [4,6], [4,7], [3,8], [1,8], [0,7]
T = [0,0], [0,7], [1,8], [3,8], 5000, [3,2], [0,2]
U = [0,2], [0,7], [1,8], [4,8], [4,2]
V = [0,2], [0,6], [2,8], [4,6], [4,2]
W = [0,2], [0,7], [1,8], [4,8], [4,2], 5000, [2,3], [2,8]
XX = [0,8], [0,6], [4,2], 5000, [4,8], [4,6], [0,2]
YY = [0,2], [0,7], [1,8], [4,8], 5000, [4,2], [4,9], [3,10], [0,10]
Z = [0,2], [4,2], [0,6], [0,8], [4,8]
comma = [1,8],[1,7],[2,7],[2,9],[1,10]
dot = [1,8],[1,7],[2,7],[2,8]
line = [1,4],[5,4]
slash = [0,8],[1,5],[3,3],[4,0]
colon = [1,2],[2,2],[2,3],[1,3],[1,2],5000,[1,7],[1,6],[2,6],[2,7],[1,7]
semicolon = [1,2],[2,2],[2,3],[1,3],[1,2],5000,[2,7],[1,7],[1,6],[2,6],[2,8],[1,9]

posx = 0
posy = 0

def writeLetter(letter):
	global posx, posy, xx, yy
	ZZ = 2
	yy = posy
	if (letter == " "):
		xx = xx+int(6*ZZ)
	else:
		n = 1
		i = len(letter)
		pyautogui.moveTo(xx+int(letter[0][0]*ZZ),yy+int(letter[0][1]*ZZ))
		pyautogui.mouseDown(button='left')
		while (n<i):
			if (letter[n] == 5000):
				pyautogui.mouseUp(button='left')
				pyautogui.moveTo(xx+int(letter[n+1][0]*ZZ),yy+int(letter[n+1][1]*ZZ))
				pyautogui.mouseDown(button='left')
	
			else:
				pyautogui.moveTo(xx+int(letter[n][0]*ZZ),yy+int(letter[n][1]*ZZ))
	
			n = n+1

		pyautogui.mouseUp(button='left')
		if (letter == I):
			xx = xx+int(4*ZZ)
		elif (letter == L):
			xx = xx+int(4*ZZ)
		elif (letter == T):
			xx = xx+int(5*ZZ)
		else:
			xx = xx+int(6*ZZ)
	return;

def writeOut(*args):
	global posx, posy, xx
	pos = pyautogui.position()
	posx = pos[0]
	posy = pos[1]
	xx = pos[0]

	stringy = v.get()
	stringy = stringy.upper()
	n = 0
	stringy = list(stringy)
	i = len(stringy)
	while (n<i):
		if (stringy[n] == " "):
			xx = xx+12
		elif (stringy[n] == "X"):
			writeLetter(XX)
		elif (stringy[n] == "Y"):
			writeLetter(YY)
		elif (stringy[n] == "."):
			writeLetter(dot)
		elif (stringy[n] == ","):
			writeLetter(comma)
		elif (stringy[n] == "-"):
			writeLetter(line)
		elif (stringy[n] == "/"):
			writeLetter(slash)
		elif (stringy[n] == ":"):
			writeLetter(colon)
		elif (stringy[n] == ";"):
			writeLetter(semicolon)
		else:
			writeLetter(eval(stringy[n]))
		n = n+1
	return;

def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")

master = Tk()
master.wait_visibility(master)
master.title('Write Stuff')
master.geometry("250x30")
master.bind("z", writeOut)
master.eval('tk::PlaceWindow %s center' % master.winfo_toplevel())
v = StringVar()
TD = Entry(master, width=25, state='normal', font=("fixedsys", 9), textvariable=v)
v.set("Hello mom")
TD.bind("<Tab>", focus_next_window)
TD.bind("<Return>", writeOut)
TD.pack(expand=True, fill=BOTH, side=LEFT)
writeButton = Button(master, text="Write", command=writeOut, font=('Georgia', '9'))
writeButton.pack(expand=False, fill=Y, side=LEFT)

master.mainloop()
