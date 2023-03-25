from collections import defaultdict
import csv

def process_csv(file_path):
    data = defaultdict(int)
    products = []

    with open(file_path, 'r') as f:
        for line in f:
            try:
                csv_values = line.strip().split(',')
                values = csv_values[1:]
                date_elements = csv_values[0].split('-')
                month = date_elements[1]
                year = date_elements[0]
                for idx, value in enumerate(values):
                    data[f'{year}-{month}:{products[idx]}'] += int(value)
            except IndexError:
                if line.startswith("Category"):
                    print(line)
                if line.startswith("Week"):
                    products = line.strip().split(',')[1:]
            except ValueError:
                print(f"Error: Invalid data in line: {line}")

    return dict(data)

file_path = 'multiTimeline10.csv'
results = process_csv(file_path)
print(results)

with open('results_by_date.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerows(results.items())