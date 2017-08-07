#!/usr/bin/env python
# coding: utf8
import time
import array
try:
    import fcntl
except:
    pass
import random
import sys
import os
import select
import numpy
import math


rgb = bytearray(3)

try:
    # Open SPI device
    spidev = file("/dev/spidev0.0", "wb")
    # byte array to store rgb values
    # setting spi frequency to 400kbps
    fcntl.ioctl(spidev, 0x40046b04, array.array('L', [400000]))
except:
    pass

# creating 10x10 matrix
matrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
cmatrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]

#@fold-children

# Define Functions for Allocation and Display

# TODO: Move Allocate to seperate file -> import

def allocate():
    # gleich wie bei imgdisp.py, wird einfach noch gespiegelt
    # damit punkt 0/0 am linken oberen rand ist

    for x in range(0, 10):
        for y in range(0, 10):
            cmatrix[x][y][0] = matrix[x][y][0]
            cmatrix[x][y][1] = matrix[x][y][1]
            cmatrix[x][y][2] = matrix[x][y][2]

            # Column 1
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

                # Column 3
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

                # Column 5
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

            # Column 7
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

                # Column 9
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
    # allocating
    allocate()
    fmatrix = numpy.fliplr(cmatrix)
    for x in range(0, 10):
        for y in range(0, 10):
            rgb[0] = fmatrix[x][y][0]
            rgb[1] = fmatrix[x][y][1]
            rgb[2] = fmatrix[x][y][2]
            try:
                spidev.write(rgb)
            except:
                pass


    try:
        spidev.flush()
    except:
        pass

    f = open("save.matrix", "w+")
    f.write(str(fmatrix))


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


def CtoN(x, y):  # convert Coordinated to Chess Notation
    y = str(y)
    try:
        if x == 1:
            return "a" + y
        if x == 2:
            return "b" + y
        if x == 3:
            return "c" + y
        if x == 4:
            return "d" + y
        if x == 5:
            return "e" + y
        if x == 6:
            return "f" + y
        if x == 7:
            return "g" + y
        if x == 8:
            return "h" + y
        else:
            print("ERROR, Wrong Input")
    except:
        print("ERROR, Wrong Input")


def NtoC(N):  # convert string to tuple
    x = N[0]
    y = int(N[1])
    try:
        if x == "a":
            return (1, y)
        if x == "b":
            return (2, y)
        if x == "c":
            return (3, y)
        if x == "d":
            return (4, y)
        if x == "e":
            return (5, y)
        if x == "f":
            return (6, y)
        if x == "g":
            return (7, y)
        if x == "h":
            return (8, y)
        else:
            print("ERROR, Wrong Input")
    except:
        print("ERROR, Wrong Input")


def xToN(x):
    if x == 1:
        return "a"
    if x == 2:
        return "b"
    if x == 3:
        return "c"
    if x == 4:
        return "d"
    if x == 5:
        return "e"
    if x == 6:
        return "f"
    if x == 7:
        return "g"
    if x == 8:
        return "h"
    else:
        print("ERROR, Wrong Input")


