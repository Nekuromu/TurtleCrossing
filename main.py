from turtle import Screen
from player import Player
from traffic_manager import TrafficManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Turtle Crossing")
screen.tracer(0)

player = Player()
traffic_manager = TrafficManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "w")

game_frame = 0
game_running = True
while game_running:
    time.sleep(0.1)
    screen.update()

    if player.ycor() == 280:
        player.reset_player()
        scoreboard.level += 1
        traffic_manager.next_level()

    for car in traffic_manager.cars:
        car.move()

        if player.distance(car) < 25:
            game_running = False
        if car.xcor() < -330:
            if not player.allowed_to_move:
                scoreboard.update_board("GO GO GO GOOOOO!")
            player.allowed_to_move = True
            car.reset_car()

    game_frame += 1
    if game_frame == traffic_manager.difficulty and len(traffic_manager.cars) != 20:
        traffic_manager.spawn_car()
        if len(traffic_manager.cars) == 1:
            scoreboard.update_board("Ready? Set!?")
        game_frame = 0

screen.exitonclick()
