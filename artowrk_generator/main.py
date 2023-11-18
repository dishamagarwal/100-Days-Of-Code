from turtle import Turtle, Screen
from draw import Draw
from damien_hirst_generator import Hirst

class Main():
    timmy_turtle = Turtle()

    """Make timmy go in a square"""
    draw = Draw(timmy_turtle)
    timmy_turtle.penup() 
    art = Hirst(timmy_turtle)
    art.generate_art("pokemon.png")
    # draw.square()
    # draw.dotted_line()
    # draw.random_walk()
    screen = Screen()
    screen.colormode(255)
    screen.exitonclick()

if __name__ == '__main__':
    Main()