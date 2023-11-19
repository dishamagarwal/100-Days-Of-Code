from turtle import Turtle

class Snake:
    def __init__(self):
        self.snake_body = []

    def add_segment(x, y):
        seg = Turtle("square")
        seg.color("white")
        seg.goto(x, y)
        return seg