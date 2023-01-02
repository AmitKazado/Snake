import random
import time
from turtle import Screen, Turtle


class Snake:
    screen = Screen()
    turtles = []
    direction = 0
    board_boundaries = [-290, 290]
    scoreboard = 0
    game_is_on = True
    fruit = Turtle("circle")

    # TODO: init fruit location & check if location is legit.
    def __init__(self):
        self.screen.tracer(0)
        self.screen.title("Snake")
        self.screen.setup(600, 600)
        self.screen.bgcolor("black")
        self.turtles.append(Turtle("square"))
        self.turtles[0].penup()
        self.turtles[0].shapesize(0.5)
        self.turtles[0].color("white")
        self.turtles.append(self.turtles[0].clone().goto(self.turtles[0].xcor() - 11, self.turtles[0].ycor()))
        self.turtles.append(self.turtles[0].clone().goto(self.turtles[0].xcor() - 22, self.turtles[0].ycor()))
        self.fruit.shapesize(0.5)
        self.fruit.color("blue")
        self.set_fruit_location()
        self.screen.update()
        self.start_game()
        self.screen.exitonclick()

    # TODO: check is location is valid
    def set_fruit_location(self):
        self.fruit.penup()
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        self.fruit.goto(x, y)

    def move(self):
        if not (self.is_move_legit()):
            self.game_over()
        else:
            for t in self.turtles:
                pass

    # TODO: case 1: snake is reaching boundaries of board
    #       case 2: snake hits himself/tale
    # Snake can't go backwards
    def is_move_legit(self):
        if self.direction - self.turtles[0].heading() == 180:
            return False
        return True

    # Checks is the snake ate the current fruit
    def is_fruit_eaten(self):
        if self.turtles[0].position == self.fruit.position:
            self.update_scoreboard()
            return True
        return False

    # Adds a new link at the back of the snake
    def enlarge_snake(self):
        if self.turtles[-2].xcor() - self.turtles[-1].xcor() == 0:  # snake is moving up/down
            if self.turtles[-2].ycor() - self.turtles[-1] == 11:  # snake is moving up
                self.turtles.append(
                    self.turtles[-1].clone().goto(self.turtles[-1].xcor(), self.turtles[-1].ycor() - 11))
            else:  # snake is moving down
                self.turtles.append(
                    self.turtles[-1].clone().goto(self.turtles[-1].xcor(), self.turtles[-1].ycor() + 11))
        else:  # snake is moving right/left
            if self.turtles[-2].xcor() - self.turtles[-1].xcor() == 11:  # snake is moving right
                self.turtles.append(
                    self.turtles[-1].clone().goto(self.turtles[-1].xcor() - 11, self.turtles[-1].ycor()))
            else:  # snake is moving left
                self.turtles.append(
                    self.turtles[-1].clone().goto(self.turtles[-1].xcor() + 11, self.turtles[-1].ycor()))

    def game_over(self):
        self.screen.textinput("Game Over", f"Your final score is: {self.scoreboard}")
        self.game_is_on = False

    def update_scoreboard(self):
        self.scoreboard += 1

    # TODO: make the snake move according to player's direction keys, fix moving bug (goto)
    def start_game(self):
        self.screen.listen()
        while self.game_is_on:
            self.screen.update()
            time.sleep(0.2)
            for t_num in range(len(self.turtles) - 1, 0, -1):
                # updating the snake's links from the end point to starting point
                x = self.turtles[t_num - 1].xcor()
                y = self.turtles[t_num - 1].ycor()
                self.turtles[t_num].goto(x, y)
            self.turtles[0].forward(11)
