import csv

try:
    with open('before.csv', 'r') as file:
        reader = csv.reader(file)

        with open('after.csv', 'w') as new_file:
            writer = csv.writer(new_file)

            next(reader)
            for row in reader:
                column = row[0]

                first, last = column.split(' ')
                new_row = row[:0] + [first, last] + row[0+1:]

                writer.writerow(new_row)

except FileNotFoundError:
    print('Plik nie istnieje')
