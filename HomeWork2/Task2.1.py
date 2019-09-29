s = "12211221"
max = 0
for i in range(1, len(s)//2 + 1):
    x = s[0:i]
    k = 1
    while x == s[k*i:(k+1)*i]:
        k += 1
    else:
        if k*i == len(s) and max < k:
            max = k
print(max)