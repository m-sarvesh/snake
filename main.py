from setup import *
import sys
import constants as C
import constraints as rules

def game_loop():
    setup(C.WINDOW_WIDTH, C.WINDOW_HEIGHT)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == C.SNAKE_MOVE:
                C.SNAKE.move()
                rules.check_food()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    if C.SNAKE.direction.y != 1:
                        C.SNAKE.direction = C.MOVE_TOP
                if event.key == pg.K_RIGHT:
                    if C.SNAKE.direction.x != -1:
                        C.SNAKE.direction = C.MOVE_RIGHT
                if event.key == pg.K_DOWN:
                    if C.SNAKE.direction.y != -1:
                        C.SNAKE.direction = C.MOVE_BOTTOM
                if event.key == pg.K_LEFT:
                    if C.SNAKE.direction.x != 1:
                        C.SNAKE.direction = C.MOVE_LEFT
        draw_frame()
        pg.display.update()
        C.CLOCK.tick(C.FRAME_RATE)

if __name__ == "__main__":
    game_loop()