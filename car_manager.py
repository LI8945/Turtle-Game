from random import choice, randint, random
from turtle import Turtle
from player import STARTING_POSITION

# List of colors that the cars can randomly be assigned
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        # List to keep track of all car objects on the screen
        self.all_cars = []
        # Initial speed of the cars
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Only create a car occasionally to prevent overcrowding
        random_choice = randint(1, 6)
        if random_choice == 1:
            # Create a new car as a stretched turtle square
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(choice(COLORS))  # Assign a random color
            random_y = randint(-250, 250)  # Random Y position for variation
            new_car.goto(300, random_y)  # Start at right edge of screen
            self.all_cars.append(new_car)  # Add to list of cars

    def move_cars(self):
        # Move all cars to the left by current speed
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        # Increase speed when player completes a level
        self.car_speed += MOVE_INCREMENT


