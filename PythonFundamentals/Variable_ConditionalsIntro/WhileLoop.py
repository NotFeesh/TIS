import turtle

while int(goto_x) > 0:
  goto_x = input("How far do you want to go?")

turtle.forward(int(goto_x))

turtle.mainloop()