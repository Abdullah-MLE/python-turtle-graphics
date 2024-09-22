from turtle import Screen
from snake import Snake, MOVE_DISTANCE
from food import Food
from scoreboard import ScoreBoard
import time

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

for i in range(200):
    scoreboard.update_score()
    snake.extend()


screen = Screen()
screen.setup(width=600, height=600)
screen.bgpic("Artboard 1.png")
screen.title("Snake Game")
screen.tracer(0)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(.1)
    snake.move()
    if snake.head.distance(food) <= 50:
        food.refresh()
        scoreboard.update_score()
        snake.extend()

    if snake.head.xcor() >= 200:
        snake.head.goto(-195, snake.head.ycor())
    if snake.head.xcor() <= -200:
        snake.head.goto(205, snake.head.ycor())
    if snake.head.ycor() >= 215:
        snake.head.goto(snake.head.xcor(), -130)
    if snake.head.ycor() <= -135:
        snake.head.goto(snake.head.xcor(), 220)

    # if snake.head.xcor() >= 200 or snake.head.xcor() <= -200 or snake.head.ycor() >= 215 or snake.head.ycor() <= -135:
    #     game_is_on = False
    #     scoreboard.game_over()
    #
    for segment in snake.segment[1:]:
        if snake.head.distance(segment) < 5:
            game_is_on = False
            scoreboard.game_over()




screen.mainloop()