Numbers = [23, 32, 67, 76, 90, 56, 51]
Even_Num = []
Odd_Num = []
for i in Numbers:
    if i%2 == 0:
        Even_Num.append(i)
    else:
        Odd_Num.append(i)

print ("Even Numbers:", Even_Num)
print ("Odd Numbers:", Odd_Num)