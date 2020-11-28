from lab3.graph import Graph
from lab3.gamesrv import min_max_latency


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
