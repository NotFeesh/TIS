import turtle

t1 = turtle.Turtle();

def main():
  t1.speed(0)
  turtle.bgcolor("black")

  spirograph()

  t1.hideturtle()

  turtle.mainloop()

def spirograph():
  colors = ["red", "blue", "purple", "cyan"]

  for x in range(360):
    t1.color(colors[x % len(colors)])
    t1.forward(1)
    t1.right(1)
    t1.forward(800)
    t1.backward(800)

if __name__ == "__main__":
  main()