from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []

    def add_segment(self, x, y):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(x, y)
        self.snake_body.append(seg)

    def move_by_one(self):
        for seg in self.snake_body:
            seg.forward(20)