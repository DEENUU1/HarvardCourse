from tabulate import tabulate
import csv

try:
    with open('regular.csv', newline='') as f:
        reader = csv.reader(f)
        next(reader)
        print(tabulate(reader, headers=['Regular', 'Small', 'Large']))


except FileNotFoundError:
    print('Nie znaleziono takiego pliku')