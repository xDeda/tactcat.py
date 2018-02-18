#!/usr/bin/env python

from tkinter import *

from Xlib import display
import time
import math
import numpy as np
import autopy3
import sys, argparse

phase = 1

draw = ["drawing"]
draw[0] = []
current_color = 'black'
fromx = 0
fromy = 0
tox = 0
toy = 0
togglevar = 0
n = 0

# Parse user arguments
parser = argparse.ArgumentParser(description='Interpreter of graphics')
parser.add_argument('--width', '-w', metavar='width', type=int, nargs=1,
                    help='Width of the scene', default = 1720)
parser.add_argument('--height', '-y', metavar='height', type=int,
                    nargs=1, help='Height of the scene', default = 1080)
parser.add_argument('--bg-color', '-b', metavar='bgcolor',
                    nargs=1, help='Background color', default = 'white')

args = parser.parse_args()

def mousepos():
    # mousepos() --> (x, y) get the mouse coordinates on the screen (linux, Xlib).
    data = display.Display().screen().root.query_pointer()._data
    return data["root_x"], data["root_y"]

def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)

master = Tk()
master.wait_visibility(master)
master.wm_attributes('-alpha',0.75)
master.title('pen')
master.geometry("1915x1080+0+0")
w = Canvas(master, width=args.width, height=args.height, bg=args.bg_color)
w.pack(side=RIGHT, fill=BOTH, expand=True)

def callback(e):
    global fromx, fromy, tox, toy, phase
    if (phase == 0):
        tox = mousepos()[0]
        toy = mousepos()[1]
        w.create_line(fromx-198,fromy-44,tox-198,toy-44, fill=current_color)
        fromx = mousepos()[0]
        fromy = mousepos()[1]
        draw[0].append([fromx,fromy])
        print("(phase 0)",fromx,",",fromy)
    else:
        fromx = mousepos()[0]
        fromy = mousepos()[1]
        draw[0].append([fromx,fromy])
        print("(1 phase)",fromx,",",fromy)
        phase = 0

def split(q):
    global fromx, fromy, draw
    draw[0].append(5000)
    fromx = mousepos()[0]
    fromy = mousepos()[1]
    draw[0].append([fromx,fromy])
    print("5000")

def toggleOn():
    global togglevar
    if (togglevar == 0):
        T.configure(state='normal')
        togglevar = 1
        T.tag_add("sel","1.0","end")
    else:
        T.configure(state='disabled')
        togglevar = 0

def play(q):
    def wait():
        time.sleep(0.1)
        return;
    
    def playThis():
        c = 0
        drawing = draw[n]
        i = len(drawing)
        drawing = draw[n]
        autopy3.mouse.move(drawing[c][0],drawing[c][1])
        autopy3.mouse.toggle(True)
        while (c<i):
            if(drawing[c] == 5000):
                autopy3.mouse.toggle(False)
                c += 1
                wait()
            else:
                autopy3.mouse.move(drawing[c][0],drawing[c][1])
                autopy3.mouse.toggle(True)
                c += 1
                wait()
        autopy3.mouse.toggle(False)
        return;
    playThis()

def getDraw():
    print(T.get('1.0', END))
    draw[0] = eval(T.get('1.0', END))
    w.delete("all") 
    c = 0
    drawing = draw[n]
    i = len(drawing)
    drawing = draw[n]
    w.create_line(drawing[c][0]-198,drawing[c][1]-44,drawing[c+1][0]-198,drawing[c+1][1]-44, fill=current_color)
    while (c<i):
        if(drawing[c] == 5000 or drawing[c+1] == 5000):
            c += 1
        else:
            w.create_line(drawing[c][0]-198,drawing[c][1]-44,drawing[c+1][0]-198,drawing[c+1][1]-44, fill=current_color)
            c += 1
    return;

okButton = Button(master, text="Record", command=callback)
okButton.pack(expand=False, fill=X)
splitButton = Button(master, text="Split", command=split)
splitButton.pack(expand=False, fill=X)
enterButton = Button(master, text="Enter drawing", command=getDraw)
enterButton.pack(expand=False, fill=X)
enableButton = Button(master, text="Textbox on/off", command=toggleOn)
enableButton.pack(expand=False, fill=X)
T = Text(master, width=30, height=50, state='disabled')
T.pack(expand=False, fill=BOTH)
master.bind('e', callback)
master.bind('q', split)
master.bind('z', play)

def update():
    T.configure(state='normal')
    T.delete('1.0', END)
    dring = str(draw[0])
    T.insert(INSERT, dring)
    T.configure(state='disabled')

def clanvas():
    global phase
    w.delete("all")
    draw[0] = []
    phase = 1
    print("clear'd")
    update()

def alphaChange(alph):
    master.wm_attributes('-alpha',int(alph)/100)

def quit():
    raise SystemExit

quitButton = Button(master,text="Quit", command=quit)
quitButton.pack(expand=False, fill=X)
clearButton = Button(master, text="Clear", command=clanvas)
clearButton.pack(expand=False, fill=X)
alphaScale = Scale(master, from_=0, to=100, orient=HORIZONTAL, command=alphaChange, showvalue=0, label="alpha")
alphaScale.pack(expand=False, fill=X)
alphaScale.set(75)
updateButton = Button(master, text="Update", command=update)
updateButton.pack(expand=False, fill=X)

# Main method
def readin():
    while True:
        try:
            readcommand()
        except KeyboardInterrupt:
            eprint("Keyboard Interrupt. Exiting.")
            sys.exit()
        except EOFError:
            eprint("EOF error. Exiting.")
            sys.exit()

def readcommand():
    global current_color
    command = input()
    words = command.split()
    # Drawing commands
    if len(words) >= 1:
        if words[0] == 'rectangle':
            fromx = float(words[1])
            fromy = float(words[2])
            tox = float(words[3])
            toy = float(words[4])
            w.create_rectangle(fromx, fromy, tox, toy, fill=current_color, outline=current_color)
        elif words[0] == 'point':
            x = float(words[1])
            y = float(words[2])
            w.create_rectangle(x, y, x+1, y+1, outline=current_color)
        elif words[0] == 'line':
            fromx = float(words[1])
            fromy = float(words[2])
            tox = float(words[3])
            toy = float(words[4])
            w.create_line(fromx,fromy,tox,toy, fill=current_color)
        elif words[0] == 'changesize':
            width = float(words[1])
            height = float(words[2])
            w.config(width=width, height=height)
        elif words[0] == 'changebg':
            w.config(bg=words[1])
        elif words[0] == 'changecolor':
            current_color = words[1]
        elif words[0] == 'txt':
            if len(words) > 3:
                x = float(words[1])
                y = float(words[2])
                w.create_text(x, y,fill = current_color,anchor=NW ,text=words[3:])
                # Canvas commands
        elif words[0] == 'clear':
            w.delete(ALL)
        elif words[0] == 'update':
            master.update()
        elif words[0] == 'quit':
            sys.exit()
        else:
            eprint('Command', command, 'not recognized')
    else:
        eprint('Error. Empty command')

update()

# Begin program
master.after(1000,readin)
mainloop()
