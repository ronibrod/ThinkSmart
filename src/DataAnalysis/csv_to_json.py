import csv
import json

def csv_to_json(csv_file, json_file):
    # Read data from CSV and convert it to a list of dictionaries
    data = []
    with open(csv_file, 'r', encoding='utf-8') as csvfile:
        csvreader = csv.DictReader(csvfile)
        for row in csvreader:
            data.append(row)

    # Write the data to a JSON file
    with open(json_file, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=4)

# Example usage
csv_to_json('C:/Users/ronib/Desktop/projects/Coffee/src/DataAnalysis/ChartData.csv', 'C:/Users/ronib/Desktop/projects/Coffee/src/DataAnalysis/ChartData.json')
