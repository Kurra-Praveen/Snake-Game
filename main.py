from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Score
import time

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("Welcome to snake game")

my_screen.tracer(0)

my_snake = []

snake = Snake()

snake.create_snake()
food = Food()
score = Score()
score.display_score()

my_screen.listen()
my_screen.onkey(snake.up, "Up")
my_screen.onkey(snake.down, "Down")
my_screen.onkey(snake.left, "Left")
my_screen.onkey(snake.right, "Right")

is_game_on =True
while is_game_on:
    my_screen.update()
    time.sleep(0.1)

    snake.move()
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.incre_snake()
        score.increase_score()

    if snake.head.xcor() > 300 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -300:
        is_game_on = False
        score.game_over()

    for segment in my_snake[1:]:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            is_game_on = False
my_screen.exitonclick()
