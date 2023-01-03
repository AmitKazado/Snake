from turtle import Screen
from Food import Food
from Scoreboard import Scoreboard
from Snake import Snake

MAX_BOUNDARY = 285
MIN_BOUNDARY = -285

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
        snake.enlarge_snake()

    if snake.head.xcor() > MAX_BOUNDARY or snake.head.ycor() > MAX_BOUNDARY or snake.head.xcor() < MIN_BOUNDARY or snake.head.ycor() < MIN_BOUNDARY:
        scoreboard.game_over()
        game_is_on = False

    if not snake.is_move_legit():
        scoreboard.game_over()
        game_is_on = False

screen.exitonclick()
