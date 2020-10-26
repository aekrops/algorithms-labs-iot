from lab1.algorithm_analysis import AlgoAnalysis


class WaterPump:
    def __init__(self, power_in_watts, brand, liter_per_hour):
        self.power_in_watts = power_in_watts
        self.brand = brand
        self.liter_per_hour = liter_per_hour

    def __str__(self):
        return '\nBrand: ' + self.brand + \
                '\nPower in watts: ' + str(self.power_in_watts) + \
                '\nLiter per hour: ' + str(self.liter_per_hour) + '\n'

    def __del__(self):
        pass


class Sort:
    """ sorting methods """

    @staticmethod
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
                AlgoAnalysis.insertion_sort_swaps_count += 0.5
                iteration -= 1
            else:
                list_of_pumps[iteration + 1] = selected_object
                AlgoAnalysis.insertion_sort_swaps_count += 0.5
        return list_of_pumps

    @staticmethod
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

        for i in range(length // 2 - 1, -1):
            Sort.heapify(list_of_pumps, length, i)

        for i in range(length - 1, 0, -1):
            Sort.swap(i, 0, list_of_pumps)
            Sort.heapify(list_of_pumps, i, 0)
        return list_of_pumps

    @staticmethod
    def swap(index1: int, index2: int, list_of_objects: list):
        list_of_objects[index1], list_of_objects[index2] = list_of_objects[index2], list_of_objects[index1]
        AlgoAnalysis.heapsort_swaps_count += 1

    @staticmethod
    def heapify(list_of_pumps, length, root):
        max_value = root
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        if left_child < length and list_of_pumps[max_value].liter_per_hour < list_of_pumps[left_child].liter_per_hour:
            max_value = left_child
            AlgoAnalysis.heapsort_comparisons_count += 2

        if right_child < length and list_of_pumps[max_value].liter_per_hour < list_of_pumps[right_child].liter_per_hour:
            max_value = right_child
            AlgoAnalysis.heapsort_comparisons_count += 2

        if max_value != root:
            Sort.swap(root, max_value, list_of_pumps)
            Sort.heapify(list_of_pumps, length, max_value)
            AlgoAnalysis.heapsort_comparisons_count += 1

