def find_min_speed_per_hour(piles, hours):
    """

    >>> find_min_speed_per_hour([3, 6, 7, 11], 8)
    4
    >>> find_min_speed_per_hour([30, 11, 23, 4, 20], 5)
    30
    >>> find_min_speed_per_hour([30, 11, 23, 4, 20], 6)
    23
    >>> find_min_speed_per_hour([10, 3], 3)
    5
    >>> find_min_speed_per_hour([3, 7 , 1], 2)
    -1

    :param piles: list of piles with bananas
    :param hours:
    :return:
    """
    min_speed = 1
    max_speed = 0
    for index in range(len(piles)):
        if max_speed < piles[index]:
            max_speed = piles[index]
    if len(piles) == hours:
        return max_speed
    elif len(piles) > hours:
        return -1
    return binary_search(piles, min_speed, max_speed, hours)


def binary_search(piles, min_speed, max_speed, hours):
    """

    :param piles: list of piles with bananas
    :param min_speed:
    :param max_speed:
    :param hours:
    :return:
    """
    average_speed = (min_speed + max_speed) // 2
    while min_speed < max_speed:
        if able_to_eat_in_time(piles, average_speed, hours):
            return binary_search(piles, min_speed, average_speed, hours)
        else:
            return binary_search(piles, average_speed + 1, max_speed, hours)
    return min_speed


def able_to_eat_in_time(piles, speed, hours):
    """


    :param piles:
    :param speed:
    :param hours:
    :return:
    """
    real_hours = 0
    for pile in piles:
        real_hours += pile // speed
        if pile % speed != 0:
            real_hours += 1
    return real_hours <= hours


if __name__ == '__main__':
    import doctest
    doctest.testmod()
