from lab3 import gamesrv
from lab3.graph import Graph
from lab3.gamesrv import dijkstra


# v1, v2 = input().split()
def read_graph(file):
    graph = Graph()
    with open(file, 'r') as file:
        all_data = file.readlines()
        vertices, edges = all_data[0].split()
        clients = map(int, all_data[1].split())
        edges = all_data[2:]
        for edge in edges:
            start_vertex, end_vertex, latency = int(edge[0]), int(edge[2]), int(edge[4])
            graph.add_edge(start_vertex, end_vertex, latency)
        for vertex in edges:
            if vertex[0] not in clients:
                # latency = dijkstra(graph, vertex)
                # print(latency)
                # print(vertex[0])
                pass
if __name__ == '__main__':
    read_graph("data/gamsrv1.in")

