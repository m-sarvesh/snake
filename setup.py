import pygame as pg
import constants as C
import os
import food
import snake

def setup(width, height):
    pg.init()
    pg.display.set_caption("Snake")
    C.WINDOW = pg.display.set_mode( (width, height) )
    C.WINDOW.fill(pg.Color('white'))
    C.CLOCK = pg.time.Clock()
    C.FOOD = food.FOOD()
    C.SNAKE = snake.SNAKE()
    load_graphics()
    pg.display.set_icon(C.ICON)
    pg.time.set_timer(C.SNAKE_MOVE, C.VELOCITY)

def draw_frame():
    C.WINDOW.fill(pg.Color('white'))
    C.FOOD.draw()
    C.SNAKE.draw()

def load_graphics():
    C.FOOD_IMG = pg.image.load(os.path.join('graphics', 'food.png'))
    # Convert image to a format in which pygame can work with it easily
    C.FOOD_IMG = C.FOOD_IMG.convert_alpha()
    C.FOOD_IMG = pg.transform.scale( C.FOOD_IMG, (C.CELL_SIZE, C.CELL_SIZE) )
    C.ICON = pg.image.load(os.path.join('graphics', 'logo.png')).convert_alpha()
