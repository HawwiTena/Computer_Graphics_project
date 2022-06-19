import random
from time import sleep

import pygame


class TurtleRunning:
    def __init__(self):

        pygame.init()
        self.display_width = 800
        self.display_height = 600
        self.black = (0, 0, 0)
        self.white = (255, 255, 255)
        self.clock = pygame.time.Clock()
        self.gameDisplay = None

        self.initialize()

    def initialize(self):

        self.bumped = False

        self.turtleImg = pygame.image.load('.\\img\\turtle2.png')
        self.turtle_x_display = (self.display_width * 0.45)
        self.turtle_y_display = (self.display_height * 0.8)
        self.turtle_width = 49

        # enemy_car
        self.turtle2 = pygame.image.load('.\\img\\turtle2.png')
        self.turtle2_startx= random.randrange(310, 450)
        self.turtle2_starty = -600
        self.turtle2_speed = 5
        self.turtle2_width= 49
        self.turtle2_height = 100

        # Background
        self.bgImg = pygame.image.load(".\\img\\back_ground.jpg")
        self.bg_x1 = (self.display_width / 2) - (360 / 2)
        self.bg_x2 = (self.display_width / 2) - (360 / 2)
        self.bg_y1 = 0
        self.bg_y2 = -600
        self.bg_speed = 3
        self.count = 0

    def turtle(self, car_x_coordinate, car_y_coordinate):
        self.gameDisplay.blit(self.turtleImg, (self.turtle_x_display, self.turtle_y_display))

    def racing_window(self):
        self.gameDisplay = pygame.display.set_mode((self.display_width, self.display_height))
        pygame.display.set_caption('turtle race')
        self.run_turtle()

    def run_turtle(self):

        while not self.bumped:

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.bumped = True
                # print(event)

                if (event.type == pygame.KEYDOWN):
                    if (event.key == pygame.K_LEFT):
                        self.turtle_x_display -= 50
                        print ("CAR X COORDINATES: %s" % self.turtle_x_display)
                    if (event.key == pygame.K_RIGHT):
                        self.turtle_x_display += 50
                        print ("CAR X COORDINATES: %s" % self.turtle_x_display)
                    print ("x: {x}, y: {y}".format(x=self.turtle_x_display, y=self.turtle_y_display))

            self.gameDisplay.fill(self.black)
            self.back_ground_raod()

            self.run_turtle2(self.turtle2_startx, self.turtle2_starty)
            self.turtle2_starty += self.turtle2_speed

            if self.turtle2_starty > self.display_height:
                self.turtle2_starty = 0 - self.turtle2_height
                self.turtle2_startx = random.randrange(310, 450)

            self.turtle(self.turtle_x_display, self.turtle_y_display)
            self.highscore(self.count)
            self.count += 1
            if (self.count % 100 == 0):
                self.turtle2_speed += 1
                self.bg_speed += 1
            if self.turtle_y_display < self.turtle2_starty + self.turtle2_height:
                if self.turtle_x_display > self.turtle2_startx and self.turtle_x_display < self.turtle2_startx + self.turtle2_width or self.turtle_x_display + self.turtle_width > self.turtle2_startx and self.turtle_x_display + self.turtle_width < self.turtle2_startx + self.turtle2_width:
                    self.bumped = True
                    self.display_message("Game Over !!!")

            if self.turtle_x_display < 310 or self.turtle_x_display > 460:
                self.bumped = True
                self.display_message("Game Over !!!")

            pygame.display.update()
            self.clock.tick(60)

    def display_message(self, msg):
        font = pygame.font.SysFont("comicsansms", 72, True)
        text = font.render(msg, True, (255, 255, 255))
        self.gameDisplay.blit(text, (400 - text.get_width() // 2, 240 - text.get_height() // 2))
        self.display_credit()
        pygame.display.update()
        self.clock.tick(60)
        sleep(1)
        car_racing.initialize()
        car_racing.racing_window()

    def back_ground_raod(self):
        self.gameDisplay.blit(self.bgImg, (self.bg_x1, self.bg_y1))
        self.gameDisplay.blit(self.bgImg, (self.bg_x2, self.bg_y2))

        self.bg_y1 += self.bg_speed
        self.bg_y2 += self.bg_speed

        if self.bg_y1 >= self.display_height:
            self.bg_y1 = -600

        if self.bg_y2 >= self.display_height:
            self.bg_y2 = -600

    def run_turtle2(self, thingx, thingy):
        self.gameDisplay.blit(self.turtle2, (thingx, thingy))

    def highscore(self, count):
        font = pygame.font.SysFont("arial", 20)
        text = font.render("Score : " + str(count), True, self.white)
        self.gameDisplay.blit(text, (0, 0))

    def display_credit(self):
        font = pygame.font.SysFont("lucidaconsole", 14)
        text = font.render("Thanks for playing!", True, self.white)
        self.gameDisplay.blit(text, (600, 520))


if __name__ == '__main__':
    turtle_running= TurtleRunning()
    turtle_running.racing_window()
