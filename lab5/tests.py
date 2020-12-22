import unittest
from lab5.algorithm import check_result


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, check_result([(16, 19)], "The text that I have wrote now", "have"))
        self.assertEqual(True, check_result([(0, 3)], "They wanted juice", "They"))
        self.assertEqual(True, check_result([(16, 17), (43, 44)],
                                            "Some body once told me the world is gonna roll me", "ol"))
        self.assertEqual(True, check_result([(0, 9)], "Aaaaaaaaaabbb", "Aaaaaaaaaa"))
        self.assertEqual(False, check_result([(0, 10)], "Postmodernism is a broad movement that developed "
                                                        "in the mid- to late 20th century across philosophy, "
                                                        "the arts, architecture, and criticism, marking a "
                                                        "departure from modernism.", "copy"))


if __name__ == '__main__':
    unittest.main()
