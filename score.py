from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Courier New', 16, 'normal')

class Scoreboard(Turtle):

    def __init__(self, shape: str = "classic", undobuffersize: int = 1000, visible: bool = True) -> None:
        super().__init__(shape, undobuffersize, visible)
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.score = 0
        
        with open("data.txt") as file:
            self.highscore = int(file.read())
        
        self.update()
           
    def add_point(self):
        self.score += 1
        self.update()
    
    def update(self):
        self.clear()
        self.write(arg=f"Score: {self.score} Highscore: {self.highscore}", align=ALIGNMENT, font=FONT)
    
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score    
            
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        
        self.score = 0
        self.update()


