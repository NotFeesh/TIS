import turtle

turtle.color("red")
turtle.bgcolor("blue")
turtle.fillcolor("orange")

turtle.begin_fill()
for x in range(4):
  turtle.forward(300)
  turtle.right(90)
turtle.end_fill()

turtle.mainloop()