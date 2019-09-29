from collections import deque

N = int(input("Число рёбер: ")) #Вводим количество рёбер
G = {}
print("Рёбра (начало, конец, вес): ")
for i in range(N):
    a0, b0, weight = map(int, input().split()) #Вводим пары чисел - рёбра графа, N штук
    for a, b in (a0, b0), (b0, a0):
        if a in G:
            G[a][b] = weight
        else:
            G[a] = {b: weight}

dist = [None] * len(G)

def search(S, E, ans):
    for neighbour in G[E]:
        if dist[E] - G[neighbour][E] == dist[neighbour]:
            if dist[neighbour] != 0:
                search(S, neighbour, ans)
                ans.append(neighbour)

def findway(noneStart, noneEnd):  #Функция обхода в ширину с весами
    dist[noneStart] = 0  #Составление таблицы расстояний dist
    queue = deque([noneStart])
    while queue:
        tmp = queue.popleft()
        for neighbour in G[tmp]:
            if dist[neighbour] == None or (dist[tmp] + G[tmp][neighbour] < dist[neighbour]):
                dist[neighbour] = dist[tmp] + G[tmp][neighbour]
                queue.append(neighbour)
    ans = [noneStart]  #Поиск кратчайшего пути по таблице dist
    search(noneStart, noneEnd, ans)
    ans.append(noneEnd)  #Вывод полученного пути
    print("Путь от старта до финиша: ", ans)

a, b = map(int, input("Введите точки старта и финиша: ").split())
findway(a, b)
