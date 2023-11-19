from turtle import Turtle, Screen
from snake import Snake

class Main():
    # initial setup
    snake = Snake()
    snake.add_segment(-20, 0)
    snake.add_segment(-40, 0)
    
    screen = Screen()
    screen.setup(600, 600)
    screen.bgcolor("black")
    screen.title("Snake Game")
    screen.exitonclick()

if __name__ == '__main__':
    Main()