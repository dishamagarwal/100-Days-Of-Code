from turtle import Turtle

MOVE_DIST = 20
UP = 90
DOWN = 270 
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.snake_body = []
        self.setup(0, 0)
        self.head = self.snake_body[0]
    
    def setup(self, x, y):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        seg.goto(x, y)
        self.snake_body.append(seg)

    def add_segment(self):
        seg = Turtle("square")
        seg.penup()
        seg.color("white")
        x, y = self.snake_body[-1].pos()
        seg.goto(x, y)
        self.snake_body.append(seg)

    def move_by_one(self):
        for idx in range(len(self.snake_body)-1, 0, -1):
            self.snake_body[idx].goto(self.snake_body[idx-1].xcor(), self.snake_body[idx-1].ycor())
        self.head.forward(MOVE_DIST)

    def within_bounds(self):
        x, y = self.head.pos()
        if x >= 290 or x <= -290 or y >= 290 or y <= -290:
            return False
        return True
    
    def collision_with_tail(self):
        for seg in self.snake_body:
            if seg == self.head:
                pass
            elif self.head.distance(seg) < 10:
                return True
        return False

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)