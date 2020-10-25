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
        """ sorting pumps by volume"""
        pass

