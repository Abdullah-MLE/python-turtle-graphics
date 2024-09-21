from turtle import Turtle, Screen
import random


def outlines():
    t.penup()
    t.goto(-600, -300)

    for i in range(2):
        t.pendown()
        t.fd(650)
        t.right(90)
        t.fd(1250)
        t.right(90)
    t.right(90)

    t.penup()
    upx, usy = -550, 300
    t.goto(upx, usy)
    t.pendown()
    for i in range(4):
        for s in range(4):
            t.fd(250)
            t.right(90)
        upx += 300
        t.penup()
        t.goto(upx, usy)
        t.pendown()

    t.penup()
    upx, usy = -550, 0
    t.goto(upx, usy)
    t.pendown()
    for i in range(4):
        for s in range(4):
            t.fd(250)
            t.right(90)
        upx += 300
        t.penup()
        t.goto(upx, usy)
        t.pendown()

def project1():
    t.penup()
    t.goto(-450, 250)
    t.pendown()

    ls = [120, 90, 72, 60, 51.429, 45, 40, 36]
    ls2 = [3, 4, 5, 6, 7, 8, 9, 10]

    for i in range(7):
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        for r in range(ls2[i]):
            t.fd(50)
            t.right(ls[i])

def project2():
    t.penup()
    t.goto(-200, 250)
    t.width(15)

    for x in range(-220, -20, 20):
        for y in range(80, 280, 20):
            t.penup()
            t.goto(x, y)
            t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
            t.pendown()
            t.goto(x, y)
    t.width(5)

def project3():
    t.penup()
    x, y = 80, 80
    t.goto(x, y)
    t.width(20)

    for i in range(10):
        t.goto(x, y)
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        t.pendown()
        t.goto(y, x)
        x += 18
        # y += 18
        t.penup()

    for i in range(11):
        t.goto(x, y)
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        t.pendown()
        t.goto(y, x)
        # x -= 18
        y += 18
        t.penup()

def project4(num):
    t.penup()
    t.goto(420, 120)
    t.pendown()
    t.width(7)
    x, y = 450, 120
    ls = [0,1]
    for i in range(num):
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        if x >= 580:
            x -= 20
            t.goto(x, y)
        if x <= 380:
            x += 20
            t.goto(x, y)
        if y >= 280:
            y -= 20
            t.goto(x, y)
        if y <= 80:
            y += 20
            t.goto(x, y)
        else:
            cho1 = random.choice(ls)
            cho2 = random.choice(ls)
            if cho1 == 0 and cho2 == 0:
                x += 20
                t.goto(x, y)
            elif cho1 == 1 and cho2 == 0:
                y += 20
                t.goto(x,y)
            elif cho1 == 0 and cho2 == 1:
                x -= 20
                t.goto(x, y)
            elif cho1 == 1 and cho2 == 1:
                y -= 20
                t.goto(x, y)

def project5(num):
    t.penup()
    t.goto(-425, -125)
    t.pendown()
    t.width(1)
    for i in range(num):
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        t.circle(60)
        t.left(360 / num)

def project6():
    t.penup()
    t.goto(-125, -118)
    t.pendown()
    t.width(2)
    for i in range(80):
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        t.circle(i * 2, 90)
        t.left(30)
    t.left(210)
    t.right(90)


def project7():
    t.penup()
    t.goto(60, -120)
    t.pendown()
    t.width(2)
    t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
    for i in range(36):
        t.forward(230)
        t.right(170)  # Rotate
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))  # Change color

def project8():
    t.penup()
    t.goto(420, -125)
    t.pendown()
    t.width(3)
    for i in range(20):
        width = random.randint(20, 100)
        height = random.randint(20, 100)
        t.color("#" + ''.join([random.choice('0123456789ABCDEF') for j in range(6)]))
        t.left(random.randint(0, 180))
        t.begin_fill()
        for _ in range(2):
            t.forward(width)
            t.left(90)
            t.forward(height)
            t.left(90)
        t.end_fill()
        t.penup()
        t.goto(random.randint(350, 600), random.randint(-270, -20))
        t.pendown()

t = Turtle()

screen = Screen()
screen.setup(width = 1380, height = 750)

t.speed(10000)
t.width(5)
t.left(90)

outlines()
project1()
project2()
project3()
project4(350)
project5(50)
project6()
project7()
project8()




















screen.exitonclick()
