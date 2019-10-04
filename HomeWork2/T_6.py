from collections import deque

class Graph:
    def __init__(self):  #Конструктор
        self.G = {}  #Словарь - граф

        print("Введите рёбра графа (в формате [[a1,a2,weidth1],[b1,b2,weidth2],..]):")
        ribs = eval(input())
        for rib in ribs:
            for a, b in (rib[0], rib[1]), (rib[1], rib[0]):
                if a in self.G:
                    self.G[a][b] = rib[2]
                else:
                    self.G[a] = {b: rib[2]}

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