class game:
    turn = False  # t = white, f = black
    border = [0, 0, 5]
    pieces = []
    moves = []
    cmove = 1
    finished = False
    draw = False

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
        #print("Moves:")

    def reset(self):
            print("\n\n RESETTING BOARD...\n\n")
            self.turn = False  # t = white, f = black
            self.border = [0, 0, 5]
            self.pieces = []
            self.moves = []
            self.cmove = 1
            self.finished = False
            self.draw = False


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


    def getCurrentSide(self):
        if self.turn:
            return "white"
        else:
            return "black"

    def getCurrentOpp(self):
        if self.turn:
            return "black"
        else:
            return "white"

    def setCurrentSide(self, side):
        if side=="white":
            self.turn = True
        if side=="black":
            self.turn = False

    def turnInd(self):
        ind = [10, 10, 10]
        if self.turn:  # white
            setColor(9, 0, ind)
        else:  # black
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

    def update(self, refresh=True):
        if not self.finished:
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

            self.switch()
        else:
            clearMatrix()
            self.paintBorder()

            for piece in self.pieces:
                self.paintPiece(piece)
            if refresh:
                if self.turn:
                    sys.stdout.write(str(self.cmove) + ". " + str(self.moves[-1]) + " ")
                    sys.stdout.flush()
                else:
                    sys.stdout.write(str(self.moves[-1]) + "\n")
                    sys.stdout.flush()
                    self.cmove += 1


            if self.draw:
                print("\n\n" + " DRAW!")
                self.border = [0, 255, 0]
                self.paintBorder()

            else:
                self.endBorder(self.getCurrentSide())
                print("\n\n" + self.getCurrentSide() + " WON!")

            print("\n\nAll Moves: " + str(self.moves)+"\n\n")


        display()

    def refreshBoard(self):
        clearMatrix()
        self.paintBorder()
        self.turnInd()
        for piece in self.pieces:
            self.paintPiece(piece)

    def freeSquare(self, x, y):
        if self.getPiece(x, y):
            return False  # Square occupied
        else:
            return True  # Square free!

    def getPiece(self, x, y):
        for piece in self.pieces:
            if piece.x == x and piece.y == y:
                return piece
            else:
                pass

    def getPieceN(self, N):
        x, y = NtoC(N)
        return self.getPiece(x, y)

    def findPiece(self, side, name, dest, x0, y0):
        x, y = dest[0], dest[1]

        for piece in self.pieces:
            if piece.name==name and piece.side==side:
                if piece.checkMove(x, y):
                    if self.checkFutureOwnCheck(piece, x, y):
                        if piece.x==x0:
                            return piece
                        if piece.y==y0:
                            return piece
                        if x0==None and y0==None:
                            return piece

        return None

    def checkEnemyPiece(self, x, y, side):
        if not self.freeSquare(x, y):
            if not self.getPiece(x, y).side == side:
                return True
        return False

    def checkEnPassant(self, pawn):
        side = pawn.side
        x, y = pawn.x, pawn.y
        if (y == 4 and side == "black") or (y == 5 and side == "white"):
            if self.checkEnemyPiece(x-1, y, side):  # leftside
                piece = self.getPiece(x-1, y)
                if piece.name == "P" and piece.firstMove:
                    #print("1")
                    return True, piece
            if self.checkEnemyPiece(x+1, y, side):  # rightside
                piece = self.getPiece(x+1, y)
                if piece.name == "P" and piece.firstMove:
                    #print("2")
                    return True, piece

        return False, None


    def sameCol(self, x, x0):
        # same Column
        if x0 == x:
            return True
        else:
            return False

    def sameRow(self, y, y0):
        # same Row
        if y0 == y:
            return True
        else:
            return False

    def sameLane(self, x, y, x0, y0):
        # same Column and row
        if self.sameCol(x, x0) or self.sameRow(y, y0):
            return True
        else:
            return False

    def sameDiagonal(self, x, y, x0, y0):
        if x - x0 == y - y0 or x - x0 == y0 - y:
            return True
        else:
            return False

    def checkRoute(self, x, y, x0, y0):
        # check if direct route to destination is unblocked
        if math.fabs(x - x0) == 1 and (math.fabs(y - y0) == 1 or y - y0 == 0):  # only 1 move
            return True
        if math.fabs(y - y0) == 1 and (math.fabs(x - x0) == 1 or x - x0 == 0):  # only 1 move
            return True

        # same Column
        if x0 == x:
            if y < y0:
                for i in range(y0 - 1, y, -1):
                    if not self.freeSquare(x, i):
                        return False  # Blocked Route
                    else:
                        pass  # Free square

            if y > y0:
                for i in range(y0 + 1, y, +1):
                    if not self.freeSquare(x0, i):
                        return False
                    else:
                        pass

        # same row
        if y0 == y:
            if x < x0:
                for i in range(x0 - 1, x, -1):
                    if not self.freeSquare(i, y):
                        return False
                    else:
                        pass
            if x > x0:
                for i in range(x0 + 1, x, +1):
                    if not self.freeSquare(i, y):
                        return False
                    else:
                        pass

        # same diagonal
        # positive diagonal
        if x - x0 == y - y0:
            if x < x0:
                for i in range(x0 - 1, x, -1):
                    for v in range(y0 - 1, y, -1):
                        if i - x0 == v - y0:
                            if not self.freeSquare(i, v):
                                return False
                            else:
                                pass

            if x > x0:
                for i in range(x0 + 1, x, +1):
                    for v in range(y0 + 1, y, +1):
                        if i - x0 == v - y0:
                            if not self.freeSquare(i, v):
                                return False
                            else:
                                pass
        # negative diagonal
        if x - x0 == y0 - y:
            if x - x0 > 0:
                for i in range(x0 + 1, x, +1):
                    for v in range(y0 - 1, y, -1):
                        if i - x0 == y0 - v:
                            if not self.freeSquare(i, v):
                                return False
                            else:
                                pass
            if y - y0 > 0:
                for i in range(x0 - 1, x, -1):
                    for v in range(y0 + 1, y, +1):
                        if i - x0 == y0 - v:
                            if not self.freeSquare(i, v):
                                return False
                            else:
                                pass
        return True  # Completely free Route

    def blinkPiece(self, piece):
        color = piece.color
        try:
            for i in range(0, 3):
                piece.color = [0, 0, 0]
                self.paintPiece(piece)
                display()
                time.sleep(0.05)
                piece.color = color
                self.paintPiece(piece)
                display()
                time.sleep(0.05)
        except:
            print "For loop error"

    def getKing(self, side):
        for piece in self.pieces:
            if piece.name == "K" and piece.side == side:

                return piece
        #print("Cant Find " + side + " KING!")
        #print(self.pieces)
        return None


    def checkOppCheck(self, side):

        # Find opponent king
        for piece in self.pieces:
            if piece.name == "K" and not piece.side == side:
                oppK = piece

        # Find Piece that checked the enemy king
        for piece in self.pieces:
            if piece.side == side and not piece.name=="K":
                if piece.checkMove(oppK.x, oppK.y):
                    oppK.check = True
                    return True, oppK
        oppK.check = False
        return False, oppK

    def checkOwnCheck(self, side):
        # Find own king
        ownK = self.getKing(side)
        if not ownK==None:
            # Find Piece that can check the own king
            for piece in self.pieces:
                if not piece.side == side and not piece.name=="K":
                    if piece.checkMove(ownK.x, ownK.y):
                        ownK.check = True
                        return True, ownK
            ownK.check = False
            return False, ownK
        return None

    # Can only be called after checkMove()
    # Returns False if own King will be in Check
    def checkFutureOwnCheck(self, piece, x, y):
        x0, y0 = piece.x, piece.y  # save init coord.
        side = piece.side
        pieceD = None
        # CHeck for piece on dest.
        if not self.freeSquare(x, y):
            pieceD = self.getPiece(x, y)
            self.removePiece(pieceD)

        # switch
        piece.x, piece.y = x, y
        if not self.checkOwnCheck(side)==None:
            check, king = self.checkOwnCheck(side)
            if king.check:
                # returns False if own King will be in check
                piece.x, piece.y = x0, y0  # fix
                if not pieceD == None:
                    self.addPiece(pieceD)

                king.check = not king.check
                return False

            else:  # No Check
                piece.x, piece.y = x0, y0
                if not pieceD == None:
                    self.addPiece(pieceD)

                return True

        piece.x, piece.y = x0, y0
        if not pieceD == None:
            self.addPiece(pieceD)
        return False

    def checkMate(self, king):
        if not self.getPossibleMoves(king.side, king)==[]:
            return False


        # CHECKMATE
        self.finished = True
        self.border = [255, 0, 0]
        self.refreshBoard()
        return True

    def removePiece(self, piece):
        self.pieces.remove(piece)

    def addPiece(self, piece):
        self.pieces.append(piece)

    # Border change to show end of game winner/loser
    def endBorder(self, winner):
        win = [0, 255, 0]
        loss = [255, 0, 0]

        if winner == "white":  # White won
            for x in range(0, 10):  # top
                setColor(x, 9, loss)
            for y in range(5, 9):  # upper right
                setColor(9, y, loss)
            for y in range(5, 9):  # upper left
                setColor(0, y, loss)

            for x in range(0, 10):  # bottom
                setColor(x, 0, win)
            for y in range(1, 5):  # lower right
                setColor(9, y, win)
            for y in range(1, 5):  # lower left
                setColor(0, y, win)

        if winner == "black":  # Black won
            for x in range(0, 10):  # top
                setColor(x, 9, win)
            for y in range(5, 9):  # upper right
                setColor(9, y, win)
            for y in range(5, 9):  # upper left
                setColor(0, y, win)

            for x in range(0, 10):  # bottom
                setColor(x, 0, loss)
            for y in range(1, 5):  # lower right
                setColor(9, y, loss)
            for y in range(1, 5):  # lower left
                setColor(0, y, loss)
        display()

    def mateChecker(self):
        check, king = self.checkOppCheck(self.getCurrentSide())
        if king.check and check:
            if self.checkMate(king):
                self.moves[-1] = str(self.moves[-1]) + "#"
                self.refreshBoard()
                self.blinkPiece(king)
                self.blinkPiece(king)
                return True

            else:
                self.moves[-1] = str(self.moves[-1]) + "+"
                self.refreshBoard()
                self.blinkPiece(king)
            return True
        else:
            if self.checkDraw(king.side):
                return True
        return False

    #Checks for Draw of Current side
    # Stalemate
    def checkDraw(self, side):
        #print("Checking Draw...")

        if self.getPossibleMoves(side)==[]:
            self.finished = True
            self.draw = True
            return True

        else:
            return False

    def fixKing(self, king):
        for piece in self.pieces:
            if piece == king:
                #print("King is here")
                return True
        self.addPiece(king)
        print("Fixed King")
        return False

    def getPossibleMoves(self, side, king=None):
        #if not king==None:
            #self.fixKing(king)
        pmoves = []


        #print("POST: ")
        for piece in self.pieces:
            if piece.side == side:
                #if self.cmove==14:
                #if piece.name=="K":
                #    print(piece.getInfo())
                for i in range(1, 9):
                    for v in range(1, 9):
                            #print("checkMove in getPossibleMoves OK")
                        if piece.checkMove(i, v)==True:
                            # King wont be in check
                            if self.checkFutureOwnCheck(piece, i, v):#FAAAILS HERE
                                pass


        #print("POSTPOST:")
        for piece in self.pieces:
            if piece.side == side:
                #if self.cmove==14:
                #if piece.name=="K":
                #    print(piece.getInfo())
                for i in range(1, 9):
                    for v in range(1, 9):
                            #print("checkMove in getPossibleMoves OK")
                        if piece.checkMove(i, v)==True:
                            # King wont be in check
                            if self.checkFutureOwnCheck(piece, i, v):#FAAAILS HERE
                                pmoves.append(piece.getInfo() + " to " + CtoN(i, v))
        return pmoves

    def promotion(self, pawn, x, y, new):
        side = pawn.side

        if (pawn.base == 2 and y == 8): #white
            self.removePiece(pawn)
            # promotion
            if new=="Q":
                new = wQ(x, y)
            if new=="B":
                new = wB(x, y)
            if new=="N":
                new = wN(x, y)
            if new=="R":
                new = wR(x, y)
            return True
        if (pawn.base == 7 and y == 1): #black
            self.removePiece(pawn)
            # promotion
            if new=="Q":
                new = bQ(x, y)
            if new=="B":
                new = bB(x, y)
            if new=="N":
                new = bN(x, y)
            if new=="R":
                new = bR(x, y)
            return True
        else:
            return False

    def illegal(self, piece, x, y):

        self.blinkPiece(piece)
        if piece.name == "P":
            print("Illegal Move: " + CtoN(x, y))
        else:
            print("Illegal Move: " + piece.name + CtoN(x, y))
        return False

    def checkDouble(self, piece, x, y):
        if not piece.name=="K":
            for double in self.pieces:
                if not double==piece and double.name == piece.name and double.side==piece.side and not double.name=="P":
                    if double.checkMove(x, y):
                        if self.checkFutureOwnCheck(double, x, y):
                            #on same column
                            if piece.x==double.x:
                                self.moves[-1] = self.moves[-1][:1] + str(piece.y) + self.moves[-1][1:]
                                return True
                            #same row
                            else:
                                self.moves[-1] = self.moves[-1][:1] + xToN(piece.x) + self.moves[-1][1:]
                                return True
        return False

    def showPieces(self):
        side = self.getCurrentSide()
        for piece in self.pieces:
            if piece.side==side:
                piece.turnWhite()
                self.paintPiece(piece)
        display()
        time.sleep(0.5)
        for piece in self.pieces:
            if piece.side==side:
                piece.resetColor()
                self.paintPiece(piece)
        display()





    def execMove(self, piece, x, y):
        piece.moved = True
        if piece.firstMove == False:
            piece.firstMove = True
        else:
            piece.firstMove = None

        #print("execMove OK")

        self.checkDouble(piece, x, y)
        #print("checkDouble OK")
        piece.setPos(x, y)
        #print("SetPos OK")
        self.mateChecker()
        #print("mateChecker OK")
        self.update()

    def move(self, piece, x, y, promote):
        if(x < 1 or x > 8) or (y < 1 or y > 8):
            print("Wrong Input")
            return self.illegal(piece, x, y)
        if piece==None:
            print("ERROR: Piece is None, might be a illegal move!")
        try:
            if not piece.side == self.getCurrentSide():
                ("\nWrong Side!")
                return self.illegal(piece, x, y)
        except:
            return self.illegal(piece, x, y)


        x0, y0 = piece.x, piece.y

        if piece.checkMove(x, y):
            if self.checkFutureOwnCheck(piece, x, y):

                # Capture
                if self.checkEnemyPiece(x, y, piece.side):
                    pieceD = self.getPiece(x, y)

                    #self.cmove += 1
                    #print("\n Move " + str(self.cmove) + "\n")
                    if piece.name == "P":
                        if self.promotion(piece, x, y, promote):
                            self.moves.append(xToN(x0) + "x" + CtoN(x, y) + "=" + promote)
                            piece = self.getPiece(x, y)
                        else:
                            self.moves.append(xToN(x0) + "x" + CtoN(x, y))
                    else:
                        # Check for multiple pieces being able to capture
                        self.moves.append(piece.name + "x" + CtoN(x, y))
                    #print(self.moves[-1] + "\n")

                    self.removePiece(pieceD)
                    self.execMove(piece, x, y)
                    return True


                #En passant
                if piece.name=="P" and piece.enPassant:
                    check, pawn = self.checkEnPassant(piece)
                    if check:
                        self.moves.append(xToN(x0) + "x" + CtoN(x, y))
                        piece.enPassant = False
                        self.removePiece(pawn)
                        self.execMove(piece, x, y)
                        return True

                # Normal Move
                else:
                    if piece.name == "P":
                        if self.promotion(piece, x, y, promote):
                            self.moves.append(CtoN(x, y) + "=" + promote)
                            piece = self.getPiece(x, y)
                        else:
                            self.moves.append(CtoN(x, y))
                    if piece.name == "K" and x == x0 + 2:  # Castle Kingside
                        self.moves.append("O-O")
                    if piece.name == "K" and x == x0 - 2:  # Castle Queenside
                        self.moves.append("O-O-O")
                    if not piece.name == "P" and not (piece.name == "K" and x == x0 + 2) and not (piece.name == "K" and x == x0 - 2):
                        self.moves.append(piece.name + CtoN(x, y))
                        if self.cmove>48 and piece.getInfo()=="K@b8":
                            print("1")
                    self.execMove(piece, x, y)

                    return True

            else:
                print("\nKing will be in Check")
                return self.illegal(piece, x, y)
        else:
            print("\nCan't move there")
            return self.illegal(piece, x, y)

    def moveN(self, piece, N, promote):
        x, y = NtoC(N)
        return self.move(piece, x, y, promote)

    #Parses standard Chess Notation and makes move
    #move must be a string in correct Chess Notation!
    def parseMove(self, move):
        #Examples: e4, dxe5, Bb5, R2b5, R2xd2, gxh8=Q, O-O, O-O-O
        side = self.getCurrentSide()
        #Begin from the back
        last = move[-1]
        dest = move[-2:]

        if move=="reset":
            self.reset()
        if move=="showPieces":
            self.showPieces()


        if move=="1/2-1/2":
            self.finished = True
            self.draw = True
            print("\n" + move)
            self.update(False)
            return True
        if move=="1-0":
            self.finished = True
            self.setCurrentSide("white")
            print("\n\n" + move)
            self.update(False)
            return True
        if move=="0-1":
            self.finished = True
            self.setCurrentSide("black")
            print("\n\n" + move)
            self.update(False)
            return True


        try:
            if last=="1" or last=="2" or last=="3" or last=="4" or last=="5" or last=="6" or last=="7" or last=="8": #No Promotion or Castle
                if len(move)==2: #Pawn Move
                    piece = self.findPiece(side, "P", NtoC(dest), NtoC(move[0] + "1")[0], None)
                    self.moveN(piece, dest, None)
                    return True
                if len(move)==3: #Normal move (non pawn)
                    piece = self.findPiece(side, move[0], NtoC(dest), None, None)

                    self.moveN(piece, dest, None)
                    return True
                if len(move)==4: #Normal Capture or double move or pawn capture
                    if move[1]=="x":#Normal Capture
                        if move[0]=="Q" or move[0]=="B" or move[0]=="N" or move[0]=="R" or move[0]=="K":
                            piece = self.findPiece(side, move[0], NtoC(dest), None, None)
                            self.moveN(piece, dest, None)
                            return True
                        else: #Pawn Capture
                            piece = self.findPiece(side, "P", NtoC(dest), NtoC(move[0] + "1")[0], None)
                            self.moveN(piece, dest, None)
                            return True
                    else:#double move i.e. R2b2
                        try:
                            if 0 < int(move[1]) < 9:
                                piece = self.findPiece(side, move[0], NtoC(dest), None, int(move[1]))
                                self.moveN(piece, dest, None)
                                return True
                        except:
                            piece = self.findPiece(side, move[0], NtoC(dest), NtoC(move[1] + "1")[0], None)
                            self.moveN(piece, dest, None)
                            return True
                if len(move)==5: #double Capture
                    try:
                        if 0 < int(move[1]) < 9:
                            piece = self.findPiece(side, move[0], NtoC(dest), None, int(move[1]))
                            self.moveN(piece, dest, None)
                            return True
                    except:
                        piece = self.findPiece(side, move[0], NtoC(dest), NtoC(move[1] + "1")[0], None)
                        self.moveN(piece, dest, None)
                        return True
        except:
            pass

        if last=="O": #Castle
            if move=="O-O":#Kingside
                if side=="white":
                    self.moveN(self.getPiece(5, 1), "g1", None)
                else:
                    self.moveN(self.getPiece(5, 8), "g8", None)
                return True
            else: #Queenside
                if side=="white":
                    self.moveN(self.getPiece(5, 1), "c1", None)
                else:
                    self.moveN(self.getPiece(5, 8), "c8", None)
                return True

        try:
            if last=="Q" or last=="B" or last=="N" or last=="R": #Promotion
                #examples: e8=Q, dxe8=R
                piece = self.findPiece(side, "P", NtoC(move[-4:-2]), None, None)
                self.moveN(piece, move[-4:-2], move[-1])
                return True

            if last=="#" or last=="+":
                move = move[:-1]
                return self.parseMove(move)
        except:
            pass

        return False



