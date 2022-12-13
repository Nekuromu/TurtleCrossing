from turtle import Screen
from player import Player
from traffic_manager import TrafficManager
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
traffic_manager = TrafficManager()

screen.listen()
screen.onkeypress(player.move, "w")

game_frame = 0
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    print(game_frame)

    for car in traffic_manager.cars:
        car.move()

        if player.distance(car) < 30:
            game_running = False
        if car.xcor() < -330:
            print("CAR DELETED.")
            car.reset()
            traffic_manager.cars.remove(car)

    game_frame += 1
    if game_frame == traffic_manager.difficulty:
        traffic_manager.spawn_car()
        game_frame = 0

screen.exitonclick()
