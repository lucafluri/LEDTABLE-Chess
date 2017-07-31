#!/usr/bin/env python
#coding: utf8
import time
import array
import fcntl
import random
import sys
import os
import select
from imgdisp import imgdisp

# Open SPI device
spidev = file("/dev/spidev0.0", "wb")
#byte array to store rgb values
rgb=bytearray(3)
#setting spi frequency to 400kbps
fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))

#creating 10x10 matrix
matrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
cmatrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]


#Define Functions for Allocation and Display
def allocate():
	#gleich wie bei imgdisp.py, wird einfach noch gespiegelt
	#damit punkt 0/0 am linken oberen rand ist

	for x in range(0,10):
		for y in range (0,10):
			cmatrix[x][y][0] = matrix[x][y][0]
			cmatrix[x][y][1] = matrix[x][y][1]
			cmatrix[x][y][2] = matrix[x][y][2]

			#Column 1
			col = 1
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1]
				cmatrix[x][y][2] = matrix[col][9][2]
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]

				#Column 3
			col = 3
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1]
				cmatrix[x][y][2] = matrix[col][9][2]
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]

				#Column 5
			col = 5
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1]
				cmatrix[x][y][2] = matrix[col][9][2]
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]

			#Column 7
			col = 7
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1]
				cmatrix[x][y][2] = matrix[col][9][2]
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]

				#Column 9
			col = 9
			if x == col and y == 0:
				cmatrix[x][y][0] = matrix[col][9][0]
				cmatrix[x][y][1] = matrix[col][9][1]
				cmatrix[x][y][2] = matrix[col][9][2]
			elif x == col and y == 1:
				cmatrix[x][y][0] = matrix[col][8][0]
				cmatrix[x][y][1] = matrix[col][8][1]
				cmatrix[x][y][2] = matrix[col][8][2]
			elif x == col and y == 2:
				cmatrix[x][y][0] = matrix[col][7][0]
				cmatrix[x][y][1] = matrix[col][7][1]
				cmatrix[x][y][2] = matrix[col][7][2]
			elif x == col and y == 3:
				cmatrix[x][y][0] = matrix[col][6][0]
				cmatrix[x][y][1] = matrix[col][6][1]
				cmatrix[x][y][2] = matrix[col][6][2]
			elif x == col and y == 4:
				cmatrix[x][y][0] = matrix[col][5][0]
				cmatrix[x][y][1] = matrix[col][5][1]
				cmatrix[x][y][2] = matrix[col][5][2]
			elif x == col and y == 5:
				cmatrix[x][y][0] = matrix[col][4][0]
				cmatrix[x][y][1] = matrix[col][4][1]
				cmatrix[x][y][2] = matrix[col][4][2]
			elif x == col and y == 6:
				cmatrix[x][y][0] = matrix[col][3][0]
				cmatrix[x][y][1] = matrix[col][3][1]
				cmatrix[x][y][2] = matrix[col][3][2]
			elif x == col and y == 7:
				cmatrix[x][y][0] = matrix[col][2][0]
				cmatrix[x][y][1] = matrix[col][2][1]
				cmatrix[x][y][2] = matrix[col][2][2]
			elif x == col and y == 8:
				cmatrix[x][y][0] = matrix[col][1][0]
				cmatrix[x][y][1] = matrix[col][1][1]
				cmatrix[x][y][2] = matrix[col][1][2]
			elif x == col and y == 9:
				cmatrix[x][y][0] = matrix[col][0][0]
				cmatrix[x][y][1] = matrix[col][0][1]
				cmatrix[x][y][2] = matrix[col][0][2]

	cmatrix.reverse()

def display():
	#allocating
	allocate()
	for x in range(0, 10):
		for y in range(0, 10):
			rgb[0] = cmatrix[x][y][0]
			rgb[1] = cmatrix[x][y][1]
			rgb[2] = cmatrix[x][y][2]
			spidev.write(rgb)

	spidev.flush()

def clearMatrix():
	for x in range(0, 10):
		for y in range(0, 10):
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0

def clearBoard():
	for x in range(1, 9):
		for y in range(1, 9):
			matrix[x][y][0] = 0
			matrix[x][y][1] = 0
			matrix[x][y][2] = 0

def setColor(x, y, rgb):
	matrix[x][y][0] = rgb[0]
	matrix[x][y][1] = rgb[1]
	matrix[x][y][2] = rgb[2]


