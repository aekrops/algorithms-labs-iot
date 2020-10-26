from lab1.algorithm_analysis import AlgoAnalysis


def heapify(list_of_pumps, length, root):
    max_value = root
    left_child = 2 * root + 1
    right_child = 2 * root + 2

    if left_child < length and list_of_pumps[max_value].liter_per_hour < list_of_pumps[left_child].liter_per_hour:
        max_value = left_child

    if right_child < length and list_of_pumps[max_value].liter_per_hour < list_of_pumps[right_child].liter_per_hour:
        max_value = right_child
        AlgoAnalysis.heapsort_comparisons_count += 2

    if max_value != root:
        list_of_pumps[root], list_of_pumps[max_value] = list_of_pumps[max_value], list_of_pumps[root]
        AlgoAnalysis.heapsort_comparisons_count += 1
        heapify(list_of_pumps, length, max_value)


def heap_sort(list_of_pumps):
    """
    HEAPSORT
    ASCENDING
    Sorting pumps by volume of water
    :param list_of_pumps: list of water pumps to sort
    COMPLEXITY: O(n*log(n))
        Worst result: O(n^2)
        Best result: O(n*log(n))
        Average result: O(n*log(n))
    """
    length = len(list_of_pumps)

    for i in range(length, - 1, -1):
        heapify(list_of_pumps, length, i)

    for i in range(length - 1, 0, -1):
        AlgoAnalysis.insertion_sort_swaps_count += 1
        list_of_pumps[i], list_of_pumps[0] = list_of_pumps[0], list_of_pumps[i]
        heapify(list_of_pumps, i, 0)
    return list_of_pumps
