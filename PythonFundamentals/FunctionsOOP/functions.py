import turtle

def circle():
  for x in range(360):
    turtle.forward(1)
    turtle.right(1)

def square(side_length):
  for x in range(4):
    turtle.forward(side_length)
    turtle.right(90)

def main():
  circle()
  square(400)
  
if __name__ == "__main__":
  main()


turtle.mainloop()