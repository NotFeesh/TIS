import turtle

def circle(percent_drawn, radius):
  for x in range(int(360 * percent_drawn * 0.01)):
    turtle.forward((6.28 * radius) / 360)
    turtle.right(1)

def square(side_length):
  for x in range(4):
    turtle.forward(side_length)
    turtle.right(90)

def main():
  circle(50, 100)
  turtle.right(90)
  turtle.forward(100)
  
if __name__ == "__main__":
  main()


turtle.mainloop()