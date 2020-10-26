from lab1.algorithm_analysis import AlgoAnalysis


def insertion_sort(list_of_pumps):
    """
    INSERTION SORT
    DESCENDING
    Sorting pumps by power in watts
    :param list_of_pumps: list of water pumps to sort
    COMPLEXITY: O(n^2)
        Worst result: O(n^2)
        Best result: O(n)
        Average result: O(n^2)
    """
    length = len(list_of_pumps)
    for obj_position in range(1, length):
        selected_object = list_of_pumps[obj_position]
        iteration = obj_position - 1
        while iteration >= 0 and selected_object.power_in_watts > list_of_pumps[iteration].power_in_watts:
            list_of_pumps[iteration + 1] = list_of_pumps[iteration]
            AlgoAnalysis.insertion_sort_comparisons_count += 2
            AlgoAnalysis.insertion_sort_swaps_count += 1
            iteration -= 1
        else:
            list_of_pumps[iteration + 1] = selected_object
            AlgoAnalysis.insertion_sort_swaps_count += 1
    return list_of_pumps
