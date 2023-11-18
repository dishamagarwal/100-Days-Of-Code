import turtle
import random

class Draw:
    def __init__(self, timmy: turtle):
        self.timmy = timmy
    
    def square(self):
        self.timmy.shape("turtle")
        self.timmy.speed(1)
        self.timmy.color("black", "CadetBlue3")
        for _ in range(4):
            self.timmy.forward(100)
            self.timmy.right(90)
        
    def dotted_line(self):
        self.timmy.shape("turtle")
        self.timmy.speed(1)
        self.timmy.color("black", "CadetBlue3")
        for _ in range(25):
            self.timmy.penup()
            self.timmy.forward(5)
            self.timmy.pendown()
            self.timmy.forward(5)

    def random_walk(self):
        self.timmy.speed(10)
        self.timmy.pensize(10)
        turtle.colormode(255)
        self.timmy.hideturtle()
        for _ in range(250):
            self.timmy.pencolor((random.randint(0, 225), random.randint(0, 225), random.randint(0, 225)))
            self.timmy.forward(20)
            self.timmy.setheading(random.choice([0,90, 180, 270]))