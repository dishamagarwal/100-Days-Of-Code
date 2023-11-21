from snake import Snake
from game_screen import GameScreen
from food import Food

class Main():
    # initial setup
    screen = GameScreen()
    snake = Snake()
    screen.listen_keywords(snake)
    snake.add_segment(-20, 0)
    snake.add_segment(-40, 0)
    screen.update_screen(snake)
    food = Food()
    screen.click_to_exit()

if __name__ == '__main__':
    main = Main()
