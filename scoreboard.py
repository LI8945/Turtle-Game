from turtle import Turtle

# Font style for the scoreboard
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.setup_appearance()
        self.display_level()

    def setup_appearance(self):
        # Set appearance of the scoreboard turtle
        self.color("black")
        self.penup()
        self.hideturtle()

    def display_level(self):
        # Display the current level on the screen
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.level}", align="Center", font=FONT)

    def increase_level(self):
        # Increase level when the player crosses
        self.level += 1
        self.display_level()

    def show_game_over(self):
        # Display game over message at the center
        self.goto(0, 0)
        self.write("GAME OVER", align="Center", font=FONT)




