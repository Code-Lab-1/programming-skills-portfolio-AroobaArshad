sandwich_orders = ["Grilled sandwich", "Steak sandwich", "Egg Salad sandwich", "Chicken sandwich"]
finished_sandwiches = []

while sandwich_orders:
  sandwich = sandwich_orders.pop()
  print ("I'm making your " + sandwich + ".")
  finished_sandwiches.append(sandwich)

print ("\n")
for sandwich in finished_sandwiches:
  print ("I made your " + sandwich)