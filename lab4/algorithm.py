from collections import defaultdict


def read_file(file):
    with open(file, 'r') as f:
        data = f.readlines()
        columns, rows = [int(number) for number in data[0].split()]
        corridor = [str(line).replace("\n", "") for line in data[1:]]
        corridor_of_slabs = [[column for column in corridor[row]] for row in range(rows)]
        return corridor_of_slabs, columns, rows


def check_results(file_in, file_out):
    result = find_number_of_ways(file_in)
    with open(file_out, 'r') as f:
        expected_result = int(f.readline())
    return result == expected_result


def find_number_of_ways(file):
    corridor_of_slabs, columns, rows = read_file(file)
    memoized_path_number = defaultdict(int)
    slabs = [[1] for row in range(rows)]
    for row in range(rows):
        memoized_path_number[corridor_of_slabs[row][0]] += 1
    for column in range(1, columns):
        variations_of_get = {}
        for row in range(rows):
            letter = corridor_of_slabs[row][column]
            if letter is not corridor_of_slabs[row][column - 1]:
                cur_value = slabs[row][column - 1] + memoized_path_number[letter]
            else:
                cur_value = memoized_path_number[letter]
            slabs[row].append(cur_value)
            variations_of_get[letter] = cur_value + variations_of_get.get(letter, 0)
        for letter in variations_of_get:
            memoized_path_number[letter] += variations_of_get[letter]
    return count_number_of_exits(slabs)


def count_number_of_exits(plates):
    if len(plates) > 1:
        return plates[0][-1] + plates[-1][-1]
    else:
        return plates[0][-1]


if __name__ == '__main__':
    print(find_number_of_ways("data/ijones1.in"))
