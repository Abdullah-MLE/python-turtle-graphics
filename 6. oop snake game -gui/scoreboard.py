from turtle import Turtle

class ScoreBoard:
    def __init__(self):
        self.t = Turtle()
        self.t.penup()
        self.t.speed(100)
        self.t.hideturtle()
        self.t.color("#ffffff")
        self.t.goto(0, 270)
        self.score = 0
        self.t.write(arg=f"Score : {self.score}", align="center", move=False, font=("Courier", 18, "normal"))

    def update_score(self):
        self.score += 1
        self.t.clear()
        self.t.goto(0, 270)
        self.t.write(arg=f"Score : {self.score}", align="center", move=False, font=("Arial", 15, "normal"))

    def game_over(self):
        self.t.goto(0, -40)
        self.t.color("red")
        self.t.write(arg=f"GAME OVER", align="center", move=False, font=("Arial", 60, "normal"))
