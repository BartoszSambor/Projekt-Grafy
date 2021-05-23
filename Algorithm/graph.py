import json


class Graph:
    def __init__(self, file_name=None):
        self.edges = []
        self.verticesCount = 0
        if file_name is not None:
            self.load_form_file(file_name)

    def load_form_file(self, file_name):
        with open(file_name) as file:
            data = json.load(file)
            for counter, row in enumerate(data):
                if not row:
                    self.add_vertex_without_edge(counter)
                    continue
                for key, val in row.items():
                    self.add_edge(int(counter), int(key), int(val))

    def add_edge(self, start, end, length):
        self.edges.append((start, end, length))
        self.verticesCount = max(self.verticesCount, start + 1, end + 1)

    def add_vertex_without_edge(self, index):
        self.verticesCount = max(self.verticesCount, index + 1)

    def __str__(self):
        return self.edges.__str__()

    def bellman_ford(self, start):
        distances = [float("inf")] * self.verticesCount
        distances[start] = 0

        for i in range(self.verticesCount):
            for start, end, weight in self.edges:
                if distances[end] > distances[start] + weight:
                    distances[end] = distances[start] + weight

        for start, end, weight in self.edges:
            if distances[end] > distances[start] + weight:
                return "Negative path"

        return {index: dis for (index, dis) in enumerate(distances)}
