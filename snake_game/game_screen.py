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
        snake.move_by_one()  # Corrected line
        if self.game_is_on:
            self.screen.ontimer(lambda: self.update_screen(snake), 100)

    def click_to_exit(self):
        self.screen.exitonclick()
