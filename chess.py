#!/usr/bin/env python
#coding: utf8
import time
import array
import fcntl
import random
import sys
import os
import select
import numpy
import math
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
	fmatrix = numpy.fliplr(cmatrix)
	for x in range(0, 10):
		for y in range(0, 10):
			rgb[0] = fmatrix[x][y][0]
			rgb[1] = fmatrix[x][y][1]
			rgb[2] = fmatrix[x][y][2]
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

def CtoN(x, y): #convert Coordinated to Chess Notation
	y = str(y)
	if x==1:
		return "a" + y
	if x==2:
		return "b" + y
	if x==3:
		return "c" + y
	if x==4:
		return "d" + y
	if x==5:
		return "e" + y
	if x==6:
		return "f" + y
	if x==7:
		return "g" + y
	if x==8:
		return "h" + y

def NtoC(N):	#convert string to tuple
	x = N[0]
	y = int(N[1])
	if x=="a":
		return (1, y)
	if x=="b":
		return (2, y)
	if x=="c":
		return (3, y)
	if x=="d":
		return (4, y)
	if x=="e":
		return (5, y)
	if x=="f":
		return (6, y)
	if x=="g":
		return (7, y)
	if x=="h":
		return (8, y)

def xToN(x):
	if x==1:
		return "a"
	if x==2:
		return "b"
	if x==3:
		return "c"
	if x==4:
		return "d"
	if x==5:
		return "e"
	if x==6:
		return "f"
	if x==7:
		return "g"
	if x==8:
		return "h"








