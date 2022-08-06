from turtle import Turtle, Screen

STARTING_POSITIONS = [(0, 0), (0, -20), (0, -40)]
DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

screen = Screen()


class Snake:
    def __init__(self):

        self.my_snake = []
        self.create_snake()
        self.head = self.my_snake[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.extend_snake(position)

    def extend_snake(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()

        segment.goto(position)
        self.my_snake.append(segment)

    def incre_snake(self):
        self.extend_snake(self.my_snake[-1].position())

    def move(self):

        for i in range(len(self.my_snake) - 1, 0, -1):
            new_x = self.my_snake[i - 1].xcor()
            new_y = self.my_snake[i - 1].ycor()
            self.my_snake[i].goto(x=new_x, y=new_y)

        self.head.forward(DISTANCE)

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
