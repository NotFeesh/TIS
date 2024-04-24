import turtle as john

john.speed(0)
john.bgcolor("midnightblue")

colors = ["LightSkyBlue", "aquamarine", "LightBlue", "DeepSkyBlue", "DodgerBlue"]

#var = colors[1]

for x in range(360):
  john.color(colors[x % len(colors)])
  john.forward(800)
  john.backward(800)
  john.right(1)

john.mainloop()
  