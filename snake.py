import turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POINTS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.create_Snake()
        self.head = self.segments[0]

    def create_Snake(self):
        for i in STARTING_POINTS:
            self.add_segment(i)

    #  this fuction add segments in snake .....
    def add_segment(self, i):
        tim = Turtle("square")
        tim.color("white")
        tim.penup()
        tim.goto(i)
        self.segments.append(tim)

    # extend the snake when it contact with food
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)

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
