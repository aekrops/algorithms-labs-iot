# ping = (in ms)
from lab3.graph import Graph
import sys


def dijkstra(obj: Graph, start_vertex: int):
    shortest_distances = {vertex: sys.maxsize for vertex in range(1, len(obj.graph) + 1)}
    parent_vertices = {vertex: None for vertex in range(1, len(obj.graph) + 1)}

    shortest_distances[start_vertex] = 0
    available_nodes = obj.vertex_queue
    available_nodes.put((0, start_vertex))
    while not available_nodes.empty():
        parent_vertex = available_nodes.get()[1]
        current_vertex = dict(graph.graph[parent_vertex])
        for child_vertex in current_vertex:
            distance = shortest_distances[parent_vertex] + current_vertex[child_vertex]

            if distance < shortest_distances[child_vertex]:
                shortest_distances[child_vertex] = distance
                parent_vertices[child_vertex] = parent_vertex
                if child_vertex < len(graph.graph.items()):
                    available_nodes.put((distance, child_vertex))
    return shortest_distances


if __name__ == '__main__':
    start = 0
    graph = Graph()
    graph.add_edge(1, 3, 10)
    graph.add_edge(3, 4, 80)
    graph.add_edge(4, 5, 50)
    graph.add_edge(5, 6, 20)
    graph.add_edge(2, 3, 40)
    graph.add_edge(2, 4, 100)

    print(dijkstra(graph, 1))

# [ [ (1, length), (3, length) ],
# [ (3, length), (2, length) ]
# [ () ]
