Pizza_topping = "\nWhat topping do you want for your pizza?"
Pizza_topping += "\nEnter 'quit' when you are done: "

while True:
  Topping = input(Pizza_topping)
  if Topping != 'quit':
    print ("I'll add " + Topping + " to your pizza.")
  else:
    break