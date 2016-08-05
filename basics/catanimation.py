
# coding: utf-8

# In[1]:

import pygame
import sys
from pygame.locals import *


# In[2]:

pygame.init()


# In[3]:

FPS = 30 # frames per second setting
fpsClock = pygame.time.Clock()


# In[4]:

# set up the window
DISPLAYSURF = pygame.display.set_mode((400, 300), 0, 32)
pygame.display.set_caption('Animation')


# In[5]:

WHITE = (255, 255, 255)
catImg = pygame.image.load('Cat.png')
catx = 10
caty = 10
direction = 'right'


# In[6]:

while True:
    DISPLAYSURF.fill(WHITE)
    
    if direction == 'right':
        catx += 5
        if catx == 280:
            direction = 'down'
        
    elif direction == 'down':
        caty += 5
        if caty == 220:
            direction = 'left'
            
    elif direction == 'left':
        catx -= 5
        if catx == 10:
            direction = 'up'
            
    elif direction == 'up':
        caty -= 5
        if caty == 10:
            direction = 'right'
            
    DISPLAYSURF.blit(catImg, (catx, caty))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    fpsClock.tick(FPS)

