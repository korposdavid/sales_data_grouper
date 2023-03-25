from collections import defaultdict
import csv

def process_csv(file_path):
    data = defaultdict(int)

    with open(file_path, 'r') as f:
        for line in f:
            try:
                csv_values = line.strip().split(',')
                date_elements = csv_values[0].split('-')
                value = csv_values[1]
                month = date_elements[1]
                year = date_elements[0]
                data[f'{month}-{year}'] += int(value)
            except IndexError:
                print(line)
            except ValueError:
                print(f"Error: Invalid data in line: {line}")

    return dict(data)

file_path = 'multiTimeline10.csv'
results = process_csv(file_path)
print(results)

with open('results.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results.items())