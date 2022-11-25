Guests = ["Muhammad Ali", "Bill Gates", "Margaret Thatcher", "Martin Luther King Jr."]

print (Guests[0] + ", I invite you to dinner.")
print (Guests[1] + ", I invite you to dinner.")
print (Guests[2] + ", I invite you to dinner.")
print (Guests[3] + ", I invite you to dinner.")

print ('\n' + Guests[3] + " can't make it to dinner!")

#Let's invite someone else
del(Guests[3])
Guests.insert(3, "Nelson Mandela")

#Sending invitations again
print ('\n' + Guests[0] + ", I invite you to dinner.")
print (Guests[1] + ", I invite you to dinner.")
print (Guests[2] + ", I invite you to dinner.")
print (Guests[3] + ", I invite you to dinner.")

print ("\nSorry, we can only invite two people.")

print ('\n' + "Sorry " + Guests[0] + " there is no room at the table.")
Guests.pop(0)
print ("Sorry " + Guests[0] + " there is no room at the table.")
Guests.pop(0)

#Inviting remaining people
print('\n' + Guests[0] + ", I invite you to dinner.")
print(Guests[1] + ", I invite you to dinner.")

del(Guests[0])
del(Guests[0])
print(Guests)