class piece:
    name = "piece"
    firstMove = False
    moved = False
    color = []
    scolor = []

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

    def getInfo(self):
        return str(self.side + " " + self.name + "@" + CtoN(self.x, self.y))

    def turnWhite(self):
        self.scolor = self.color
        self.color = [255, 255, 255]

    def resetColor(self):
        self.color = self.scolor


class P(piece):
    name = "P"
    base = 0
    nA = 1
    bA = 2
    enPassant = False

    def checkMove(self, x, y):
        # Normal move (0, -1)
        # Possible first move (0, -2)
        # Possible Capture (+-1, -1)
        if game.checkRoute(x, y, self.x, self.y):
            if game.freeSquare(x, y):
                if self.y == self.base and y == self.y + self.bA and x == self.x:
                    return True
                if y == self.y + self.nA and x == self.x:
                    return True

            if ((x == self.x - 1 or x == self.x + 1) and y == self.y + self.nA):  # Capture
                if game.checkEnemyPiece(x, y, self.side):  # normal
                    return True
                if game.checkEnPassant(self):  # en passant
                    if sys._getframe(1).f_code.co_name == "move": #execute only if move() called checkmove()
                        self.enPassant = True
                    return True

        return False

class wP(P):
    color = [30, 30, 255]
    side = "white"
    base = 2
    nA = 1
    bA = 2