class game:
	turn = False #t = white, f = black
	border = [0,0,5]
	pieces = []
	moves = []
	cmove = 1
	finished = False

	def __init__(self):
		clearMatrix()
		self.paintBorder()

		wP1 = wP(1, 2)
		self.paintPiece(wP1)
		wP2 = wP(2, 2)
		self.paintPiece(wP2)
		wP3 = wP(3, 2)
		self.paintPiece(wP3)
		wP4 = wP(4, 2)
		self.paintPiece(wP4)
		wP5 = wP(5, 2)
		self.paintPiece(wP5)
		wP6 = wP(6, 2)
		self.paintPiece(wP6)
		wP7 = wP(7, 2)
		self.paintPiece(wP7)
		wP8 = wP(8, 2)
		self.paintPiece(wP8)
		wR1 = wR(1, 1)
		self.paintPiece(wR1)
		wR2 = wR(8, 1)
		self.paintPiece(wR2)
		wN1 = wN(2, 1)
		self.paintPiece(wN1)
		wN2 = wN(7, 1)
		self.paintPiece(wN2)
		wB1 = wB(3, 1)
		self.paintPiece(wB1)
		wB2 = wB(6, 1)
		self.paintPiece(wB2)
		wQ1 = wQ(4, 1)
		self.paintPiece(wQ1)
		wK1 = wK(5, 1)
		self.paintPiece(wK1)

		bP1 = bP(1, 7)
		self.paintPiece(bP1)
		bP2 = bP(2, 7)
		self.paintPiece(bP2)
		bP3 = bP(3, 7)
		self.paintPiece(bP3)
		bP4 = bP(4, 7)
		self.paintPiece(bP4)
		bP5 = bP(5, 7)
		self.paintPiece(bP5)
		bP6 = bP(6, 7)
		self.paintPiece(bP6)
		bP7 = bP(7, 7)
		self.paintPiece(bP7)
		bP8 = bP(8, 7)
		self.paintPiece(bP8)
		bR1 = bR(1, 8)
		self.paintPiece(bR1)
		bR2 = bR(8, 8)
		self.paintPiece(bR2)
		bN1 = bN(2, 8)
		self.paintPiece(bN1)
		bN2 = bN(7, 8)
		self.paintPiece(bN2)
		bB1 = bB(3, 8)
		self.paintPiece(bB1)
		bB2 = bB(6, 8)
		self.paintPiece(bB2)
		bQ1 = bQ(4, 8)
		self.paintPiece(bQ1)
		bK1 = bK(5, 8)
		self.paintPiece(bK1)

		self.switch()
		display()
		print("Moves:")



	def turnInd(self):
		ind = [10, 10, 10]
		if self.turn: #white
			setColor(9, 0, ind)
		else: #black
			setColor(9, 9, ind)

	def switch(self):
		self.turn = not self.turn
		self.turnInd()

	def paintPiece(self, piece):
		setColor(piece.x, piece.y, piece.color)

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

		for piece in self.pieces:
			self.paintPiece(piece)

		if self.turn:
			sys.stdout.write(str(self.cmove) + ". " + str(self.moves[-1]) + " ")
			sys.stdout.flush()
		else:
			sys.stdout.write(str(self.moves[-1]) + "\n")
			sys.stdout.flush()
			self.cmove += 1

		if not self.finished:
			self.switch()
		else:
			del(self) #game instance is deleted
		display()

	def refreshBoard(self):
		clearMatrix()
		self.paintBorder()
		self.turnInd()
		for piece in self.pieces:
			self.paintPiece(piece)



	def freeSquare(self, x, y):
		if self.getPiece(x, y):
			return False #Square occupied
		else:
			return True #Square free!

	def getPiece(self, x, y):
		for piece in self.pieces:
			if piece.x == x and piece.y == y:
				return piece
			else:
				pass

	def getPieceN(self, N):
		x, y = NtoC(N)
		for piece in self.pieces:
			if piece.x == x and piece.y == y:
				return piece
			else:
				pass

	def checkEnemyPiece(self, x, y):
		if not self.freeSquare(x, y):
			if self.turn and self.getPiece(x, y).side=="black":
				return True
			if not self.turn and self.getPiece(x, y).side=="white":
				return True
			else:
				return False
		else:
			return False

	def checkEnPassant(self, x, y):
		pass

	def sameLane(self, x, y, x0, y0):
		#same Column
		if x0==x or y0==y:
			return True
		else:
			return False

	def sameDiagonal(self, x, y, x0, y0):
		if x-x0==y-y0 or x-x0==y0-y:
			return True
		else:
			return False


	def checkRoute(self, x, y, x0, y0):
		#check if direct route to destination is unblocked
		if math.fabs(x-x0)==1 or math.fabs(y-y0)==1: #only 1 move
			return True
		#same Column
		if x0==x:
			if y<y0:
				for i in range(y0-1, y, -1):
					if not self.freeSquare(x, i):
						return False #Blocked Route
					else:
						return True	#Free Route

			if y>y0:
				for i in range(y0+1, y, +1):
					if not self.freeSquare(x, i):
						return False
					else:
						return True

		#same row
		if y0==y:
			if x<x0:
				for i in range(x0-1, x, -1):
					if not self.freeSquare(i, y):
						return False
					else:
						return True
			if x>x0:
				for i in range(x0+1, x, +1):
					if not self.freeSquare(i, y):
						return False
					else:
						return True

		#same diagonal
		#positive diagonal
		if x-x0==y-y0:
			if x<x0:
				for i in range(x0-1, x, -1):
					for v in range(y0-1, y, -1):
						if not self.freeSquare(i, v):
							return False
						else:
							return True
			if x>x0:
				for i in range(x0+1, x, +1):
					for v in range(y0+1, y, +1):
						if not self.freeSquare(i, v):
							return False
						else:
							return True
		#negative diagonal
		if x-x0==y0-y:
			if x-x0>0:
				for i in range(x0+1, x, +1):
					for v in range(y0-1, y, -1):
						if not self.freeSquare(i, v):
							return False
						else:
							return True
			if y-y0>0:
				for i in range(x0-1, x, -1):
					for v in range(y0+1, y, +1):
						if not self.freeSquare(i, v):
							return False
						else:
							return True



	def blinkPiece(self, piece):
		color = piece.color
		try:
			for i in range(0, 3):
				piece.color = [0,0,0]
				self.paintPiece(piece)
				display()
				time.sleep(0.1)
				piece.color = color
				self.paintPiece(piece)
				display()
				time.sleep(0.1)
		except:
			print "For loop error"




	def checkOppCheck(self):
		if self.turn:
			side = "white"
			opp = "black"
		else:
			side = "black"
			opp = "white"

		#Find opponent king
		for piece in self.pieces:
			if piece.name == "K" and piece.side==opp:
				oppK = piece

		#Find Piece that checked the enemy king
		for piece in self.pieces:
			if piece.side == side:
				if piece.checkMove(oppK.x, oppK.y):
					oppK.check = True
					return True, oppK
				else:
					pass
			else:
				pass
		oppK.check = False
		return False, oppK

	def checkOwnCheck(self, side):
		if side=="white":
			opp = "black"
		if side=="black":
			opp = "white"

		#Find opponent king
		for piece in self.pieces:
			if piece.name == "K" and piece.side==side:
				ownK = piece

		#Find Piece that checked the own king
		for piece in self.pieces:
			if piece.side == opp:
				if piece.checkMove(ownK.x, ownK.y):
					ownK.check = True
					return ownK
				else:
					pass
			else:
				pass

		#ownK.check = False
		return ownK



	def checkMate(self, king):

		for piece in self.pieces:
			if piece.side==king.side:
				for i in range(1, 9):
					for v in range(1, 9):
						if piece.checkMove(i, v):
							if not self.checkFutureOwnCheck(piece, i, v):#King will still be in check
								pass
							else:
								self.finished=True
								self.border = [255, 0, 0]
								self.refreshBoard()
								return True
						else:
							pass
			else:
				pass

		return False



	#Can only be called after checkMove()
	def checkFutureOwnCheck(self, piece, x, y):
		x0, y0 = piece.x, piece.y #save init coord.
		#switch
		piece.x, piece.y = x, y
		king = self.checkOwnCheck(piece.side)
		if king.check:
			#returns False if own King will be in check
			piece.x, piece.y = x0, y0 #fix
			king.check = not king.check
			return False
		else:
			piece.x, piece.y = x0, y0
			king.check = not king.check
			return True


	def removePiece(self, piece):
		self.pieces.remove(piece)

	def addPiece(self, piece):
		self.pieces.append(piece)


	def move(self, piece, x, y):
		if(x<1 or x>8) or (y<1 or y>8):
			print("Wrong Input")
			return False
		if(self.turn and piece.side=="black") or (not self.turn and piece.side=="white"):
			return False

		pieceD = self.getPiece(x, y)
		x0, y0 = piece.x, piece.y
		#Capture
		if self.checkEnemyPiece(x, y) and piece.checkMove(x, y) and self.checkFutureOwnCheck(piece, x, y):
			self.removePiece(pieceD)
			piece.setPos(x, y)
			#self.cmove += 1
			#print("\n Move " + str(self.cmove) + "\n")
			if piece.name=="P":
				self.moves.append(xToN(x0) + "x" + CtoN(x, y))
			else:
				self.moves.append(piece.name + "x" + CtoN(x, y)) #Check for multiple pieces being able to capture
			#print(self.moves[-1] + "\n")
			check, king = self.checkOppCheck()
			if king.check:
				if self.checkMate(king):
					self.moves[-1] = str(self.moves[-1]) + "#"
					game.refreshBoard()
					self.blinkPiece(king)

				else:
					self.moves[-1] = str(self.moves[-1]) + "+"
					game.refreshBoard()
					self.blinkPiece(king)
			game.update()
			return True
		#Normal Move
		if piece.checkMove(x, y) and self.checkFutureOwnCheck(piece, x, y):
			piece.setPos(x, y)
			#self.cmove += 1
			#print("\n Move " + str(self.cmove) + "\n")
			if piece.name=="P":
				self.moves.append(CtoN(x, y))
			else:
				self.moves.append(piece.name + CtoN(x, y))
			#print("\n")
			check, king = self.checkOppCheck()
			if king.check:
				if self.checkMate(king):
					self.moves[-1] = str(self.moves[-1]) + "#"
					game.refreshBoard()
					self.blinkPiece(king)

				else:
					self.moves[-1] = str(self.moves[-1]) + "+"
					game.refreshBoard()
					self.blinkPiece(king)
			game.update()
			return True
		else:
			if piece.name=="P":
				print("Illegal Move: " + CtoN(x, y))
			else:
				print("Illegal Move: " + piece.name + CtoN(x, y))
			return False

	def moveN(self, piece, N):
		x, y = NtoC(N)
		return self.move(piece, x, y)



