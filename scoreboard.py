from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="Center", font=FONT)

    def score(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER", align="Center", font=FONT)





