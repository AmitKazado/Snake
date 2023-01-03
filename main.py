from turtle import Screen, Turtle

from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake
snakey = Turtle()
# snakey.goto
screen = Screen()
screen.title("Snake")
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
scoreboard = Scoreboard()
game_is_on = True

while game_is_on:
    screen.update()
    snake.move()
    if snake.head.distance(food) < 15:
        food.generate_new_location()
        scoreboard.increase_score()


screen.exitonclick()
