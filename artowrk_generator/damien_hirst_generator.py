import turtle
import colorgram
import random

class Hirst:
    def __init__(self, turtle: turtle.Turtle):
        self.pen = turtle

    def convert_color(self, color):
        return (color.rgb.r, color.rgb.g, color.rgb.b)

    def generate_art(self, image):
        self.pen.goto(-300, 300)
        self.pen.speed(10)
        turtle.colormode(255)
        self.colors = colorgram.extract(image, 8)
        # pen.hideturtle()
        for i in range(10): 
            for j in range(10): 
                # dot 
                self.pen.dot(50, self.convert_color(random.choice(self.colors))) 
                
                # distance for another dot 
                self.pen.forward(60) 
            self.pen.backward(10*60) 
            
            # direction 
            self.pen.right(90) 
            self.pen.forward(60) 
            self.pen.left(90) 
