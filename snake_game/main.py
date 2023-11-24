from snake import Snake
from game_screen import GameScreen
from food import Food
from scoreboard import Scoreboard

class Main():
    # initial setup
    screen = GameScreen()
    snake = Snake()
    score = Scoreboard()
    screen.listen_keywords(snake)
    snake.add_segment()
    snake.add_segment()
    food = Food()
    screen.update_screen(snake, food, score)
    screen.click_to_exit()

if __name__ == '__main__':
    main = Main()
