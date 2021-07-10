from pygame.math import Vector2
from pygame import Rect, Color
from pygame.draw import rect
import constants as C

class SNAKE:
    def __init__(self):
        self.body = [Vector2(C.SNAKE_INIT_X, C.SNAKE_INIT_Y),
                     Vector2(C.SNAKE_INIT_X-1, C.SNAKE_INIT_Y),
                     Vector2(C.SNAKE_INIT_X-2, C.SNAKE_INIT_Y),]
        self.direction = C.MOVE_RIGHT

    def draw(self):
        for part in self.body:
            x_coordinate = part.x * C.CELL_SIZE
            y_coordinate = part.y * C.CELL_SIZE
            part_rect = (Rect(x_coordinate, y_coordinate, C.CELL_SIZE, C.CELL_SIZE))
            rect(C.WINDOW, Color('blue'), part_rect)

    def move(self):
        new_body = self.body[:-1]
        head = self.body[0] + self.direction
        new_body.insert(0, head)
        self.body = new_body[:]

    def grow(self):
        new_body = self.body[:]
        head = self.body[0] + self.direction
        new_body.insert(0, head)
        self.body = new_body[:]
