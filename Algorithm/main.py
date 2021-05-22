class Graph:
    def __init__(self):
        self.edges = []
        self.verticesCount = 0

    def add_edge(self, start, end, length):
        self.edges.append((start, end, length))
        self.verticesCount = max(self.verticesCount, start + 1, end + 1)

    def __str__(self):
        return self.edges.__str__()

    def bellman_ford(self, start):
        distances = [float("inf")] * self.verticesCount
        distances[start] = 0

        for i in range(self.verticesCount):
            for s, e, d in self.edges:
                if distances[e] > distances[s] + d:
                    distances[e] = distances[s] + d

        print(distances)


g = Graph()
g.add_edge(0, 1, 100)
g.add_edge(0, 2, 3)
g.add_edge(2, 1, 4)

print(g)
g.bellman_ford(0)
