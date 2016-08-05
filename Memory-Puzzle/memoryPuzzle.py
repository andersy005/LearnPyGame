
# Memory Puzzle clone
# By Anderson Banihirwe  


import random
import pygame
import sys
from pygame.locals import *


FPS = 30  # frames per second, the general speed of the program
WINDOWWIDTH = 640  # size of window's width in pixels
WINDOWHEIGHT = 480  # size of window's height in pixels
REVEALSPEED = 8  # speed boxes' sliding reveals and covers
BOXSIZE = 40  # size of box height & width in pixels
GAPSIZE = 10  # size of gap between boxes in pixels
BOARDWIDTH = 10  # number of columns of icons
BOARDHEIGHT = 7  # number of rows of icons

assert(BOARDHEIGHT * BOARDWIDTH) % 2 == 0, 'Board needs to have an even number of boxes for pairs of matches.'

XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

GRAY = (100, 100, 100)
NAVYBLUE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLUE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'

ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)
assert len(ALLCOLORS) * len(ALLSHAPES) * 2 >= BOARDWIDTH * BOARDHEIGHT, \
    "Board is too big for the number of shapes/colors defined"


def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode(WINDOWWIDTH, WINDOWHEIGHT)

    mousex = 0   # used to store x coordinate of  mouse event
    mousey = 0   # used to store y coordinate of mouse event
    pygame.display.set_caption('Memory Game')

    mainBoard = getRandomizedBoard()
    revealedBoxes = generateRevealedBoxesData(False)

    firstSelection = None  # stores the (x, y) of the first box clicked.

    DISPLAYSURF.fill(BGCOLOR)
    startGameAnimation(mainBoard)

    while True:  # main game loop
        mouseClicked = False

        DISPLAYSURF.fill(BGCOLOR)  # drawing the window
        drawBoard(mainBoard, revealedBoxes)

        for event in pygame.event.get():  # event handling loop
            if event.type == QUIT or (event.type == KEYUP and event.key == K_ESCAPE):
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

        boxx, boxy = getBoxAtPixel(mousex, mousey)