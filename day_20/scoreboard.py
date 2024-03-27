from  turtle import Turtle
FONT = ("Courier",25,"italic")
class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("deep pink")
        self.hideturtle()
        with open("data.txt", "r") as file:
            self.highscore = file.read()
        self.penup()
        self.goto(0,270)
        self.score=0
        self.update_score()
    def update_score(self):
        self.clear()
        if self.score < int(self.highscore):
            self.write(f"score :{self.score} Highscore: {self.highscore}", align="center", font=FONT)
        else:
            self.highscore=self.score
            with open("data.txt", "w") as file:
                file.write(f"{self.highscore}")
            self.write(f"score :{self.highscore} Highscore: {self.highscore}" , align="center", font=FONT)
    def game_over(self):
        self.write("game over" )

    def increse_score(self):
        self.score+=1
        self.clear()
        self.update_score()



    def reset(self):
                self.score=0
                self.update_score()




    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("Game Over" ,align="center" ,font=FONT)
