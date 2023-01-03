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
        for position in POSITIONS:
            self.create_new_link(position)

    # Adds a new link after eating food
    def enlarge_snake(self):
        self.create_new_link(self.links[-1].position())

    # Adds a new link at the back of the snake
    def create_new_link(self, position):
        link = Turtle("square")
        link.penup()
        link.shapesize(1)
        link.color("white")
        link.goto(position)
        self.links.append(link)

    def move(self):
        time.sleep(0.1)
        for link in range(len(self.links) - 1, 0, -1):
            # updating the snake's links from the end point to starting point
            x = round(self.links[link - 1].xcor())
            y = round(self.links[link - 1].ycor())
            self.links[link].goto(x, y)
        self.links[0].forward(MOVE_DISTANCE)

    # searches if snake's head touches the body
    def is_move_legit(self):
        for link in self.links[1:]:
            if self.head.distance(link) < 10:
                return False
        return True

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
