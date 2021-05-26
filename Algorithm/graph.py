import json


class Graph:
    def __init__(self):
        self.edges = []
        self.verticesCount = 0

    def __str__(self):
        return self.edges.__str__()

    def load_form_file(self, file_name):
        try:
            file = open(file_name)
        except:
            return "Invalid file path"
        try:
            data = json.load(file)
        except:
            return "Error while parsing JSON"
        for counter, row in enumerate(data):
            if not row:
                self.add_vertex_without_edge(counter)
                continue
            for key, val in row.items():
                self.add_edge(int(counter), int(key), int(val))
        return None

    def add_edge(self, start, end, length):
        self.edges.append((start, end, length))
        self.verticesCount = max(self.verticesCount, start + 1, end + 1)

    def add_vertex_without_edge(self, index):
        self.verticesCount = max(self.verticesCount, index + 1)

    def bellman_ford(self, start):
        distances = [float("inf")] * self.verticesCount
        distances[start] = 0

        for i in range(self.verticesCount):
            for start, end, weight in self.edges:
                if distances[end] > distances[start] + weight:
                    distances[end] = distances[start] + weight

        for start, end, weight in self.edges:  # Checking for negative value loops
            if distances[end] > distances[start] + weight:
                return "Negative path"

        # Returns dictionary where key is vertex index and value is the shortest distance from starting vertex
        return {index: dis for (index, dis) in enumerate(distances)}
