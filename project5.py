# Tring to switch between screens in pygame

import glfw
import numpy as np
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


# Making the window using pygame
pygame.init()

class Screen():
    def __init__(self, title, width=900, height=445):
        self.title = title
        self.width = width
        self.height = height
        # self.fill = fill
        self.current = False
    def makeCurrent(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode((self.width, self.height))
    def endCurrent(self):
        self.current = False
    def checkUpdate(self):
        return self.current
    # def screenUpdate(self):
    #     if((self.current)):
    #         self.
    def returnTitle(self):
        return self.screen

class Button():
    def __init__(self, x, y, sx, sy, bcolour, fcolour, fbcolour,font, fontsize,  text):
        self.x = x
        self.y = y
        self.sx = sx
        self.sy = sy
        self.bcolour = bcolour
        self.fbcolour = fbcolour
        self.fcolour = fcolour
        self.font = font
        self.fontsize = fontsize
        self.text = text
        self.current = False
        self.buttonf = pygame.font.SysFont(font, fontsize)

    def showButton(self, display):
        if(self.current):
            pygame.draw.rect(display, self.fbcolour, (self.x, self.y, self.sx, self.sy))

        else:
            pygame.draw.rect(display, self.bcolour, (self.x, self.y, self.sx, self.sy))
        textsurface = self.buttonf.render(self.text, False, self.fcolour)
        display.blit(textsurface,((self.x + (self.sx/2) - (self.fontsize/2)* (len(self.text)/2) - 5, (self.y + (self.sy/2) - (self.fontsize/2) - 4     ))))


