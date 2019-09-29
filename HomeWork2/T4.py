from collections import deque

class Graph:
    def __init__(self):  #Конструктор
        self.G = {}  #Словарь - граф
        self.used = set()  # Множество пройденных вершин

        N = int(input("Число рёбер: "))  # Вводим количество рёбер
        print("Рёбра (начало, конец): ")
        for i in range(N):
            a0, b0 = map(int, input().split())  # Вводим пары чисел - рёбра графа, N штук
            for a, b in (a0, b0), (b0, a0):
                if a in self.G:
                    self.G[a].add(b)
                else:
                    self.G[a] = {b}

    def dfs(self, vertex):  #Функция обхода в глубину
        print(vertex, end=' ')
        self.used.add(vertex)
        for neighbour in self.G[vertex]:
            if neighbour not in self.used:
                self.dfs(neighbour)

    def bfs(self, vertex):  #Функция обхода в ширину
        dist = {}
        dist[vertex] = 0
        queue = deque([vertex])
        while queue:
            tmp = queue.popleft()
            print(tmp, end=' ')
            for neighbour in self.G[tmp]:
                if neighbour not in dist:
                    dist[neighbour] = dist[tmp] + 1
                    queue.append(neighbour)

G = Graph()
a = int(input("Введите точку старта: "))
if a in G.G:
    print("Обход в глубину:")
    G.dfs(a)
    print("\nОбход в ширину:")
    G.bfs(a)
else:
    print("В графе нет такой точки")