class bP(P):
    color = [0, 0, 255]
    side = "black"
    base = 7
    nA = -1
    bA = -2


class R(piece):
    name = "R"

    def checkMove(self, x, y):
        # Possible Move (0, +-y)/(+-x, 0)
        if game.sameLane(x, y, self.x, self.y):
            if game.checkRoute(x, y, self.x, self.y):
                if game.freeSquare(x, y):
                    return True
                else:
                    if game.checkEnemyPiece(x, y, self.side):
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
        # Possible Moves (+-1, +-2)/(+-2, +-1)
        # 8 Squares max
        if game.freeSquare(x, y) or game.checkEnemyPiece(x, y, self.side):
            if (((x == self.x + 1 or x == self.x - 1) and (y == self.y + 2 or y == self.y - 2)) or ((x == self.x + 2 or x == self.x - 2) and (y == self.y + 1 or y == self.y - 1))):
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
        # Possible Moves (+-x, 1-y)
        if game.sameDiagonal(x, y, self.x, self.y) and game.checkRoute(x, y, self.x, self.y):
            if game.freeSquare(x, y) or game.checkEnemyPiece(x, y, self.side):
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
        # Possible diagonal and lane moves
        if (game.sameDiagonal(x, y, self.x, self.y) or game.sameLane(x, y, self.x, self.y)):
            if game.checkRoute(x, y, self.x, self.y):
                if game.freeSquare(x, y):
                    return True
                else:
                    if game.checkEnemyPiece(x, y, self.side):
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

        if game.freeSquare(x, y) or game.checkEnemyPiece(x, y, self.side):
            if game.sameLane(x, y, self.x, self.y) and (math.fabs(x - self.x) == 1 or math.fabs(y - self.y) == 1):
                return True
            if game.sameDiagonal(x, y, self.x, self.y) and (math.fabs(x - self.x) == 1 and math.fabs(y - self.y) == 1):
                return True
            if not self.moved:  # Castle
                if x == 7:
                    if game.getPiece(8, self.y) and game.getPiece(8, self.y).moved == False:  # Kingside
                        if game.checkRoute(5, self.y, 8, self.y):
                            # move rook as king will be moved in move()
                            rook = game.getPiece(8, self.y)
                            if sys._getframe(1).f_code.co_name == "move": #execute only if move() called checkmove()
                                rook.x = 6
                                rook.moved = True
                                rook.firstMove = True
                            return True
                if x == 3:
                    # Queenside
                    if game.getPiece(1, self.y) and game.getPiece(1, self.y).moved == False:
                        if game.checkRoute(5, self.y, 1, self.y):
                            # move rook as king will be moved in move()
                            rook = game.getPiece(1, self.y)
                            if sys._getframe(1).f_code.co_name == "move": #execute only if move() called checkmove()
                                rook.x = 4
                                rook.moved = True
                                rook.firstMove = True
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
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
    # Border init
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

    # Checkerboard pattern
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


