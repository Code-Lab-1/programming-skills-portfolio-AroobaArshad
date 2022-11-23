Your_age = "\nWhat is your age?"
Your_age += "\nPlease enter 'Quit' when you are done: "

while True:
  Age = input(Your_age)
  if Age == 'Quit':
    break
  Age = int(Age)
  if Age < 3:
    print ("Your ticket is free!")
  elif Age >= 3 and Age <= 12:
    print ("Your ticket price is $10.")
  else:
    print ("Your ticket price is $15.")