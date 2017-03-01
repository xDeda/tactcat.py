#!/usr/bin/env python

import autopy3
import math
import time
import sys

pos = autopy3.mouse.get_pos()
xx = pos[0]
yy = pos[1]
xx1 = pos[0]
yy1 = pos[1]

# = [,] , [,] , [,] , [,] , [,] , [,] , [,] , [,] , [,] , [,] , [,]
A = [3,22] , [10,0] , [18,22] , [15,14] , [4,14]
B = [3,1] , [11,1] , [16,5] , [12,10] , [3,11] , [12,10] , [17,16] , [10,22] , [3, 22] , [3,1]
C = [17,4] , [10,0] , [4,4] , [1,12] , [4,19] , [10,22] , [17,18]
D = [3,0] , [11,1] , [15,4] , [17,11] , [16,18] , [13,21] , [6,23] , [3,23] , [3,0]
E = [3,0] , [16,0] , [3,0] , [3,10] , [14,10] , [3,10] , [3,22] , [16,22]
F = [3,0] , [15,0] , [3,0] , [3,10] , [14,10] , [3,10] , [3,22]
G = [16,3] , [9,0] , [3,3] , [1,10] , [4,20] , [10,22] , [16,20] , [16,11] , [10,11]
H = [3,0] , [3,22] , [3,10] , [15,10] , [15,0] , [15,22]
I = [3,0] , [15,0] , [9,0] , [9,22] , [3,22] , [15,22]
J = [4,0] , [15,0] , [15,18] , [12,21] , [8,23] , [5,22] , [3,19]
K = [3,0] , [3,22] , [3,13] , [15,0] , [7,8] , [16,22]
L = [3,0] , [3,22] , [15,22]
M = [3,22] , [3,0] , [10,15] , [16,0] , [16,22]
N = [3,22] , [3,0] , [16,22] , [16,0]
O = [11,0] , [17,3] , [19,11] , [17,20] , [11,23] , [5,20] , [3,11] , [5,3] , [11,0]
P = [3,22] , [3,0] , [13,0] , [15,2] , [17,6] , [13,13] , [3,13]
Q = [9,22] , [6,19] , [3,11] , [5,3] , [10,0] , [15,3] , [18,10] , [15,19] , [9,22] , [13,25], [18,27]
R = [3,22] , [3,0] , [13,0] , [17,6] , [15,10] , [6,11] , [11,11] , [16,22] , [18,22]
S = [16,3] , [10,0] , [5,2] , [3,5] , [5,9] , [12,12] , [17,16] , [15,20] , [10,23] , [5,22] , [2,19]
T = [3,0] , [20,0] , [12,0] , [12,22]
U = [3,0] , [3,17] , [5,20] , [9,22] , [12,20] , [15,17] , [15,0]
V = [3,0] , [10,22] , [18,0]
W = [3,0] , [7,22] , [11,6] , [15,22] , [19,0]
X = [3,0] , [15,22] , [9,11] , [3,22] , [15,0]
Y = [3,0] , [10,13] , [10,22] , [10,13] , [17,0]
Z = [3,0] , [16,0] , [3,22] , [16,22]
one = [5,4] , [11,2] , [11,23] , [4,23] , [17,23]
two = [3,5] , [5,3] , [9,2] , [12,3] , [14,5] , [15,8] , [14,12] , [3,23] , [16,23]
three = [5,6] , [7,4] , [10,3] , [12,4] , [16,8] , [14,11] , [7,13] , [15,15] , [17,19] , [14,22] , [10,23] , [7,22] , [5,21] , [3,20]
four = [13,23] , [13,2] , [2,16] , [17,16]
five = [15,2] , [4,2] , [4,12] , [7,11] , [10,10] , [14,11] , [16,15] , [16,18] , [14,21] , [9,23] , [5,22] , [3,20]
six = [16,4] , [15,3] , [11,2] , [8,3] , [5,6] , [3,10] , [3,17] , [6,21] , [10,23] , [14,22] , [16,20] , [17,17] , [16,13] , [11,11] , [7,12] , [5,14] , [3,17]
seven = [3,2] , [17,2] , [13,7] , [10,12] , [9,17] , [8,23]
eight = [10,2] , [13,3] , [16,7] , [12,12] , [7,13] , [4,14] , [3,18] , [4,21] , [10,23] , [14,22] , [16,20] , [17,17] , [15,14] , [11,12] , [6,11] , [4,7] , [5,4] , [10,2]
nine = [15,10] , [12,13] , [9,14] , [5,13] , [3,8] , [4,4] , [9,2] , [12,3] , [15,5] , [16,11] , [16,17] , [14,20] , [11,22] , [8,23] , [4,21]
dot = [9,18] , [11,20] , [9,22] , [7,20] , [9,18]
comma = [10,21] , [11,21] , [12,24] , [10,27] , [7,29]
apostrophe = [11,0] , [10,9]
exclamation = [10,1] , [10,14]
exclamation2 = [10,19] , [11,21] , [9,22] , [8,20] , [10,19]
question = [5,3] , [8,1] , [11,1] , [13,2] , [15,4] , [15,7] , [12,9] , [9,12] , [9,14]
question2 = [9,19] , [11,21] , [9,22] , [8,21] , [9,19]
quotation = [7,1] , [6,11]
quotation2 = [15,1] , [14,11]