#standard promote=Q
def m(a, b, t=0.25):  # a, b str in Notation
    time.sleep(t)
    game.moveN(game.getPieceN(a), b, "Q")

def p(move, t=0): #in Notation
    time.sleep(t)

    if not move==" " or not move=="*" or move or not game.finished:
        if not game.parseMove(move):
            print("\nPARSING FAILED AT " + move)

def printPGNInfo(string):
        length = len(string)
        inp = ""
        i = 0
        print("PGN INFO:")
        print("---------\n")
        while i < length:        #Ignore everything in [], {}
            if string[i]=="[":
                i+=1
                while not string[i]=="]":
                    inp = inp + string[i]
                    i+=1
                i+=1
                print(inp)
                inp = ""
                continue
            if string[i]=="{":
                i+=1
                while not string[i]=="}":
                    i+=1
                i+=1
                continue

            #ignore \n
            if string[i:i+1]=="\n":
                i += 1
                if not inp=="":
                    print(inp)
                inp=""
                continue
            else:
                i+=1
        print("\n---------\n")

def parseString(string, t=0.5):
    printPGNInfo(string)

    length = len(string)
    inp = ""
    i = 0

    while i < length:        #Ignore everything in [], {}
        if string[i]=="[":
            i+=1
            while not string[i]=="]":
                i+=1
            i+=1
            continue
        if string[i]=="{":
            i+=1
            while not string[i]=="}":
                i+=1
            i+=1
            continue


        #ignore \n
        if string[i:i+1]=="\n":
            i += 1
            if not inp=="":
                p(inp, t)
            inp=""

            continue
        #ignore spaces
        if string[i]==" ":
            i+=1
            p(inp, t)
            inp=""

        if not string[i]==" ":
            inp = inp + string[i]
            i+=1

        #check if in count
        if inp[-1]==".":
            inp = ""
            i+=1
    if not inp=="":
        p(inp, t)
        inp=""

