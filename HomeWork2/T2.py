d = {}
s = str(input("Введите текст (чтобы завершить ввод - ещё раз Enter): "))
while len(s) > 0:
    s = s.split()
    for i in s:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    s = str(input())

max = 0
for i in d:
    if max < d[i]:
        max = d[i]
        slovo = i
        kol = True
    elif max == d[i]:
        kol = False

if kol:
    print(slovo)
else:
    print("--")