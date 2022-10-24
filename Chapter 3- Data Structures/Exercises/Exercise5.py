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