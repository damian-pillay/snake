from turtle import Screen
from score import Scoreboard
from snake import Snake
from food import Food
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)
screen.update()

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.up, "w")
screen.onkey(snake.down, "s")
screen.onkey(snake.left, "a")
screen.onkey(snake.right, "d")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.08)
    snake.move()

    #Detect Collision with food

    if snake.head.distance(food) <  17:
        score.add_point()
        snake.extend()
        food.refresh()
    
    #Detect Collision with wall

    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        score.reset()

    #Detect Collision with tail
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            score.reset()

screen.exitonclick()