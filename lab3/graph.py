from queue import PriorityQueue


class Graph:
    def __init__(self):
        self.graph = {}
        self.vertex_queue = PriorityQueue()

    def __del__(self):
        pass

    def __str__(self):
        return str(self.graph)

    def _add_edge_from_vertices(self, from_vertex: int, to_vertex: int, weight: int):
        if weight < 0:
            raise ValueError("Weight not able to be negative")
        if from_vertex not in self.graph.keys():
            self.graph[from_vertex] = {to_vertex: weight}
        else:
            self.graph[from_vertex][to_vertex] = weight

    def add_edge(self, from_vertex: int, to_vertex: int, weight: int):
        self._add_edge_from_vertices(from_vertex, to_vertex, weight)
        self._add_edge_from_vertices(to_vertex, from_vertex, weight)