class piece:
	name = "piece"
	def __init__(self, x, y):
		game.pieces.append(self)
		self.x = x
		self.y = y
		self.captured = False

	def checkMove(self, x, y):
		pass

	def setPos(self, x, y):
		self.x = x
		self.y = y




class wP(piece):
	name = "P"
	color = [30, 30, 255]
	side = "white"


	def checkMove(self, x, y):
		#Normal move (0, +1)
		#Possible first move (0, +2)
		#Possible Capture (+-1, +1)
		if game.checkRoute(x, y, self.x, self.y):
			if game.freeSquare(x, y):
				if self.y == 2 and (y==self.y+1 or y==self.y+2):
					return True
				if y==self.y+1:
					return True
			if game.checkEnemyPiece(x, y) and ((x==self.x-1 or x==self.x+1) and y==self.y+1): #Capture
				return True
			else:
				return False
		else:
			return False
		#En Passant...

class bP(piece):
	name = "P"
	color = [0, 0, 255]
	side = "black"
	def checkMove(self, x, y):
		#Normal move (0, -1)
		#Possible first move (0, -2)
		#Possible Capture (+-1, -1)
		if game.checkRoute(x, y, self.x, self.y):
			if game.freeSquare(x, y):
				if self.y == 7 and (y==self.y-1 or y==self.y-2):
					return True
				if y==self.y-1:
					return True
			if game.checkEnemyPiece(x, y) and ((x==self.x-1 or x==self.x+1) and y==self.y-1): #Capture
				return True
			else:
				return False
		else:
			return False
		#En Passant


