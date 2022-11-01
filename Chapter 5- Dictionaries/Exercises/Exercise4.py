Rivers = {
    "Nile":"Egypt",
    "Euphrates":"Iraq",
    "Indus":"Pakistan",
    }

for river, country in Rivers.items():
  print ("The " + river + " flows through " + country + ".")

print ("\nRivers:")
for river in Rivers.keys():
  print ("-" + river)

print ("\nCountries:")
for country in Rivers.values():
  print ("-" + country)