def playPGN(filename="chess/masterGame1.pgn", t=0.5):
    file = open(filename, "r")
    pgn = file.read()

    parseString(pgn, t)



def test():
    #King test
    game.pieces = []
    game.addPiece(wK(1, 5))
    game.addPiece(wP(1, 4))
    game.addPiece(wP(2, 3))
    game.addPiece(wP(3, 2))
    game.addPiece(wP(3, 5))
    game.addPiece(wP(6, 4))
    game.addPiece(wP(8, 4))

    game.addPiece(bK(2, 8))
    game.addPiece(bP(1, 6))
    game.addPiece(bP(2, 7))
    game.addPiece(bP(3, 6))
    game.addPiece(bP(4, 5))
    game.addPiece(bP(6, 5))
    game.addPiece(bP(8, 5))

    game.refreshBoard()
    display()

    p("Kb6")
    p("Kc8")


# MAIN

# startupAnimation()
game = game()


# TESTS
'''playPGN("chess/test.pgn", 0)
time.sleep(1)
game.reset()'''
#playPGN("chess/masterGame1.pgn", 0)
#test()



'''
#Promotion + Illegal
p("e4")
p("d6")

p("e5")
p("d5")

p("a3")
p("f5")

p("exf6")
p("e6")

p("f7+")
p("Ke7")

p("fxg8=Q")#Promotoion
p("a6")

p("Qe6+") #Check not mate (king can take Queen)
p("Ke8") #Illegal
'''

