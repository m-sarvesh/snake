from setup import *
import sys
import constants as C

def game_loop():
    setup(C.WINDOW_WIDTH, C.WINDOW_HEIGHT)
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            if event.type == C.SNAKE_MOVE:
                C.SNAKE.move()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_UP:
                    C.SNAKE.direction = C.MOVE_TOP
                if event.key == pg.K_RIGHT:
                    C.SNAKE.direction = C.MOVE_RIGHT
                if event.key == pg.K_DOWN:
                    C.SNAKE.direction = C.MOVE_BOTTOM
                if event.key == pg.K_LEFT:
                    C.SNAKE.direction = C.MOVE_LEFT

        C.WINDOW.fill(pg.Color('white'))
        C.FOOD.draw()
        C.SNAKE.draw()
        pg.display.update()
        C.CLOCK.tick(C.FRAME_RATE)

if __name__ == "__main__":
    game_loop()