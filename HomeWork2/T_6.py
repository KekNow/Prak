from collections import deque

class Graph:
    def __init__(self):  #Конструктор
        self.G = {}  #Словарь - граф

        N = int(input("Число рёбер: "))  # Вводим количество рёбер
        print("Рёбра (начало, конец, вес): ")
        for i in range(N):
            a0, b0, weight = map(int, input().split())  # Вводим 3 числа - ребро графа и вес, N штук
            for a, b in (a0, b0), (b0, a0):
                if a in self.G:
                    self.G[a][b] = weight
                else:
                    self.G[a] = {b: weight}
        self.dist = {}  #Словарь - расстояние до каждой вершины

    def findways(self, noneStart):  # Функция обхода в ширину с весами
        self.dist[noneStart] = 0  # Составление таблицы расстояний dist
        queue = deque([noneStart])
        while queue:
            tmp = queue.popleft()
            for neighbour in self.G[tmp]:
                if (neighbour not in self.dist) or (self.dist[tmp] + self.G[tmp][neighbour] < self.dist[neighbour]):
                    self.dist[neighbour] = self.dist[tmp] + self.G[tmp][neighbour]
                    queue.append(neighbour)

    def time(self, start):
        self.findways(start)
        max = 0
        for i in self.G:
            if i not in self.dist:
                print(-1)
                break
            elif self.dist[i] > max:
                max = self.dist[i]
        else:
            print("Время распространения: ", max)

G = Graph()
a = int(input("Введите точку старта: "))
G.time(a)
