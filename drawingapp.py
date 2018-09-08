from tkinter import *
import pyautogui
import math

draw = []
pos = pyautogui.position()
fromx = 0
fromy = 0
tox = 0
toy = 0
phase = 1
togglevar = 0

def callback(e):
	global fromx, fromy, tox, toy, phase
	pos = pyautogui.position()
	if (phase == 0):
		tox = pos[0]
		toy = pos[1]
		w.create_line((fromx-239)-master.winfo_x(),(fromy-31)-master.winfo_y(),(tox-239)-master.winfo_x(),(toy-31)-master.winfo_y(), fill="Black")
		fromx = pos[0]
		fromy = pos[1]
		draw.append([fromx,fromy])
		print("(phase 0)",fromx,",",fromy)
	else:
		fromx = pos[0]
		fromy = pos[1]
		draw.append([fromx,fromy])
		print("(1 phase)",fromx,",",fromy)
		phase = 0


def split(q):
	global fromx, fromy
	pos = pyautogui.position()
	draw.append(5000)
	fromx = pos[0]
	fromy = pos[1]
	draw.append([fromx,fromy])
	print("5000")

def getArray(drawing):
	n = 0
	i = len(drawing)
	print(len(drawing))
	
	thethingX = drawing[0][0]
	thethingY = drawing[0][1]
	
	while (n<i):
		if (drawing[n] != 5000):
			if (drawing[n][0] < thethingX):
				thethingX = drawing[n][0]
				print(thethingX, "is the new X low")
			if (drawing[n][1] < thethingY):
				thethingY = drawing[n][1]
				print(",",thethingY, " is the new Y low")
		n = n+1
	
	n = 0
	
	while (n<i):
		if (drawing[n] != 5000):
			drawing[n][0] = drawing[n][0] - thethingX
			drawing[n][1] = drawing[n][1] - thethingY
			# print(array[n], ",")
		# elif (array[n] == 5000):
			# print("5000,")
		n = n+1

	return drawing


def getDraw():
	global draw
	drawing = str(T.get("1.0",END))
	T.configure(state='disabled')

	draw = eval(drawing)
	drawing = draw

	drawing = getArray(drawing)

	c = 0
	i = len(drawing)
	w.create_line(drawing[c][0]+50,drawing[c][1]+50,drawing[c+1][0]+50,drawing[c+1][1]+50, fill="Black")
	while (c+1<i):
		if(drawing[c] == 5000 or drawing[c+1] == 5000):
			c += 1
		else:
			w.create_line(drawing[c][0]+50,drawing[c][1]+50,drawing[c+1][0]+50,drawing[c+1][1]+50, fill="Black")
			c += 1
	return;

def update():
	global draw
	T.configure(state='normal')
	T.delete('1.0', END)
	drawz = getArray(draw)
	drawz = str(drawz)[1:-1]
	T.insert(INSERT, drawz)
	T.configure(state='disabled')
	w.delete("all")
	getDraw()

def clear():
	global phase, draw
	w.delete("all")
	T.configure(state='normal')
	T.delete('1.0', END)
	T.configure(state='disabled')
	draw = []
	phase = 1
	print("clear'd")

def play(z):
	update()
	global draw
	drawing = draw
	pos = pyautogui.position()
	xx = pos[0]
	yy = pos[1]

	c = 0
	i = len(drawing)
	pyautogui.moveTo(xx+drawing[c][0],yy+drawing[c][1])
	pyautogui.mouseDown(button='left')
	while (c<i):
		if(drawing[c] == 5000):
			pyautogui.mouseUp(button='left')
			c += 1
		else:
			pyautogui.moveTo(xx+drawing[c][0],yy+drawing[c][1])
			pyautogui.mouseDown(button='left')
			c += 1
	pyautogui.mouseUp(button='left')
	return;

def toggle():
	global togglevar
	if (togglevar == 0):
		T.configure(state='normal')
		togglevar = 1
		T.tag_add("sel","1.0","end")
	else:
		T.configure(state='disabled')
		togglevar = 0

def alphaChange(alph):
	master.wm_attributes('-alpha',int(alph)/100)

def focus_next_window(event):
    event.widget.tk_focusNext().focus()
    return("break")

master = Tk()
master.wait_visibility(master)
master.title('Drawing App')
master.geometry("800x640+100+100")
master.bind('e', callback)
master.bind('q', split)
master.bind('z', play)
w = Canvas(master, bg="White")
w.pack(side=RIGHT, fill=BOTH, expand=True)
okButton = Button(master, text="Record", command=callback)
okButton.pack(expand=False, fill=X)
splitButton = Button(master, text="Split", command=split)
splitButton.pack(expand=False, fill=X)
enterButton = Button(master, text="Enter drawing", command=getDraw)
enterButton.pack(expand=False, fill=X)
updateButton = Button(master, text="Update", command=update)
updateButton.pack(expand=False, fill=X)
clearButton = Button(master, text="Clear", command=clear)
clearButton.pack(expand=False, fill=X)
toggleButton = Button(master, text="Textbox on/off", command=toggle)
toggleButton.pack(expand=False, fill=X)
alphaScale = Scale(master, from_=10, to=100, orient=HORIZONTAL, command=alphaChange, showvalue=0)
alphaScale.pack(expand=False, fill=X)
alphaScale.set(100)
yscrollbar = Scrollbar(master)
yscrollbar.pack(side=RIGHT, fill=Y)
T = Text(master, width=30, height=10, state='normal', font=("Source Code Pro", 8), yscrollcommand=yscrollbar.set)
T.bind("<Tab>", focus_next_window)
T.pack(expand=True, fill=Y)
yscrollbar.config( command = T.yview )

mainloop()
