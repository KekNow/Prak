d = {}
s = str(input())
while len(s) > 0:
    s = s.split()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    s = str(input())

max = 1
for i in d:
    if max < d[i]:
        max = d[i]
        kol = True
    elif max == d[i]:
        kol = False

if kol:
    print(max)
else:
    print("--")