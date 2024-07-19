import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

car = CarManager()
player = Player()
score = Scoreboard()
score.scoree()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()

    car.car()
    car.move_car()

    for carss in car.cars:
        if player.distance(carss) < 20:
            game_is_on = False
            score.end()

    if player.ycor() == 280:
        car.car_speed()
        player.restart()
        score.scoree()


screen.exitonclick()