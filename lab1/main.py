from lab1.algorithm_analysis import AlgoAnalysis
from lab1.csv_reader import read_csv_file
from lab1.algorithms.heap_sort import heap_sort
from lab1.algorithms.insertion_sort import insertion_sort

if __name__ == '__main__':
    file = input("Enter name of csv file in format \"pumps.csv\":  ")
    water_pumps = read_csv_file(file)

    heap = heap_sort(water_pumps)
    print()
    print(AlgoAnalysis.result_view('heap'))
    heapsort_str = ''
    for item in heap:
        heapsort_str += str(item.liter_per_hour) + ' '
    print(heapsort_str)

    insertion_sort = insertion_sort(water_pumps)
    print(AlgoAnalysis.result_view('insertion_sort'))
    insertion_sort_str = ''
    for item in insertion_sort:
        insertion_sort_str += str(item.power_in_watts) + ' '
    print(insertion_sort_str)


