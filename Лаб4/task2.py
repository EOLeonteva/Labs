# TODO импортировать необходимые модули
import csv
import json
from collections import OrderedDict

INPUT_FILENAME = "input1.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    # TODO считать содержимое csv файла
    with open(INPUT_FILENAME, mode='r', newline='') as csv_file:
        reader = csv.DictReader(csv_file)
        data = [OrderedDict(row) for row in reader] # конвертирую ряды в список словарей

    with open(OUTPUT_FILENAME, mode='w') as json_file: # TODO Сериализовать в файл с отступами равными 4
        json.dump(data, json_file, indent=4)

if __name__ == '__main__':

    task()     # выполняем для проверки

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")

