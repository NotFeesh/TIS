import turtle as john

john.bgcolor("black")
john.speed(0)

colors = ["red", "blue", "green"]

for x in range(360):
  john.color(colors[x % 3])
  john.forward(700)
  john.backward(700)
  john.right(1)

john.hideturtle()

john.mainloop()