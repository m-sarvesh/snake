import pygame as pg
import random
import constants as C
from pygame.math import Vector2

class FOOD:
    def __init__(self):
        self.x = random.randint(0, C.NUM_OF_CELLS - 1)
        self.y = random.randint(0, C.NUM_OF_CELLS - 1)
        self.loc = Vector2(self.x, self.y)
    
    def draw(self):
        x_coordinate = self.loc.x * C.CELL_SIZE
        y_coordinate = self.loc.y * C.CELL_SIZE
        food_rect = pg.Rect(x_coordinate, y_coordinate, C.CELL_SIZE, C.CELL_SIZE)
        pg.draw.rect(C.WINDOW, pg.Color('red'), food_rect)

    def relocate(self):
        self.x = random.randint(0, C.NUM_OF_CELLS - 1)
        self.y = random.randint(0, C.NUM_OF_CELLS - 1)
        self.loc = Vector2(self.x, self.y)