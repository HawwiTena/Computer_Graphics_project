# Window with a background Image
import pygame

import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from pygame.locals import *


# Making the window using pygame
pygame.init()

# We need to load the turtle Image or avatar onto the screen

turtleAvatar = pygame.image.load('Images\\turtle.png')
backgroundImage = pygame.image.load('Images\\gameBackground2a.jpg')
turtles_X_Coordinate = 400
turtles_Y_Coordinate = 500
X_Coordinate_Change = 0
Y_Coordinate_Change = 0


def init():
    pygame.init()
    # display = (500, 500)
    # create the screen
    # screen = pygame.display.set_mode((900,600),  DOUBLEBUF | OPENGL)
    screen = pygame.display.set_mode((900, 600))
    pygame.display.set_caption("TurtleRex")
    icon = pygame.image.load('Images\\turtleGameIcon.png')
    pygame.display.set_icon(icon)

def draw(newX, newY):
    screen = pygame.display.set_mode((900, 600))
    screen.blit(backgroundImage, (0, 0))
    screen.blit(turtleAvatar, (newX, newY))




def main(turtles_X_Coordinate, turtles_Y_Coordinate):
    init()
    turtles_X_Coordinate = 400
    turtles_Y_Coordinate = 500
    X_Coordinate_Change = 0
    Y_Coordinate_Change = 0
    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    X_Coordinate_Change = -0.9
                elif event.key == pygame.K_RIGHT:
                    X_Coordinate_Change = 0.9
                elif event.key == pygame.K_UP:
                    Y_Coordinate_Change = -0.9
                elif event.key == pygame.K_DOWN:
                    Y_Coordinate_Change = 0.9

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    X_Coordinate_Change = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    Y_Coordinate_Change = 0


        turtles_X_Coordinate += X_Coordinate_Change
        turtles_Y_Coordinate += Y_Coordinate_Change
        draw(turtles_X_Coordinate, turtles_Y_Coordinate)
        pygame.display.update()
        pygame.display.flip()
        pygame.time.wait(10)
main(turtles_X_Coordinate, turtles_Y_Coordinate)