class R(piece):
	name = "R"
	def checkMove(self, x, y):
		#Possible Move (0, +-y)/(+-x, 0)
		if game.sameLane(x, y, self.x, self.y):
			if game.checkRoute(x, y, self.x, self.y):
				if game.freeSquare(x, y):
					return True
				else:
					if game.checkEnemyPiece(x, y):
						return True
					else:
						return False
			else:
				return False
		else:
			return False

class wR(R):
	color = [100, 25, 255]
	side = "white"

class bR(R):
	color = [50, 0, 255]
	side = "black"

class N(piece):
	name = "N"
	def checkMove(self, x, y):
		#Possible Moves (+-1, +-2)/(+-2, +-1)
		#8 Squares max
		if game.freeSquare(x, y) or game.checkEnemyPiece(x, y):
			if (((x==self.x+1 or x==self.x-1) and (y==self.y+2 or y==self.y-2)) or ((x==self.x+2 or x==self.x-2) and (y==self.y+1 or y==self.y-1))):
				return True
			else:
				return False
		else:
			return False


class wN(N):
	color = [0, 255, 100]
	side = "white"
class bN(N):
	color = [0, 255, 0]
	side = "black"

class B(piece):
	name = "B"
	def checkMove(self, x, y):
		#Possible Moves (+-x, 1-y)
		if game.sameDiagonal(x, y, self.x, self.y) and game.checkRoute(x, y, self.x, self.y):
			if game.freeSquare(x, y) or game.checkEnemyPiece(x, y):
				return True
			else:
				False
		else:
			return False

class wB(B):
	color = [255, 255, 60]
	side = "white"
class bB(B):
	color = [255, 255, 0]
	side = "black"

class Q(piece):
	name = "Q"
	def checkMove(self, x, y):
		#Possible diagonal and lane moves
		if (game.sameDiagonal(x, y, self.x, self.y) or game.sameLane(x, y, self.x, self.y)):
			if game.checkRoute(x, y, self.x, self.y):
				if game.freeSquare(x, y):
					return True
				else:
					if game.checkEnemyPiece(x, y):
						return True
					else:
						return False
			else:
				return False
		else:
			return False


class wQ(Q):
	color = [255, 100, 255]
	side = "white"
class bQ(Q):
	color = [255, 0, 255]
	side = "black"

class K(piece):
	name = "K"
	check = False

	def checkMove(self, x, y):
		#+-1 in every direction

		if game.freeSquare(x, y) or game.checkEnemyPiece(x, y):
			if game.sameLane(x, y, self.x, self.y) and (math.fabs(x-self.x)==1 or math.fabs(y-self.y)==1):
				return True
			if game.sameDiagonal(x, y, self.x, self.y) and (math.fabs(x-self.x)==1 and math.fabs(y-self.y)==1):
				return True
			else:
				return False
		else:
			return False

class wK(K):
	color = [255, 25, 25]
	side = "white"
class bK(K):
	color = [255, 0, 0]
	side = "black"


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




#MAIN
#startupAnimation()
game = game()



def m(a, b): #a, b str in Notation
	time.sleep(0.25)
	game.moveN(game.getPieceN(a), b)


m("e2", "e4")
m("e7", "e5")

m("f1", "c4")
m("a7", "a6")

m("d2", "d4")

m("e5", "d4") #capture exd4


m("d1", "d4") #capture Qxd4
#...
m("b8", "c6")


m("d4", "d5")
m("g7", "g5")

m("d5", "f7") #Capture and Checkmate Qxf7##

m("e8", "e7")#test for move verification
