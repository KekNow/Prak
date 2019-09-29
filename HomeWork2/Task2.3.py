m = [[' '], ["OO"], ['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
x = input()
a = int(x[0])
b = int(x[1])
for i in m[a]:
    for j in m[b]:
        print(i,j, sep = '', end = ' ')