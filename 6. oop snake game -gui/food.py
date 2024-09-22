from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color("#ffffff")
        self.speed(10)
        random_x = random.randrange(-180, 180, 20)
        random_y = random.randrange(-130, 200, 20)
        self.goto(random_x, random_y)

    def refresh(self):
        random_x = random.randrange(-180, 180, 20)
        random_y = random.randrange(-130, 200, 20)
        self.goto(random_x, random_y)