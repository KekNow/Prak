from collections import deque

def dfs(vertex, G, used):  #Функция обхода в глубину
    print(vertex, end=' ')
    used.add(vertex)
    for neighbour in G[vertex]:
        if neighbour not in used:
            dfs(neighbour, G, used)

def bfs(vertex, G):  #Функция обхода в ширину
    dist = [None] * len(G)
    dist[vertex] = 0
    queue = deque([vertex])
    while queue:
        tmp = queue.popleft()
        print(tmp, end=' ')
        for neighbour in G[tmp]:
            if dist[neighbour] == None:
                dist[neighbour] = dist[tmp] + 1
                queue.append(neighbour)
    print()

N = int(input()) #Вводим количество рёбер
G = {}
for i in range(N):
    a0, b0 = map(int, input().split()) #Вводим пары чисел - рёбра графа, N штук
    for a, b in (a0, b0), (b0, a0):
        if a in G:
            G[a].add(b)
        else:
            G[a] = {b}

used = set()
dfs(0, G, used)
print()
bfs(0, G)