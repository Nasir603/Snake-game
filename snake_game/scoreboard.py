from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.update_score()

    def update_score(self):
        """Clear previous score and display updated score"""
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=('Arial', 12, 'bold'))
    def game_over(self):
        """Write game over on screen when snake collide with wall or itself"""
        self.goto(0,0)
        self.write(f"Game Over", align="center", font=('Arial', 12, 'bold'))

    def increase_score(self):
        """Increase score and update display"""
        self.score += 1
        self.update_score()
