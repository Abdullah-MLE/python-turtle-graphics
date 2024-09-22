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

        # cheat_x = snake.xcor()
        # cheat_y = snake.ycor()
        # cheat_dir = snake.heading
        # if cheat_dir == 90:
        #     self.goto(cheat_x, cheat_y + 20)
        # elif cheat_dir == 0:
        #     self.goto(cheat_x + 20, cheat_y)
        # elif cheat_dir == 180:
        #     self.goto(cheat_x -20, cheat_y)
        # elif cheat_dir == 270:
        #     self.goto(cheat_x, cheat_y - 20)
