# import pandas
import turtle

class Main():
    turtle = turtle.Turtle()
    screen = turtle.Screen()
    shape = "blank_states_img.gif"
    screen.addshape(shape)
    turtle.shape(shape)
    guessed_count = 0
    turtle.title("Guess the State")
    turtle.textinput(guessed_count + "/50 States Guessed", "what is another state name?")

    turtle.mainloop()

if __name__ == '__main__':
    main = Main()