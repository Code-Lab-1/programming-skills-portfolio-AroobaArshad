Guests = ["Muhammad Ali", "Bill Gates", "Margaret Thatcher", "Martin Luther King Jr."]

msg = Guests[0] + ", I invite you to dinner."
print (msg)
msg = Guests[1] + ", I invite you to dinner."
print (msg)
msg = Guests[2] + ", I invite you to dinner."
print (msg)
msg = Guests[3] + ", I invite you to dinner."
print (msg)

print ('\n' + Guests[3] + " can't make it to dinner!")

#Let's invite someone else
del(Guests[3])
Guests.insert(3, "Nelson Mandela")

#Sending invitations again
msg = (Guests[0]) + ", I invite you to dinner."
print ('\n' + msg)
msg = Guests[1] + ", I invite you to dinner."
print (msg)
msg = Guests[2] + ", I invite you to dinner."
print (msg)
msg = Guests[3] + ", I invite you to dinner."
print (msg)