import importlib

graph_module = importlib.import_module("graph")

while True:
    filename = str.strip(input("Insert path to graph file or type \"exit\" to exit: "))
    if str.lower(filename) == "exit":
        break

    graph = graph_module.Graph()
    errorMessage = graph.load_form_file(filename)
    if errorMessage is not None:
        print(errorMessage)
        continue

    start_index = input("Insert starting index: ")
    try:
        start_index = int(start_index)
    except:
        print("You did not enter a valid integer")
        continue
    if start_index > graph.verticesCount or start_index < 0:
        print("Vertex with this index does not belong to graph")
        continue

    # Executing algorithm and printing results
    result = graph.bellman_ford(start_index)
    print("Input:")
    print(graph)
    print("Result:")
    print(result)
