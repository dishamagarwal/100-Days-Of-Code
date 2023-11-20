from turtle import Turtle
from snake import Snake
from game_screen import GameScreen

class Main():
    # initial setup
    screen = GameScreen()
    snake = Snake()
    snake.add_segment(0, 0)
    snake.add_segment(-20, 0)
    snake.add_segment(-40, 0)
    screen.update_screen(snake)
    screen.click_to_exit()

if __name__ == '__main__':
    main = Main()
