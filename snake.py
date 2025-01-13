from turtle import Turtle
starting_positions = [(0, 0), (0,  -20), (0, -40)]
move_distance = 20
class Snake:

       def __init__(self):
              self.segments = []
              self.create_snake()
              self.head = self.segments[0]

       def create_snake(self):
              for positions in starting_positions:
                     new_segment = Turtle(shape="square")
                     new_segment.penup()
                     new_segment.color("white")
                     new_segment.goto(positions)
                     self.segments.append(new_segment)

       def increase_size(self):
              new_positon = self.segments[-1].position()
              new_segment = Turtle(shape="square")
              new_segment.penup()
              new_segment.color("green")
              new_segment.goto(new_positon)
              self.segments.append(new_segment)

       def restart(self):
              for segment in self.segments:
                     segment.goto(1000, 1000)
              self.segments.clear()
              self.create_snake()
              self.head = self.segments[0]
       def move(self):
              for i in range(len(self.segments) - 1, 0, -1):
                     new_x = self.segments[i - 1].xcor()
                     new_y = self.segments[i - 1].ycor()
                     self.segments[i].goto(new_x, new_y)
              self.segments[0].forward(move_distance)

       def up(self):
              if self.head.setheading != 2700:
                     self.head.setheading(90)

       def down(self):
              if self.head.setheading != 90:
                     self.head.setheading(270)

       def left(self):
              if self.head.setheading != 0:
                     self.head.setheading(180)

       def right(self):
              if self.head.setheading != 180:
                     self.head.setheading(0)
