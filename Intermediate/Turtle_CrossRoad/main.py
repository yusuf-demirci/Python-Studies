from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True


while game_is_on:
    time.sleep(car.car_speed)
    screen.update()
    car.create_car()
    car.move_cars()
    for cars in car.all_cars:    
        if player.distance(cars) < 20:
            game_is_on = False
            scoreboard.game_over()

    if player.ycor() > 280:
        player.reset_position()
        car.increase_speed()
        scoreboard.next_level()

    
screen.exitonclick()