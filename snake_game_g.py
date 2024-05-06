import turtle
import time
import random
delay = 0.1
score = 0
high_score = 0
# Function to start the game
def start_game():
  start_menu.clear()
  wn.update()
  wn.listen()
# Start Menu
start_menu = turtle.Screen()
start_menu.title("Snake Game - Start Menu")
start_menu.bgcolor("blue")
start_menu.setup(width=800, height=600)
start_menu.tracer(0)

  # Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 200)
title.write("Snake Game", align="center", font=("candara", 36, "bold"))

  # Start Button
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("white")
start_button.penup()
start_button.hideturtle()
start_button.goto(0, 0)
start_button.shape("square")
start_button.shapesize(stretch_wid=2, stretch_len=8)
start_button.write("Start", align="center", font=("candara", 24, "bold"))

  # Bind the start_game function to the button click event
start_button.onclick(start_game)

start_menu.mainloop()

  # Main game window
wn = turtle.Screen()
wn.title("Snake Game")
wn.bgcolor("blue")
wn.setup(width=800, height=600)
wn.tracer(0)

border = turtle.Turtle()
border.hideturtle()
border.penup()
border.goto(-390, -290)
border.pendown()
border.pensize(3)
for _ in range(4):
      border.forward(780)
      border.left(90)


score_display_left = turtle.Turtle()
score_display_left.speed(0)
score_display_left.color("white")
score_display_left.penup()
score_display_left.hideturtle()
score_display_left.goto(-340, 260)
score_display_left.write("Score : 0", align="left", font=("candara", 24, "bold"))


score_display_right = turtle.Turtle()
score_display_right.speed(0)
score_display_right.color("white")
score_display_right.penup()
score_display_right.hideturtle()
score_display_right.goto(200, 260)
score_display_right.write("High Score : 0", align="left", font=("candara", 24, "bold"))


head = turtle.Turtle()
head.shape("square")
head.color("white")
head.penup()
head.goto(0, 0)
head.direction = "Stop"


food = turtle.Turtle()
colors = random.choice(['red', 'green', 'black'])
shapes = random.choice(['square', 'triangle', 'circle'])
food.speed(0)
food.shape(shapes)
food.color(colors)
food.penup()
food.goto(0, 100)

def group():
      if head.direction != "down":
          head.direction = "up"

def godown():
      if head.direction != "up":
          head.direction = "down"

def goleft():
      if head.direction != "right":
          head.direction = "left"

def goright():
      if head.direction != "left":
          head.direction = "right"

def move():
  if head.direction == "up":
      y = head.ycor()
      if y > 270:
          head.sety(-270)
      else:
          head.sety(y + 20)
  elif head.direction == "down":
      y = head.ycor()
      if y < -270:
          head.sety(270)
      else:
          head.sety(y - 20)
  elif head.direction == "left":
      x = head.xcor()
      if x < -390:
          head.setx(390)
      else:
          head.setx(x - 20)
  elif head.direction == "right":
      x = head.xcor()
      if x > 390:
          head.setx(-390)
      else:
          head.setx(x + 20)

wn.listen()
wn.onkeypress(group, "w")
wn.onkeypress(godown, "s")
wn.onkeypress(goleft, "a")
wn.onkeypress(goright, "d")

segments = []

while True:
      wn.update()


      if head.xcor() > 390:
          head.setx(-390)
      elif head.xcor() < -390:
          head.setx(390)
      elif head.ycor() > 290:
          head.sety(-290)
      elif head.ycor() < -290:
          head.sety(290)


      if head.distance(food) < 20:
          x = random.randint(-370, 370)
          y = random.randint(-270, 270)
          food.goto(x, y)


          new_segment = turtle.Turtle()
          new_segment.speed(0)
          new_segment.shape("square")
          new_segment.color("orange")
          new_segment.penup()
          segments.append(new_segment)


          score += 10
          if score > high_score:
              high_score = score


          score_display_left.clear()
          score_display_left.write("Score : {}".format(score), align="left", font=("candara", 24, "bold"))

          score_display_right.clear()
          score_display_right.write("High Score : {}".format(high_score), align="left", font=("candara", 24, "bold"))


      for index in range(len(segments) - 1, 0, -1):
          x = segments[index - 1].xcor()
          y = segments[index - 1].ycor()
          segments[index].goto(x, y)

      if len(segments) > 0:
          x = head.xcor()
          y = head.ycor()
          segments[0].goto(x, y)

      move()


      for segment in segments:
          if segment.distance(head) < 20:
              time.sleep(1)
              head.goto(0, 0)
              head.direction = "Stop"
              for segment in segments:
                  segment.goto(1000, 1000)
              segments.clear()
              score = 0


              score_display_left.clear()
              score_display_left.write("Score : {}".format(score), align="left", font=("candara", 24, "bold"))


      time.sleep(delay)

  # Start Menu
start_menu = turtle.Screen()
start_menu.title("Snake Game - Start Menu")
start_menu.bgcolor("blue")
start_menu.setup(width=800, height=600)
start_menu.tracer(0)

  # Title
title = turtle.Turtle()
title.speed(0)
title.color("white")
title.penup()
title.hideturtle()
title.goto(0, 200)
title.write("Snake Game", align="center", font=("candara", 36, "bold"))

  # Start Button
start_button = turtle.Turtle()
start_button.speed(0)
start_button.color("white")
start_button.penup()
start_button.hideturtle()
start_button.goto(0, 0)
start_button.shape("square")
start_button.shapesize(stretch_wid=2, stretch_len=8)
start_button.write("Start", align="center", font=("candara", 24, "bold"))

def start_game(x, y):
      start_menu.clear()
      wn.update()
      wn.mainloop()

start_button.onclick(start_game)

start_menu.mainloop()

