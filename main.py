from turtle import *
from random import randint

screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0)

def playing_area():
    t = Turtle()
    t.speed(0)
    t.ht()
    t.pu()
    t.goto(-250, 250)
    t.color('light blue')
    t.pd()
    t.begin_fill()
    for i in range(4):
        t.forward(500)
        t.right(90)
    t.end_fill()

class Head(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.pu()
        self.speed(0)
        self.direction = "stop"

    def move(self):
        if self.direction == "up":
            self.sety(self.ycor() + 20)
        elif self.direction == "down":
            self.sety(self.ycor() - 20)
        elif self.direction == "left":
            self.setx(self.xcor() - 20)
        elif self.direction == "right":
            self.setx(self.xcor() + 20)

    def go_up(self):
        if self.direction != "down":
            self.direction = "up"
            
    def go_down(self):
        if self.direction != "up":
            self.direction = "down"
            
    def go_left(self):
        if self.direction != "right":
            self.direction = "left"
            
    def go_right(self):
        if self.direction != "left":
            self.direction = "right"

class Segment(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.pu()
        self.speed(0)
        self.goto(x_pos, y_pos)

class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.pu()
        self.speed(0)
        self.relocate()

    def relocate(self):
        x = randint(-11, 11) * 20
        y = randint(-11, 11) * 20
        self.goto(x, y)

playing_area()
head = Head()

body = []
body.append(head)

apple = Apple()

screen.listen()
screen.onkey(head.go_up, "Up")
screen.onkey(head.go_down, "Down")
screen.onkey(head.go_left, "Left")
screen.onkey(head.go_right, "Right")

def game_loop():
    if head.xcor() <= -250 or head.xcor() >= 250 or head.ycor() <= -250 or head.ycor() >= 250:
        return

    if head.direction != "stop":
        for segment in body[1:]:
            if head.distance(segment) < 15:
                return

    old_positions = []
    for b in body:
        old_positions.append((b.xcor(), b.ycor()))

    head.move()

    if head.xcor() <= -250 or head.xcor() >= 250 or head.ycor() <= -250 or head.ycor() >= 250:
        return

    for index in range(1, len(body)):
        body[index].goto(old_positions[index - 1][0], old_positions[index - 1][1])

    if head.distance(apple) < 20:
        apple.relocate()
        tail_pos = old_positions[-1]
        new_segment = Segment(tail_pos[0], tail_pos[1])
        body.append(new_segment)
    
    screen.update()
    screen.ontimer(game_loop, 100)

screen.update()
game_loop()
screen.exitonclick()
