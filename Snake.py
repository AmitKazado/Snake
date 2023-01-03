import time
from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
POSITIONS = ((0, 0), (0, -20), (0, -40))

class Snake:

    # TODO: init fruit location & check if location is legit.
    def __init__(self):
        self.links = []
        self.create_snake()
        self.head = self.links[0]

    def create_snake(self):
        for i in range(3):
            self.links.append(Turtle("square"))
            self.links[i].penup()
            self.links[i].shapesize(1)
            self.links[i].color("white")
            self.links[i].goto(POSITIONS[i])

    def move(self):
        time.sleep(0.1)
        for link in range(len(self.links) - 1, 0, -1):
            # updating the snake's links from the end point to starting point
            x = round(self.links[link - 1].xcor())
            y = round(self.links[link - 1].ycor())
            self.links[link].goto(x, y)
        self.links[0].forward(MOVE_DISTANCE)

    # TODO: case 1: snake is reaching boundaries of board
    #       case 2: snake hits himself/tale
    # Snake can't go backwards
    def is_move_legit(self):
        if self.head.heading() - self.links[0].heading() == 180:
            return False
        return True

    # Adds a new link at the back of the snake
    def enlarge_snake(self):
        if self.links[-2].xcor() - self.links[-1].xcor() == 0:  # snake is moving up/down
            if self.links[-2].ycor() - self.links[-1] == MOVE_DISTANCE:  # snake is moving up
                self.links.append(
                    self.links[-1].clone().goto(self.links[-1].xcor(), self.links[-1].ycor() - MOVE_DISTANCE))
            else:  # snake is moving down
                self.links.append(
                    self.links[-1].clone().goto(self.links[-1].xcor(), self.links[-1].ycor() + MOVE_DISTANCE))
        else:  # snake is moving right/left
            if self.links[-2].xcor() - self.links[-1].xcor() == MOVE_DISTANCE:  # snake is moving right
                self.links.append(
                    self.links[-1].clone().goto(self.links[-1].xcor() - MOVE_DISTANCE, self.links[-1].ycor()))
            else:  # snake is moving left
                self.links.append(
                    self.links[-1].clone().goto(self.links[-1].xcor() + MOVE_DISTANCE, self.links[-1].ycor()))

    def up(self):
        if self.head.heading() != DOWN:
            self.links[0].setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.links[0].setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.links[0].setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.links[0].setheading(LEFT)
