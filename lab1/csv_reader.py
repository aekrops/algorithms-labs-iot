import csv
from lab1.water_pump import WaterPump


def read_csv_file(file):
    list_of_pump = []
    with open(file, 'r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            # power_in_watts, brand, liter_per_hour
            list_of_pump.append(WaterPump(int(row[0]), row[1], int(row[2])))
    return list_of_pump
