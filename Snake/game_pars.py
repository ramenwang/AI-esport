import os
import pygame
import argparse
import seaborn as sns
import numpy as np
from random import randint


class thematic_setting():

    def __init__(self, window_width, window_height):
        pygame.display.set_caption('AI Snake Game')
        self.window_width = window_width
        self.window_height = window_height
        self.gameDisplay = pygame.display.set_mode(size = (window_width, window_height + 60)) # why +60
        self.bg = pygame.image.load("img/background.png")
        self.crash = False
        self.player = Player(self)
        self.food = Food()
        self.score = 0


class Player(object):

    def __init__(self, thematics):
        """

        """

        self.theme = thematics
        x = 0.45 * thematics.window_width
        y = 0.5 * thematics.window_height
        self.x = x - x % 20 # position on x-axis
        self.y = y - y % 20 # position on y-axis
        self.position = []
        self.position.append([self.x, self.y])
        self.food = 1
        self.eaten = False
        self.image = pygame.image.load('img/snakeBody.png')
        self.x_change = 20 # initially move towards right ?
        self.y_change = 0


    def update_position(self, x, y):
        """
        Define how snake updates its position

        :param x: given new x position
        :param y: given new y position

        :return self.position: updated position list
        :rtype: a list same as the length of position list
        """

        if self.position[-1][0] != x or self.position[-1][1] != y: # make sure that given x,y is not the last nearest position
            self.position[-1][0], self.position[-1][1] = x,y
            # update the position of each part of the snakeBody
            for i in range(0, self.food-1):
                self.position[i][0], self.position[i][1] = self.position[i+1]


    def do_move(self, move, x, y, food, agent):
        """

        """

        if self.eaten: # eat a food
            self.position.append([self.x, self.y])
            self.eaten = False
            self.food = self.food + 1

        if np.array_equal(move, [0,1,0]): # if going forward
            move_array = [self.x_change, self.y_change]
        elif np.array_equal(move, [1,0,0]) and self.y_change==0: # turn left, going horizontal
            move_array = [0, -self.x_change]
        elif np.array_equal(move, [1,0,0]) and self.x_change==0: # turn left, going vertical
            move_array = [self.y_change, 0]
        elif np.array_equal(move, [0,0,1]) and self.y_change==0: # turn right, going horizontal
            move_array = [0, self.x_change]
        elif np.array_equal(move, [0,0,1]) and self.x_change==0: # turn right, going vertical
            move_array = [-self.y_change, 0]
