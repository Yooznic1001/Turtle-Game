COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]

MOVE_INCREMENT = 10
import random
from turtle import Turtle
class CarManager():
    def __init__(self):
        self.cars = []
        self.STARTING_MOVE_DISTANCE = 5



    def car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Turtle()
            car.shape("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.color(random.choice(COLORS))
            car.penup()
            car.setheading(180)
            car.goto(x=300, y=random.randint(-250, 250))
            self.cars.append(car)

    def move_car(self):
        for car in self.cars:
            car.forward(self.STARTING_MOVE_DISTANCE)

    def car_speed(self):
        self.STARTING_MOVE_DISTANCE += 5