import turtle

screen = turtle.Screen()
screen.bgcolor("darkgreen")

bird = turtle.Turtle()
bird.speed(1)
bird.pensize(2)

def draw_circle(t, radius, x, y, color):
    t.penup()
    t.goto(x, y - radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

def draw_triangle(t, points, color):
    t.penup()
    t.goto(points[0])
    t.pendown()
    t.color(color)
    t.begin_fill()
    for point in points[1:] + [points[0]]:
        t.goto(point)
    t.end_fill()

def draw_body():
    draw_circle(bird, 70, 0, 0, "lightblue")

def draw_eyes():
    draw_circle(bird, 10, -25, 50, "white")
    draw_circle(bird, 10, 25, 50, "white")
    draw_circle(bird, 4, -25, 50, "black")
    draw_circle(bird, 4, 25, 50, "black")

def draw_beak():
    beak_points = [(-10, 35), (0, 15), (10, 35)]
    draw_triangle(bird, beak_points, "orange")

def draw_wings():
    draw_circle(bird, 30, -70, 0, "darkgray")
    draw_circle(bird, 30, 70, 0, "darkgray")

def draw_feet():
    bird.color("orange")
    for x in [-20, 20]:
        bird.penup()
        bird.goto(x, -70)
        bird.setheading(-90)
        bird.pendown()
        bird.forward(20)
        for angle in [-30, 30]:
            bird.penup()
            bird.goto(x, -90)
            bird.setheading(angle - 90)
            bird.pendown()
            bird.forward(10)

def draw_feathers():
    bird.color("black")
    for angle in [120, 90, 60]:
        bird.penup()
        bird.goto(0, 70)
        bird.setheading(angle)
        bird.pendown()
        bird.forward(15)

draw_body()
draw_eyes()
draw_beak()
draw_wings()
draw_feet()
draw_feathers()
bird.hideturtle()
screen.mainloop()
