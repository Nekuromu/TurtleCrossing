from random import randint
from car import Car

SPAWN_INDEXES = [-249, -223.5, -198, -172.5, -147, -121.5, -96, -70.5, -45, -19.5, 6, 31.5, 57, 82.5, 108,
                 133.5, 159, 184.5, 210, 235.5]


class TrafficManager:

    def __init__(self):
        self.cars = []
        self.difficulty = 15
        self.car_amount = len(SPAWN_INDEXES)

    def spawn_car(self):
        new_car = Car()
        new_car.goto(300, SPAWN_INDEXES.pop(randint(0, len(SPAWN_INDEXES) - 1)))
        new_car.reset_pos = new_car.ycor()
        self.cars.append(new_car)

    def next_level(self):
        for car in self.cars:
            car.speed -= 1
