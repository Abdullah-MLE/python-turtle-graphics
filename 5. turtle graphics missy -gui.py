import random
from turtle import Turtle, Screen

def create_new_ball():
    b = Turtle()
    b.shape("circle")
    b.speed(10)
    b.penup()
    b.left(random.randint(0, 360))
    b.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    return b

def bounce(t):
    c = t.heading()
    x = t.xcor()
    y = t.ycor()

    if x >= 190:
        if 0 <= c < 90:
            t.setheading(180 - c)
        elif 270 < c < 360:
            t.setheading(180 - c)
        ls.append(create_new_ball())

    if x <= -190:
        if 90 < c < 180:
            t.setheading(180 - c)
        elif 180 < c < 270:
            t.setheading(180 - c)
        ls.append(create_new_ball())

    if y >= 315:
        if 0 < c < 90:
            t.setheading(-c)
        elif 90 < c < 180:
            t.setheading(-c)
        ls.append(create_new_ball())

    if y <= -315:
        if 180 < c < 270:
            t.setheading(-c)
        elif 270 < c < 360:
            t.setheading(-c)
        ls.append(create_new_ball())



screen = Screen()
screen.bgcolor("#212528")
screen.setup(width=450, height=700)
screen.tracer(10)

ls = [create_new_ball()]
while True:
    for b in ls:
        bounce(b)
        b.fd(10)


screen.mainloop()
