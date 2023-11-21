import random
from turtle import Turtle

# inheritence
class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.shapesize(0.5, 0.5)
        self.penup()
        self.color("yellow")
        self.speed("fastest")
        self.generate_food()

    def generate_food(self):
        self.x = random.randint(-280, 280)
        self.y = random.randint(-280, 280)
        self.goto(self.x, self.y)
