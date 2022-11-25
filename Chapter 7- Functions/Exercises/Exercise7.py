def max_num():
  a = int(input())
  b = int(input())
  c = int(input())
  if a>b and a>c:
    print (str(a) + " is the largest number.")
  elif b>a and b>c:
    print (str(b) + " is the largest number.")
  else:
    print (str(c) + " is the largest number.")
max_num()