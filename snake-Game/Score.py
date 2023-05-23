from turtle import *

class Scoreboared(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("aqua")        
        self.penup()
        self.goto(x=0 ,y=270)
        self.write(f"SCORE : {self.score} ",align="center" , font=("cursive" , 10 , "bold"))
        self.hideturtle()

    def game_over(self):
        self.goto(x=0 ,y=0)
        self.write(f" GAME OVER ",align="center" , font=("georgia" , 10 , "bold"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"SCORE : {self.score} ",align="center" , font=("cursive" , 10 , "bold"))