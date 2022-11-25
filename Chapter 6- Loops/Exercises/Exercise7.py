num = []
for x in range(500, 1000):
    if x%2==0 and x%5==0:
        num.append(str(x))

print(','.join(num))