**READ ME FOR TURTLE-DRAWING.py**

import turtle: This line imports the Turtle module, which allows us to create graphics using a virtual turtle.
turtle.bgcolor("black"): This line sets the background color of the drawing window to black.
t = turtle.Turtle(): This line creates a new Turtle object called `t`, which we'll use to draw on the screen.
colors = ["red", "dark red"]: This line creates a list containing two colors: red and dark red. These colors will alternate as the turtle draws the spiral.
for number in range(400): This line starts a loop that will repeat 400 times. The variable `number` will take on values from 0 to 399.
t.forward(number+20): Inside the loop, this line makes the turtle move forward by a distance that depends on the current value of `number`. The distance increases as `number` increases due to `number + 20`.
t.right(89): This line makes the turtle turn right by an angle of 89 degrees after moving forward. This creates the spiral pattern.
t.pencolor(colors[number%2]): This line sets the pen color of the turtle. It uses the `%` operator to alternate between the two colors in the `colors` list based on whether `number` is even or odd. 

CONTIBUTOR:
VANSH
