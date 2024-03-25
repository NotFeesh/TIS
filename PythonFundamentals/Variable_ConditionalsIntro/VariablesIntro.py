name = "Kaiyo"
age = 16
favorite_color = "chartreuse"

import turtle

turtle.begin_fill()
for x in range(4):
  turtle.forward(300)
  turtle.right(90)

turtle.fillcolor(favorite_color)
turtle.end_fill()

turtle.mainloop()