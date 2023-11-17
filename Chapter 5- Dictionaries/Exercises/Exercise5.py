Pets = []

Pet = {"Name":"Cookie",
       "Animal type":"Cat",
       "Owner":"Rosanna"}
Pets.append(Pet)

Pet = {"Name":"Cassie",
       "Animal type":"Parrot",
       "Owner":"Amy"}
Pets.append(Pet)

Pet = {"Name":"Pesto",
       "Animal type":"Dog",
       "Owner":"Harry"}
Pets.append(Pet)

Pet = {"Name":"Bruno",
       "Animal type":"Turtle",
       "Owner":"Louise"}
Pets.append(Pet)

for Pet in Pets:
  print(f"\nHere's what I know about {Pet['Name'].title()}:")
  for key, value in Pet.items():
    print (f" {key}: {value}")