class WaterPump:
    def __init__(self, power_in_watts, brand, liter_per_hour):
        self.power_in_watts = power_in_watts
        self.brand = brand
        self.liter_per_hour = liter_per_hour

    def __del__(self):
        pass


class Sort:
    """ sorting methods """

    @staticmethod
    def insertion_sort(list_of_pumps):
        """ sorting pumps by power in watts (descending) """
        length = len(list_of_pumps)
        for obj_position in range(1, length):
            selected_object = list_of_pumps[obj_position]
            iteration = obj_position - 1
            while iteration >= 0 and selected_object.power_in_watts > list_of_pumps[iteration].power_in_watts:
                list_of_pumps[iteration + 1] = list_of_pumps[iteration]
                iteration -= 1
            else:
                list_of_pumps[iteration + 1] = selected_object
        return list_of_pumps

    @staticmethod
    def heap_sort(list_of_pumps):
        """ sorting pumps by volume """
        length = len(list_of_pumps)

        for i in range(length // 2 - 1, -1):
            Sort.heapify(list_of_pumps, length, i)

        for i in range(length - 1, 0, -1):
            Sort.swap(i, 0, list_of_pumps)
            Sort.heapify(list_of_pumps, i, 0)
        return list_of_pumps

    @staticmethod
    def swap(elem_index1: int, elem_index2: int, list_of_objects: list):
        temp = list_of_objects[elem_index1]
        list_of_objects[elem_index1] = list_of_objects[elem_index2]
        list_of_objects[elem_index2] = temp

    @staticmethod
    def heapify(list_of_pumps, length, root):
        max_value = root
        left_child = 2 * root + 1
        right_child = 2 * root + 2

        if left_child < length and list_of_pumps[max_value].liter_per_hour < list_of_pumps[left_child].liter_per_hour:
            max_value = left_child

        if right_child < length and list_of_pumps[max_value].liter_per_hour < list_of_pumps[right_child].liter_per_hour:
            max_value = right_child

        if max_value != root:
            Sort.swap(root, max_value, list_of_pumps)
            Sort.heapify(list_of_pumps, length, max_value)
