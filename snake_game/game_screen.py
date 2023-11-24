
from turtle import Screen

class GameScreen:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.screen.title("Snake Game")
        self.screen.tracer(0)
        self.game_is_on = True

    def update_screen(self, snake, food, score):
        self.screen.update()
        snake.move_by_one()
        if self.game_is_on:
            if snake.head.distance(food) < 15:
                food.generate_food()
                score.gain_point()
                snake.add_segment()
            if not snake.within_bounds() or snake.collision_with_tail():
                self.game_is_on = False
            self.screen.ontimer(lambda: self.update_screen(snake, food, score), 100)
        else:
            score.final_score()

    def click_to_exit(self):
        self.screen.exitonclick()

    def listen_keywords(self, snake):
        self.screen.listen()
        self.screen.onkey(snake.up, "Up")
        self.screen.onkey(snake.down, "Down")
        self.screen.onkey(snake.left, "Left")
        self.screen.onkey(snake.right, "Right")