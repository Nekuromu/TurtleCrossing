from random import randint, choice
from car import Car

SPAWN_INDEXES = [-250, -206, -162, -118, -74, -30, 14, 58, 102, 146, 190, 234]


class TrafficManager:

    def __init__(self):
        self.cars = []
        self.difficulty = 5

    def spawn_car(self):
        new_car = Car()
        new_car.goto(300, choice(SPAWN_INDEXES))
        self.cars.append(new_car)
