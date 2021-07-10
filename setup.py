import pygame as pg
import constants as C
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
    pg.time.set_timer(C.SNAKE_MOVE, C.VELOCITY)

def draw_frame():
    C.WINDOW.fill(pg.Color('white'))
    C.FOOD.draw()
    C.SNAKE.draw()