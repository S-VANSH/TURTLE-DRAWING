import turtle
turtle.bgcolor("black")
t = turtle.Turtle()
colors = ["red", "dark red"]
for number in range(400):
    t.speed(30)
    t.forward(number+50)
    t.right(89)
    t.pencolor(colors[number%2])
