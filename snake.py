from turtle import Turtle

STARTING_POSTIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self) -> None:
        self.snake = []
        self.create_snake()
        self.head = self.snake[0]

    def create_snake(self):
        for cor in STARTING_POSTIONS:
            self.add_segment(cor)

    def move(self):
        for segnum in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[segnum - 1].xcor()
            new_y = self.snake[segnum - 1].ycor()

            self.snake[segnum].goto(new_x, new_y)  
        self.snake[0].forward(MOVE_DISTANCE)
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def add_segment(self, cor):
        segment = Turtle("square")
        segment.color("white")
        segment.penup()
        segment.goto(cor)
        self.snake.append(segment)

    def extend(self):
        self.add_segment(self.snake[-1].position())
    
    def reset(self):
        for seg in self.snake:
            seg.goto(1000, 1000)
        self.snake.clear()
        self.create_snake()
        self.head = self.snake[0]