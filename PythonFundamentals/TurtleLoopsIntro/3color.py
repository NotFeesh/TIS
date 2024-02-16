import turtle

#intro to color
turtle.color("red")
#teach blue, brown, cyan, gold, gray, green, orange, pink, purple, red, yellow, violet
#full color list -> https://cs111.wellesley.edu/labs/lab02/colors
turtle.forward(300)
turtle.right(90)
turtle.color("blue")
turtle.forward(300)

turtle.bgcolor("orange")

turtle.clearscreen()

turtle.begin_fill()

turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)
turtle.right(90)
turtle.forward(300)

turtle.fillcolor("red")
# fillcolor can be placed right before the end_fill()
turtle.end_fill()

turtle.mainloop()