'''
#en passant
m("e2", "e4")
m("d7", "d6")

m("e4", "e5")
m("d6", "d5")

m("a2", "a3")
m("f7", "f5")

m("e5", "f6")
'''

'''
# Checkmate and capture test

m("e2", "e4")
m("e7", "e5")

m("f1", "c4")
m("b7", "b6")
# print(game.getPieceN("d4").getInfo())

m("g2", "g4")
m("f7", "f5")

m("g4", "f5") #capture gxf5
m("b6", "b5")

m("c4", "b5") #capture Bxb5
m("a7", "a6")

m("b5", "c4")
m("a6", "a5")

m("d2", "d4")
m("e5", "d4")  # capture exd4

m("d1", "d4")  # capture Qxd4

m("b8", "c6")


m("d4", "d5")
m("g7", "g5")

m("d5", "f7")  # Capture and Checkmate Qxf7#
'''

'''
# Checkmate test

m("e2", "e4")
m("e7", "e5")

m("f1", "c4")
m("a7", "a6")
# print(game.getPieceN("d4").getInfo())

m("d2", "d4")
m("e5", "d4")  # capture exd4

m("d1", "d4")  # capture Qxd4

m("b8", "c6")


m("d4", "d5")
m("g7", "g5")

m("d5", "f7")  # Capture and Checkmate Qxf7##
m("e8", "e7")  # test for move verification

'''
'''
#King test
game.pieces = []
game.addPiece(wK(1, 5))
game.addPiece(wP(1, 4))
game.addPiece(wP(2, 3))
game.addPiece(wP(3, 2))
game.addPiece(wP(3, 5))
game.addPiece(wP(6, 4))
game.addPiece(wP(8, 4))

game.addPiece(bK(2, 8))
game.addPiece(bP(1, 6))
game.addPiece(bP(2, 7))
game.addPiece(bP(3, 6))
game.addPiece(bP(4, 5))
game.addPiece(bP(6, 5))
game.addPiece(bP(8, 5))

game.refreshBoard()
display()

p("Kb6")
p("Kc8")
'''
'''
#Stalemate Test and double test
game.pieces = []
game.addPiece(bK(5, 8))
game.addPiece(wK(1, 1))
game.addPiece(wQ(4, 1))
game.addPiece(wQ(8, 3))
game.addPiece(wR(1, 7))
game.refreshBoard()
display()
m("h3", "f1")
'''

def checkInput():
    # falls stdin vorhanden wird es auf input gespeichert
    if select.select([sys.stdin], [], [], 0)[0]:
        input = sys.stdin.readline().strip()
        return input

'''
In App:
1. Decide between play and PGN Mode
    a) If play:
        i. Parse every input (add reset parse)
    b) If PGN:
        i. Select from directory and send PGN as string
        ii. playPGN string

'''
print("Please enter one of the following commands:\n- play (for manual Play)\n- pgn (for parsing and playing a string in pgn format)")
while True:
    #input = raw_input("PGN filename in /chess/? ")
    inp = checkInput()
    if inp == "play":
        game.reset()
        while not game.finished:
            inp = checkInput()
            while inp==None:
                inp = checkInput()
            p(inp)

    if inp=="pgn":
        game.reset()
        inp = checkInput()
        while inp==None:
            inp = checkInput()
        parseString(inp)

    else:
        continue
    #playPGN("chess/"+input, 0.5)

    while not game.finished:
        input = raw_input("Move? ")
        p(input)





#!fold-children
