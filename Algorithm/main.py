from Algorithm import graph as gh

graphs = {
    "../Data/gkl.json": 1,
    "../Data/kk.txt": 0
}

for filename, start_index in graphs.items():
    graph = gh.Graph(filename)
    result = graph.bellman_ford(start_index)
    print(filename, ":")
    print(result)



