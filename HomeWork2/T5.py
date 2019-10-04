from collections import deque

class Graph:
    def __init__(self):  #Конструктор
        self.G = {}  # Словарь - граф

        print("Введите рёбра графа (в формате [[a1,a2,weidth1],[b1,b2,weidth2],..]):")
        ribs = eval(input())
        for rib in ribs:
            for a, b in (rib[0], rib[1]), (rib[1], rib[0]):
                if a in self.G:
                    self.G[a][b] = rib[2]
                else:
                    self.G[a] = {b: rib[2]}

        self.dist = {}  #Словарь - расстояние до каждой вершины

    def search(self, S, E, ans):
        for neighbour in self.G[E]:
            if self.dist[E] - self.G[neighbour][E] == self.dist[neighbour]:
                if self.dist[neighbour] != 0:
                    self.search(S, neighbour, ans)
                    ans.append(neighbour)

    def findway(self, noneStart, noneEnd):  # Функция обхода в ширину с весами
        self.dist[noneStart] = 0  # Составление таблицы расстояний dist
        queue = deque([noneStart])
        while queue:
            tmp = queue.popleft()
            for neighbour in self.G[tmp]:
                if (neighbour not in self.dist) or (self.dist[tmp] + self.G[tmp][neighbour] < self.dist[neighbour]):
                    self.dist[neighbour] = self.dist[tmp] + self.G[tmp][neighbour]
                    queue.append(neighbour)
        ans = [noneStart]  # Поиск кратчайшего пути по таблице dist
        self.search(noneStart, noneEnd, ans)
        ans.append(noneEnd)  # Вывод полученного пути
        print("Кратчайший путь: ", ans)

G = Graph()
a, b = map(int, input("Введите точки старта и финиша: ").split())
G.findway(a, b)
