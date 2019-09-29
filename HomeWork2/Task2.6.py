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

dist = {}

def findways(noneStart):  #Функция обхода в ширину с весами
    dist[noneStart] = 0  #Составление таблицы расстояний dist
    queue = deque([noneStart])
    while queue:
        tmp = queue.popleft()
        for neighbour in G[tmp]:
            if (neighbour not in dist) or (dist[tmp] + G[tmp][neighbour] < dist[neighbour]):
                dist[neighbour] = dist[tmp] + G[tmp][neighbour]
                queue.append(neighbour)

a = int(input("Введите точку старта: "))
findways(a)
max = 0
for i in G:
    if i not in dist:
        print(-1)
        break
    elif dist[i] > max:
        max = dist[i]
else:
    print("Время распространения: ", max)