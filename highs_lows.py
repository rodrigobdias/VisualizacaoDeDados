import csv

# Obtém as temperaturas máximas do arquivo
filename = 'sitka_weather_07-2014.csv'

with open(filename) as f:
    reader = csv.reader(f)
    header_now = next(reader)

    for index, column_header in enumerate(header_now):
        print(index, column_header)

    highs = []
    for row in reader:
        high = int(row[1])
        highs.append(high)

    print(highs)
