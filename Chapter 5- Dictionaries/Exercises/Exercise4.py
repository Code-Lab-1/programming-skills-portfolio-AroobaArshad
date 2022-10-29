Rivers = {
    "Nile":"Egypt",
    "Euphrates":"Iraq",
    "Indus":"Pakistan",
    }

for river, country in Rivers.items():
  print (f"The {river.title()} flows through {country.title()}.")

print ("\nRivers:")
for river in Rivers.keys():
  print ("-" + river)

print ("\nCountries:")
for country in Rivers.values():
  print ("-" + country)