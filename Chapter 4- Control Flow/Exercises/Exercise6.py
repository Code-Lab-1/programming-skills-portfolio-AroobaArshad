marks= int(input())
if marks>=80 and marks<=100:
  print ("Your grade is A+")
elif marks>=70 and marks<=80:
  print("Your grade is A")
elif marks>=60 and marks<=70:
  print("Your grade is B")
elif marks>40:
  print("You have passed")
else:
  print("You have failed")