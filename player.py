from turtle import Turtle

# Starting position of the turtle (bottom center)
STARTING_POSITION = (0, -280)
# How far the turtle moves each time the player presses "Up"
MOVE_DISTANCE = 10
# Y-coordinate that marks the finish line (top of the screen)
FINISH_LINE_Y = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")         # Set turtle shape
        self.color("black")          # Set turtle color
        self.penup()                 # Don't draw when moving
        self.setheading(90)          # Point the turtle upward
        self.go_to_start()           # Move turtle to starting position

    def go_up(self):
        # Move the turtle forward by a fixed distance
        self.forward(MOVE_DISTANCE)

    def go_to_start(self):
        # Move the turtle back to the starting position
        self.goto(STARTING_POSITION)

    def is_at_finish_line(self):
        # Check if the turtle has reached the top of the screen
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False

