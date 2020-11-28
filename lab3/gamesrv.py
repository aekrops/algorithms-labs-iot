from lab3.graph import Graph
import sys


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
