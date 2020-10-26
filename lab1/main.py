from lab1.water_pump import Sort
from lab1.algorithm_analysis import AlgoAnalysis
from lab1.csv_reader import read_csv_file

if __name__ == '__main__':
    water_pumps = read_csv_file("pumps.csv")

    heapsort = Sort.heap_sort(water_pumps)
    print(AlgoAnalysis.result_view('heapsort'))
    heapsort_str = ''
    for item in heapsort:
        heapsort_str += str(item.liter_per_hour) + ' '
    print(heapsort_str)

    insertion_sort = Sort.insertion_sort(water_pumps)
    print(AlgoAnalysis.result_view('insertion_sort'))
    insertion_sort_str = ''
    for item in insertion_sort:
        insertion_sort_str += str(item.power_in_watts) + ' '
    print(insertion_sort_str)


