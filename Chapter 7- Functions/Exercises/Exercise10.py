def even_odd():
  a = int(input())
  b = int(input())
  c = int(input())
  d = int(input())
  e = int(input())
  nums = [a,b,c,d,e]
  even = []
  odd = []
  for i in nums:
    if i%2==0:
      even.append(i)
    else:
      odd.append(i)
  print ("Even list: ", even)
  print ("Odd list: ", odd)
even_odd()