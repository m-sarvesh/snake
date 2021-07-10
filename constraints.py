import constants as C

# Check if the snake have reached to food 
def check_food():
    if C.SNAKE.body[0] == C.FOOD.loc:
        # Eat food and grow
        C.FOOD.relocate()
        C.SNAKE.grow()

# Check if the snake bites itself or bumped into boundary
def check_failure():
    # Check if snake bumped into boundary
    if C.SNAKE.body[0].x <= 0 or \
       C.SNAKE.body[0].x >= C.C.NUM_OF_CELLS or \
       C.SNAKE.body[0].y <= 0 or \
       C.SNAKE.body[0].y >= C.NUM_OF_CELLS :
            game_over()
    
    # Check if snake bites itself
    for part in C.SNAKE.body[1:]:
        if C.SNAKE.body[0] == part:
            game_over()


def game_over():
    pass
       

