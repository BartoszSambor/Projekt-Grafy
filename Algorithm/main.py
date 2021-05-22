class Graph:
    def __init__(self):
        self.Verticles = []
        self.VerticlesCount = 0

    def addVerticle(self, start, end, length):
        self.Verticles.append((start, end, length))
        self.VerticlesCount = max(self.VerticlesCount, start + 1, end + 1)

    def __str__(self):
        return self.Verticles.__str__()

    def BellmanFord(self, start):
        distances = [float("inf")] * self.VerticlesCount
        distances[start] = 0

        for i in range(self.VerticlesCount):
            for s, e, d in self.Verticles:
                if distances[e] > distances[s] + d:
                    distances[e] = distances[s] + d

        print(distances)



g = Graph()
g.addVerticle(0,1, 100)
g.addVerticle(0,2, 3)
g.addVerticle(2,1, 4)

print(g)
g.BellmanFord(0)