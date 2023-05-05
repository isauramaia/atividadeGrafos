# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


from collections import deque

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)
        self.adj_list[v].append(u)

    def bfs(self, s, t):
        visited = [False] * self.V
        queue = deque()
        queue.append(s)
        visited[s] = True
        path = {s: None}

        while queue:
            u = queue.popleft()
            if u == t:
                break

            for v in self.adj_list[u]:
                if not visited[v]:
                    visited[v] = True
                    queue.append(v)
                    path[v] = u

        if t not in path:
            print("Não há caminho entre os vértices.")
        else:
            caminho = []
            while t != None:
                caminho.append(t)
                t = path[t]
            caminho.reverse()
            print("Caminho encontrado: ", caminho)

            class Graph:
                def __init__(self, vertices):
                    self.V = vertices
                    self.adj_list = [[] for _ in range(vertices)]

                def add_edge(self, u, v):
                    self.adj_list[u].append(v)
                    self.adj_list[v].append(u)

                def dfs(self, s, t):
                    visited = [False] * self.V
                    stack = [s]
                    path = {s: None}

                    while stack:
                        u = stack.pop()
                        if not visited[u]:
                            visited[u] = True
                            if u == t:
                                break

                            for v in self.adj_list[u]:
                                if not visited[v]:
                                    stack.append(v)
                                    path[v] = u

                    if t not in path:
                        print("Não há caminho entre os vértices.")
                    else:
                        caminho = []
                        while t != None:
                            caminho.append(t)
                            t = path[t]
                        caminho.reverse()
                        print("Caminho encontrado: ", caminho)