def writeLetter(letter):
	global xx, yy
	if (letter == " "):
		if (xx >= 1100):
			xx = xx1-20
			yy = yy+30
		xx = xx+20
	else:
		n = 1
		i = len(letter)
		autopy3.mouse.move(xx+letter[0][0],yy+letter[0][1])
		wait()
		autopy3.mouse.toggle(True)
		wait()
		while (n<i):
			autopy3.mouse.move(xx+letter[n][0],yy+letter[n][1])
			n = n+1
			wait()
		autopy3.mouse.toggle(False)
		if (letter != question):
			if (letter != exclamation):
				if (letter != quotation):
					xx = xx+20
		wait()
	return;

def writeExclamation():
	writeLetter(exclamation)
	writeLetter(exclamation2)
	return;

def writeQuestion():
	writeLetter(question)
	writeLetter(question2)
	return;

def writeQuotation():
	writeLetter(quotation)
	writeLetter(quotation2)
	return;

def wait():
	time.sleep(0.05)
	return;

def writeOut(str):
	global xx, yy
	n = 0
	str = list(str)
	i = len(str)
	while (n<i):
		if (str[n] == "A"):
			writeLetter(A)
		elif (str[n] == "B"):
			writeLetter(B)
		elif (str[n] == "C"):
			writeLetter(C)
		elif (str[n] == "D"):
			writeLetter(D)
		elif (str[n] == "E"):
			writeLetter(E)
		elif (str[n] == "F"):
			writeLetter(F)
		elif (str[n] == "G"):
			writeLetter(G)
		elif (str[n] == "H"):
			writeLetter(H)
		elif (str[n] == "I"):
			writeLetter(I)
		elif (str[n] == "J"):
			writeLetter(J)
		elif (str[n] == "K"):
			writeLetter(K)
		elif (str[n] == "L"):
			writeLetter(L)
		elif (str[n] == "M"):
			writeLetter(M)
		elif (str[n] == "N"):
			writeLetter(N)
		elif (str[n] == "O"):
			writeLetter(O)
		elif (str[n] == "P"):
			writeLetter(P)
		elif (str[n] == "Q"):
			writeLetter(Q)
		elif (str[n] == "R"):
			writeLetter(R)
		elif (str[n] == "S"):
			writeLetter(S)
		elif (str[n] == "T"):
			writeLetter(T)
		elif (str[n] == "U"):
			writeLetter(U)
		elif (str[n] == "V"):
			writeLetter(V)
		elif (str[n] == "W"):
			writeLetter(W)
		elif (str[n] == "X"):
			writeLetter(X)
		elif (str[n] == "Y"):
			writeLetter(Y)
		elif (str[n] == "Z"):
			writeLetter(Z)
		elif (str[n] == " "):
			writeLetter(" ")
		elif (str[n] == "1"):
			writeLetter(one)
		elif (str[n] == "2"):
			writeLetter(two)
		elif (str[n] == "3"):
			writeLetter(three)
		elif (str[n] == "4"):
			writeLetter(four)
		elif (str[n] == "5"):
			writeLetter(five)
		elif (str[n] == "6"):
			writeLetter(six)
		elif (str[n] == "7"):
			writeLetter(seven)
		elif (str[n] == "8"):
			writeLetter(eight)
		elif (str[n] == "9"):
			writeLetter(nine)
		elif (str[n] == "."):
			writeLetter(dot)
		elif (str[n] == ","):
			writeLetter(comma)
		elif (str[n] == "!"):
			writeExclamation()
		elif (str[n] == "?"):
			writeQuestion()
		elif (str[n] == "\""):
			writeQuotation()
		elif (str[n] == "'"):
			writeLetter(apostrophe)
		n = n+1
	return;

draw = sys.argv[1].upper()

writeOut(draw)

autopy3.mouse.move(xx1,yy+30)
