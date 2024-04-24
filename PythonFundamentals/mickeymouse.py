import turtle as jane

jane.speed(0)

def mickey_mouse(size, head_color, ear_color):
  jane.fillcolor(head_color)

  jane.begin_fill()
  jane.circle(-size, 360)
  jane.end_fill()
  jane.circle(-size, 45)

  jane.fillcolor(ear_color)

  jane.begin_fill()
  jane.circle(size / 2)
  jane.end_fill()

  jane.circle(-size, 270)

  jane.begin_fill()
  jane.circle(size / 2)
  jane.end_fill()


size = int(input("What size mickey mouse would you like?"))
head_color = input("What color head would you like?")
ear_color = input("What color ear would you like?")

mickey_mouse(size, head_color, ear_color)

jane.mainloop()