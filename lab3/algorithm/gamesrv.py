from lab3.algorithm.util.graph import Graph
import sys


def create_graph_by_file(file):
    graph = Graph()
    with open(file, 'r') as file:
        data = file.readlines()
        number_of_vertices, number_of_edges = [int(number) for number in data[0].split()]
        clients = [int(number) for number in data[1].split()]
        edges = [list(map(int, edge.split())) for edge in data[2:]]
        for edge in edges:
            graph.add_edge(edge[0], edge[1], edge[2])
        return {"graph": graph, "clients": clients}


def min_max_ping(file):
    data = create_graph_by_file(file)
    graph = data['graph']
    clients = data['clients']
    return min_max_latency(graph, clients)


def read_result(file):
    with open(file, 'r') as file:
        result = int(file.readline())
        return result


def check_result(file_in, file_out):
    data_in = min_max_ping(file_in)
    data_out = read_result(file_out)
    return data_in == data_out


def min_max_latency(obj: Graph, clients: list):
    latencies = {}
    latencies_for_users = {}
    for vertex in obj.graph.keys():
        if vertex not in clients:
            latencies[vertex] = dijkstra(obj, vertex)
            latencies_for_users[vertex] = max([latencies[vertex][client] for client in clients])
    # best server for players
    # optimal_server = min(latencies_for_users, key=latencies_for_users.get)
    return min(latencies_for_users.values())


def dijkstra(obj: Graph, start_vertex: int):
    shortest_distances = {vertex: sys.maxsize for vertex in range(1, len(obj.graph) + 1)}
    parent_vertices = {vertex: None for vertex in range(1, len(obj.graph) + 1)}

    shortest_distances[start_vertex] = 0
    available_nodes = obj.vertex_queue
    available_nodes.put((0, start_vertex))
    while not available_nodes.empty():
        parent_vertex = available_nodes.get()[1]
        child_vertices = obj.graph[parent_vertex]
        for child_vertex in child_vertices:
            distance = shortest_distances[parent_vertex] + child_vertices[child_vertex]
            if distance < shortest_distances[child_vertex]:
                shortest_distances[child_vertex] = distance
                parent_vertices[child_vertex] = parent_vertex
                available_nodes.put((distance, child_vertex))
    return shortest_distances
