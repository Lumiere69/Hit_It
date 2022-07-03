from turtle import *
from random import randint

class sprite(Turtle):
  def __init__(self, x, y, step=10, shape='circle', color='black'):
      super().__init__()
      self.penup()
      self.speed(0)
      self.goto(x, y)
      self.color(color)
      self.shape(shape)
      self.step = step
      self.points = 0
  def lose(self):
    self.penup()
    self.goto(-110,0)
    self.pensize(3)
    self.pendown()
    self.speed(15)
    self.color('red')
    self.left(90)
    self.forward(100)
    self.penup()
    self.goto(-30, 0)
    self.pendown()
    self.forward(100)
    self.left(90)
    self.forward(50)
    self.left(90)
    self.forward(100)
    self.left(90)
    self.forward(50)
    self.left(90)
    self.penup()
    self.goto(-5, 0)
    self.pendown()
    self.right(90)
    self.forward(50)
    self.left(90)
    self.forward(50)
    self.left(90)
    self.forward(50)
    self.right(90)
    self.forward(50)
    self.right(90)
    self.forward(50)
    self.penup()
    self.goto(65,0)
    self.pendown()
    self.forward(50)
    self.backward(50)
    self.left(90)
    self.forward(50)
    self.right(90)
    self.forward(50)
    self.backward(50)
    self.left(90)
    self.forward(50)
    self.right(90)
    self.forward(50)
    self.backward(50)

  def dance(self):
      self.speed(150)
      self.left(randint(0,90))
      a = 0
      while a < 8:
          self.penup()
          self.goto(0,0)
          self.pendown()
          b = 1
          while b < 32:
              self.forward(b)
              self.left(b/2+5)
              b += 1
          a += 1
      self.goto(0,0)
  
  def move_up(self):
      self.goto(self.xcor(), self.ycor() + self.step)
  def move_down(self):
      self.goto(self.xcor(), self.ycor() - self.step)
  def move_left(self):
      self.goto(self.xcor() - self.step, self.ycor())
  def move_right(self):
      self.goto(self.xcor() + self.step, self.ycor())

  def is_collide(self, sprite):
      dist = self.distance(sprite.xcor(), sprite.ycor())
      if dist < 30:
          return True
      else:
          return False
  def set_move(self, x_start, y_start, x_end, y_end):
      self.x_start = x_start
      self.y_start = y_start
      self.x_end = x_end
      self.y_end = y_end
      self.goto(x_start, y_start)
      self.setheading(self.towards(x_end, y_end))
  
  def make_step(self):
      self.forward(self.step)
      if self.distance(self.x_end, self.y_end) < self.step:
          self.set_move(self.x_start, self.y_start, self.x_end, self.y_end) 

s_width = 200
s_height = 180
player = sprite(0, -130, 10, 'circle', 'orange')
enemy1 = sprite(-s_width, 0, 30, 'square', 'red')
enemy1.set_move(-200, 0, 200, 0)
enemy2 = sprite(s_width, 70, 30, 'square', 'red')
enemy2.set_move(200, 70, -200, 70)
enemy3 = sprite(s_width, 70, 30, 'square', 'red')
enemy3.set_move(200, -70, -200, -70)
goal = sprite(0, 120, 20, 'triangle', 'green')

scr = player.getscreen()
scr.listen()
scr.onkey(player.move_up, 'Up')
scr.onkey(player.move_left, 'Left')
scr.onkey(player.move_right, 'Right')
scr.onkey(player.move_down, 'Down')

total_score = 0

while total_score < 3:
    enemy1.make_step()
    enemy2.make_step()
    enemy3.make_step()
    if player.is_collide(goal):
        player.goto(0, -130)
        total_score += 1
    if total_score == 3:
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        goal.hideturtle()
        player.hideturtle()
        player.dance()
    if player.is_collide(enemy1) or player.is_collide(enemy2):
        enemy1.hideturtle()
        enemy2.hideturtle()
        enemy3.hideturtle()
        goal.hideturtle()
        player.hideturtle()
        player.lose()
        break

enemy1.hideturtle()
enemy2.hideturtle()
enemy3.hideturtle()