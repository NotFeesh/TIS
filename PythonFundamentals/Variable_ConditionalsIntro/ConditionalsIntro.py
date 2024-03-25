name = "Kaiyo"
age = 16
favorite_color = "chartreuse"

inputted_name = input("Please enter your name: ")

if inputted_name == name:
  print("Hello " + name + "!")
else:
  print("You are not " + name + ".")

inputted_age = input("Please enter your age: ")

if int(inputted_age) == age:
  print("You are the same age as " + name)
elif int(inputted_age) < age:
  print("You are younger than " + name)
elif int(inputted_age) > age:
  print("You are older than " + name)