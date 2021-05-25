from Algorithm import graph as gh

while True:
    # Exit input handling
    filename = str.strip(input("Insert path to graph file or type \"exit\" to exit: "))
    if str.lower(filename) == "exit":
        break
    graph = gh.Graph()
    if not graph.load_form_file(filename):  # Loading graph from file and handling invalid file path
        print("Invalid path to file.")
        continue

    # Index input handling
    start_index = input("Insert starting index: ")
    try:
        start_index = int(start_index)
    except:
        print("You did not enter a valid integer")
        continue

    # Executing algorithm and printing results
    result = graph.bellman_ford(start_index)
    print("Input:")
    print(graph)
    print("Result:")
    print(result)