class game:
	turn = True #t = white, f = black
	border = [0,0,5]

	def turnInd(self):
		ind = [10, 10, 10]
		if self.turn: #white
			setColor(9, 9, ind)
		else: #black
			setColor(9, 0, ind)

	def switch(self):
		self.turn = not self.turn
		self.turnInd()

	def paintPiece(self, piece):
		setColor(piece[0], piece[1], piece[2])

	def paintBorder(self):
		for x in range(0, 10):
			setColor(x, 0, self.border)
		for y in range(1, 10):
			setColor(9, y, self.border)
		for x in range(9, -1, -1):
			setColor(x, 9, self.border)
		for y in range(9, 0, -1):
			setColor(0, y, self.border)

	def update(self):
		clearMatrix()
		self.paintBorder()

		self.paintPiece(white.P1)
		self.paintPiece(white.P2)
		self.paintPiece(white.P3)
		self.paintPiece(white.P4)
		self.paintPiece(white.P5)
		self.paintPiece(white.P6)
		self.paintPiece(white.P7)
		self.paintPiece(white.P8)
		self.paintPiece(white.R1)
		self.paintPiece(white.R2)
		self.paintPiece(white.N1)
		self.paintPiece(white.N2)
		self.paintPiece(white.B1)
		self.paintPiece(white.B2)
		self.paintPiece(white.Q)
		self.paintPiece(white.K)

		self.paintPiece(black.P1)
		self.paintPiece(black.P2)
		self.paintPiece(black.P3)
		self.paintPiece(black.P4)
		self.paintPiece(black.P5)
		self.paintPiece(black.P6)
		self.paintPiece(black.P7)
		self.paintPiece(black.P8)
		self.paintPiece(black.R1)
		self.paintPiece(black.R2)
		self.paintPiece(black.N1)
		self.paintPiece(black.N2)
		self.paintPiece(black.B1)
		self.paintPiece(black.B2)
		self.paintPiece(black.Q)
		self.paintPiece(black.K)

		self.switch()

		display()

class white:
	#colors
	PC = [30, 30, 255]
	RC = [100, 25, 255]
	NC = [0, 255, 100]
	BC = [255, 255, 60]
	QC = [255, 100, 255]
	KC = [255, 25, 25]

	#Pieces
	P1 = [1, 7, PC]
	P2 = [2, 7, PC]
	P3 = [3, 7, PC]
	P4 = [4, 7, PC]
	P5 = [5, 7, PC]
	P6 = [6, 7, PC]
	P7 = [7, 7, PC]
	P8 = [8, 7, PC]
	R1 = [1, 8, RC]
	R2 = [8, 8, RC]
	N1 = [2, 8, NC]
	N2 = [7, 8, NC]
	B1 = [3, 8, BC]
	B2 = [6, 8, BC]
	Q = [4, 8, QC]
	K = [5, 8, KC]

class black:
	#colors
	PC = [0, 0, 255]
	RC = [50, 0, 255]
	NC = [0, 255, 0]
	BC = [255, 255, 0]
	QC = [255, 0, 255]
	KC = [255, 0, 0]

	#Pieces
	P1 = [1, 2, PC]
	P2 = [2, 2, PC]
	P3 = [3, 2, PC]
	P4 = [4, 2, PC]
	P5 = [5, 2, PC]
	P6 = [6, 2, PC]
	P7 = [7, 2, PC]
	P8 = [8, 2, PC]
	R1 = [1, 1, RC]
	R2 = [8, 1, RC]
	N1 = [2, 1, NC]
	N2 = [7, 1, NC]
	B1 = [3, 1, BC]
	B2 = [6, 1, BC]
	Q = [4, 1, QC]
	K = [5, 1, KC]


def startupAnimation():
	clearMatrix()
	#Border init
	border = game.border
	whiteN = [255, 255, 255]
	whiteB = [1, 1, 1]
	for x in range(0, 10):
		setColor(x, 0, border)
		display()
		time.sleep(0.041)
	for y in range(1, 10):
		setColor(9, y, border)
		display()
		time.sleep(0.041)
	for x in range(9, -1, -1):
		setColor(x, 9, border)
		display()
		time.sleep(0.041)
	for y in range(9, 0, -1):
		setColor(0, y, border)
		display()
		time.sleep(0.041)

	#Checkerboard pattern
	for y in range(1, 9, 2):
		for x in range(1, 9, 2):
			setColor(x, y, whiteN)
			time.sleep(0.041)
			display()
	for y in range(2, 9, 2):
		for x in range(2, 9, 2):
			setColor(x, y, whiteN)
			time.sleep(0.041)
			display()

	time.sleep(0.5)
	clearBoard()
	display()

def init():
	#Pieces
	for x in range(1, 9):
		setColor(x, 7, white.PC) #wP
	setColor(1, 8, white.RC)	#wR
	setColor(8, 8, white.RC)
	setColor(2, 8, white.NC)	#wN
	setColor(7, 8, white.NC)
	setColor(3, 8, white.BC)	#wB
	setColor(6, 8, white.BC)
	setColor(4, 8, white.QC)	#wQ
	setColor(5, 8, white.KC)		#wK

	for x in range(1, 9):
		setColor(x, 2, black.PC)	#bP
	setColor(1, 1, black.RC)	#bR
	setColor(8, 1, black.RC)
	setColor(2, 1, black.NC)	#bN
	setColor(7, 1, black.NC)
	setColor(3, 1, black.BC) #bB
	setColor(6, 1, black.BC)
	setColor(4, 1, black.QC)	#bQ
	setColor(5, 1, black.KC)	#bK

	#Border
	for x in range(0, 10):
		setColor(x, 0, game.border)
	for y in range(1, 10):
		setColor(9, y, game.border)
	for x in range(9, -1, -1):
		setColor(x, 9, game.border)
	for y in range(9, 0, -1):
		setColor(0, y, game.border)

	game.turnInd()
	display()



#MAIN
game = game()
white = white()
black = black()

startupAnimation()
init()


#test manual game
def n():
	game.update()
	time.sleep(1)

time.sleep(1)
white.P5[1] = 5
n()
black.P5[1] = 4
n()
white.N2[0] -= 1
white.N2[1] -= 2
n()
