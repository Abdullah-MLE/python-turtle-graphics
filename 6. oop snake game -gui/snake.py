from turtle import Turtle
MOVE_DISTANCE = 10
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-MOVE_DISTANCE, 0), (-MOVE_DISTANCE * 2, 0)]

class Snake:
    def __init__(self):
        self.segment = []
        self.initialize_the_snake()
        self.head = self.segment[0]

    def initialize_the_snake(self):
        pos = 0
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def move(self):
        for seg in range(len(self.segment) - 1, 0, -1):
            x = self.segment[seg - 1].xcor()
            y = self.segment[seg - 1].ycor()
            self.segment[seg].goto(x, y)
        self.segment[0].fd(MOVE_DISTANCE)

    def add_segment(self, pos):
        t = Turtle("square")
        t.shapesize(MOVE_DISTANCE / 20, MOVE_DISTANCE / 20)
        t.penup()
        t.color("#ffffff")
        t.goto(pos)
        self.segment.append(t)

    def extend(self):
        self.add_segment(self.segment[-1].position())

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)




















