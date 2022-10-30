sandwich_orders = ["Grilled sandwich", "Pastrami sandwich", "Steak sandwich", "Pastrami sandwich",
                   "Egg Salad sandwich", "Pastrami sandwich", "Chicken sandwich"]
finished_sandwiches = []

print ("Sorry, we've run out of pastrami.")
while 'Pastrami sandwich' in sandwich_orders:
  sandwich_orders.remove("Pastrami sandwich")

print ("\n")
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print ("I'm making your " + sandwich + ".")
    finished_sandwiches.append(sandwich)

print ("\n")
for sandwich in finished_sandwiches:
  print ("I made your " + sandwich)