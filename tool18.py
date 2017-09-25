#!/usr/bin/python2.7

from Tkinter import *
from ttk import Frame, Button, Style
import autopy
import math
import time
import sys

draw = ["drawing"]
draw[0] = []
n = 0
togglevar = 0

class Example(Frame):

	def __init__(self, parent):
		Frame.__init__(self, parent)

		self.parent = parent
		self.initUI()

	def initUI(self):

		def toggleOn():
			global togglevar
			if (togglevar == 0):
				T.configure(state='normal')
				togglevar = 1
			else:
				T.configure(state='disabled')
				togglevar = 0

		def update():
			T.configure(state='normal')
			T.delete('1.0', END)
			T.insert(INSERT, draw[0][:])
			T.configure(state='disabled')

		def intake(q):
			T.configure(state='normal')
			contents = T.get("1.0",END)
			T.delete('1.0', END)
			T.insert(INSERT, contents)
			T.configure(state='disabled')

		def callback(q):
			global draw
			x = self.winfo_pointerx()
			y = self.winfo_pointery()
			print x,y
			draw[0].append([x,y])
			update()

		def split(q):
			global draw
			draw[0].append(5000)
			print "xxx"
			update()

		def play(q):
			def wait():
				time.sleep(0.1)
				return;
			
			def playThis():
				c = 0
				drawing = draw[n]
				i = len(drawing)
				drawing = draw[n]
				autopy.mouse.move(drawing[c][0],drawing[c][1])
				autopy.mouse.toggle(True)
				while (c<i):
					if(drawing[c] == 5000):
						autopy.mouse.toggle(False)
						c += 1
						wait()
					else:
						autopy.mouse.move(drawing[c][0],drawing[c][1])
						autopy.mouse.toggle(True)
						c += 1
						wait()
				autopy.mouse.toggle(False)
				return;
			playThis()

		self.parent.title("Drowquick")
		self.parent.bind('e', callback)
		self.parent.bind('q', split)
		self.parent.bind('z', play)
		self.parent.bind('f', intake)
		self.style = Style()
		self.style.theme_use("default")
		
		frame = Frame(self, relief=RAISED, borderwidth=1)
		frame.pack(fill=BOTH, expand=True)
		
		self.pack(fill=BOTH, expand=True)

		okButton = Button(self, text="Record!", command=callback)
		okButton.pack(fill=X)
		splitButton = Button(self, text="Split!", command=split)
		splitButton.pack(fill=X)
		enableButton = Button(self, text="Textbox on/off", command=toggleOn)
		enableButton.pack(fill=X)
		T = Text(self, height=180, state='disabled')
		T.pack()

def main():
  
	root = Tk()
	root.geometry("300x1080+0+0")
	app = Example(root)
	root.mainloop()  

if __name__ == '__main__':
	main()
