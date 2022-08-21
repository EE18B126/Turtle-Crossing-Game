from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "black", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        super().__init__()
        self.cars = []
        self.movenum = STARTING_MOVE_DISTANCE
        self.newcar()

    def newcar(self):
        if random.randint(1, 6) == 1:
            newcar = Turtle("square")
            newcar.color(random.choice(COLORS))
            newcar.penup()
            newcar.shapesize(stretch_wid=1, stretch_len=2)
            newcar.goto(300, random.randint(-250, 250))
            self.cars.append(newcar)

    def move(self):
        for car in self.cars:
            car.backward(self.movenum)

    def speedup(self):
        self.movenum += MOVE_INCREMENT

