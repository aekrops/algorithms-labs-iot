import timeit


class AlgoAnalysis:

    # counts amount of comparisons
    insertion_sort_comparisons_count, heapsort_comparisons_count = 0, 0

    # counts amount of swaps
    insertion_sort_swaps_count, heapsort_swaps_count = 0, 0

    @staticmethod
    def algorithm_time(algorithm_name: str):
        setup = "from __main__ import " + algorithm_name
        return timeit.timeit(algorithm_name, setup)

    @staticmethod
    def result_view(algorithm_name: str):
        print("Name: " + algorithm_name.capitalize())
        print("Time: " + str(AlgoAnalysis.algorithm_time(algorithm_name)))
        if 'insertion' in algorithm_name:
            print("Amount of comparison operations: " + str(AlgoAnalysis.insertion_sort_comparisons_count))
            print("Amount of swap operations: " + str(AlgoAnalysis.insertion_sort_swaps_count))
        elif 'heap' in algorithm_name:
            print("Amount of comparison operations: " + str(AlgoAnalysis.heapsort_comparisons_count))
            print("Amount of swap operations: " + str(AlgoAnalysis.heapsort_swaps_count))
