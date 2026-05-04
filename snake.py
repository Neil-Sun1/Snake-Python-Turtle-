from turtle import *
import random

def generate_color():
    return f"#{random.randint(0, 0xFFFFFF):06x}"

def playing_area():
    pen = Turtle()
    pen.ht()
    pen.speed(0)
    pen.color('light blue')
    pen.begin_fill()
    pen.goto(-240,240)
    pen.goto(240,240)
    pen.goto(240,-240)
    pen.goto(-240,-240)
    pen.goto(-240,240)
    pen.end_fill()
    
class Head(Turtle):
  def __init__(self, screen, body):
    super().__init__()
    pass

  def up(self):
    pass

  def down(self):
    pass

  def left(self):
    pass

  def right(self):
    pass

  def move(self):
    pass
    
  def die(self):
    pass


class Segment(Turtle):
  def __init__(self, other):
    super().__init__()
    pass

  def move(self, other):
    pass

class Apple(Turtle):
  def __init__(self):
    super().__init__()
    pass

  def relocate(self):
    pass

screen = Screen()
screen.bgcolor("black")
screen.setup(520,520)
# Key Binding. Connects key presses and mouse clicks with function calls
screen.listen()

body = []


screen.exitonclick()






screen.exitonclick()