import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carm = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(player.up, "Up")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    carm.newcar()
    carm.move()
    for car in carm.cars:
        if player.distance(car) < 20:
            score.gameover()
            game_is_on = False
    if player.finish():
        carm.speedup()
        score.display()


screen.exitonclick()
