from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()
        with open("highscore.txt") as file:
            self.high_score = int(file.read())

    def gain_point(self):
        self.score += 1
        self.update_scoreboard()

    def lose_point(self):
        self.score -= 1

    def update_scoreboard(self):
        self.clear()
        self.write("Score: " + str(self.score), align="center", font=("Arial", 24, "normal"))

    def final_score(self):
        high_score = 0
        if self.score > self.high_score:
            self.high_score = self.score
            with open("highscore.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.clear()
        self.goto(0, 0)
        self.write("Game Over" + "\nFinal Score: " + str(self.score) + "\nHigh Score: " + str(self.high_score), align="center", font=("Arial", 24, "normal"))