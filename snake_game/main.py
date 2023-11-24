from snake import Snake
from game_screen import GameScreen
from food import Food

class Main():
    # initial setup
    score = 0
    screen = GameScreen()
    snake = Snake()
    screen.listen_keywords(snake)
    snake.add_segment(-20, 0)
    snake.add_segment(-40, 0)
    food = Food()
    screen.update_screen(snake, food, score)
    screen.click_to_exit()

if __name__ == '__main__':
    main = Main()
