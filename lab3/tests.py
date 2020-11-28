import unittest
from lab3.algorithm.util.graph import Graph
from lab3.algorithm.gamesrv import dijkstra, check_result
import os

test1_in = os.path.join(os.path.dirname(__file__), 'data/gamsrv1.in')
test1_out = os.path.join(os.path.dirname(__file__), 'data/gamsrv1.out')
test2_in = os.path.join(os.path.dirname(__file__), 'data/gamsrv2.in')
test2_out = os.path.join(os.path.dirname(__file__), 'data/gamsrv2.out')
test3_in = os.path.join(os.path.dirname(__file__), 'data/gamsrv3.in')
test3_out = os.path.join(os.path.dirname(__file__), 'data/gamsrv3.out')
test4_in = os.path.join(os.path.dirname(__file__), 'data/gamsrv4.in')
test4_out = os.path.join(os.path.dirname(__file__), 'data/gamsrv4.out')


class MyTestCase(unittest.TestCase):
    def test_min_max_ping(self):
        self.assertEqual(True, check_result(test1_in, test1_out))
        self.assertEqual(True, check_result(test2_in, test2_out))
        self.assertEqual(True, check_result(test3_in, test3_out))
        self.assertEqual(True, check_result(test4_in, test4_out))

    def test_dijkstra(self):
        graph1 = Graph()
        graph1.add_edge(1, 4, 7)
        graph1.add_edge(1, 3, 11)
        graph1.add_edge(2, 3, 5)
        graph1.add_edge(3, 4, 10)
        graph1.add_edge(4, 2, 7)

        self.assertEqual({1: 7, 2: 7, 3: 10, 4: 0}, dijkstra(graph1, 4))
        self.assertEqual({1: 0, 2: 14, 3: 11, 4: 7}, dijkstra(graph1, 1))
        self.assertEqual({1: 14, 2: 0, 3: 5, 4: 7}, dijkstra(graph1, 2))

        graph2 = Graph()
        graph2.add_edge(1, 2, 11)
        graph2.add_edge(1, 5, 3)
        graph2.add_edge(1, 4, 5)
        graph2.add_edge(1, 6, 1)
        graph2.add_edge(5, 4, 9)
        graph2.add_edge(6, 3, 7)

        self.assertEqual({1: 1, 2: 12, 3: 7, 4: 6, 5: 4, 6: 0}, dijkstra(graph2, 6))
        self.assertEqual({1: 5, 2: 16, 3: 13, 4: 0, 5: 8, 6: 6}, dijkstra(graph2, 4))
        self.assertEqual({1: 11, 2: 0, 3: 19, 4: 16, 5: 14, 6: 12}, dijkstra(graph2, 2))


if __name__ == '__main__':
    unittest.main()
