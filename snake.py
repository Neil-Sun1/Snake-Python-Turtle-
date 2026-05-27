from turtle import *
from random import randint


screen = Screen()
screen.setup(600, 600)
screen.bgcolor('black')
screen.title("Snake Game")
screen.tracer(0) 

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
    def __init__(self, body_list):
        super().__init__()
        self.shape("square")
        self.color("green")
        self.pu()
        self.speed(0)
        last_element = body_list[-1]
        self.goto(last_element.xcor(), last_element.ycor())

class Apple(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.pu()
        self.speed(0)
        self.relocate()

    def relocate(self):
        x = randint(-14, 14) * 20
        y = randint(-14, 14) * 20
        self.goto(x, y)

head = Head()
apple = Apple()


body = []
body.append(head)
body.append(Segment(body))
body.append(Segment(body))


screen.listen()
screen.onkey(head.go_up, "Up")
screen.onkey(head.go_down, "Down")
screen.onkey(head.go_left, "Left")
screen.onkey(head.go_right, "Right")
def game_loop():
    for index in range(len(body) - 1, 0, -1):
        front_segment = body[index - 1]
        body[index].goto(front_segment.xcor(), front_segment.ycor())
    head.move()
    if head.distance(apple) < 20:
        apple.relocate()
        new_segment = Segment(body)
        body.append(new_segment)
    
    screen.update()
    screen.ontimer(game_loop,100)
game_loop()
screen.mainloop()