import turtle as john

john.bgcolor("black")
john.speed(0)

colors = ["red", "blue", "green"]

john.penup()
john.forward(100)
john.pendown()

for x in range(360):
  john.color(colors[x % 3])
  john.forward(800)
  john.backward(800)
  john.right(1)

john.hideturtle()

john.mainloop()