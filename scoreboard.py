from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")

    def display_score(self):
        self.penup()
        self.goto(x=-30, y=275)
        self.write(f"Score:{self.score}", align="center", font=("arial", 15, "normal"))
        self.hideturtle()

    def increase_score(self):
        self.score += 1
        self.clear()
        self.display_score()

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER ", align="center", font=("arial", 15, "normal"))
