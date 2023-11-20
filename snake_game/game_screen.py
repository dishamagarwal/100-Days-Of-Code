from turtle import Screen

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.game_is_on = True

    def update_screen(self, snake):
        self.screen.update()
        snake.move_by_one()
        if self.game_is_on:
            self.screen.ontimer(lambda: self.update_screen(snake), 100)

    def click_to_exit(self):
        self.screen.exitonclick()

    def listen_keywords(self, snake):
        self.screen.listen()
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")
