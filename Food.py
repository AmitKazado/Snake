import random
from turtle import Turtle


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.create_food()

    def create_food(self):
        self.shape("circle")
        self.shapesize(0.5)
        self.color("blue")
        self.speed("fastest")
        self.penup()
        self.generate_new_location()

    def generate_new_location(self):
        self.goto(random.randint(-290, 290), random.randint(-290, 260))
