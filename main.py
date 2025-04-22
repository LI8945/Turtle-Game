import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)  # Turn off automatic screen updates for smoother animation

# Create game objects
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# Listen for keypresses to move the turtle
screen.listen()
screen.onkey(player.go_up, "Up")

# Main game loop
game_is_on = True
while game_is_on:
    time.sleep(0.1)  # Delay to control game speed
    screen.update()  # Refresh the screen

    car_manager.create_car()  # Occasionally generate new cars
    car_manager.move_cars()   # Move all cars across the screen

    # Check for collision between turtle and any car
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()

    # Check if player successfully reached the top
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.score()

# Keep the screen open after the game ends
screen.exitonclick()
