import csv

# Path to CSV file
file_path = 'example.csv'

# Initialize an empty list to store the data
data = []

# Use the `with` context manager to open the file
with open(file_path, mode='r', encoding='utf-8') as file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(file)

    # Iterate over the lines of the CSV file
    for line in csv_reader:
        # Add each row (a dictionary) to the data list
        data.append(line)

# Display data read from CSV file
for record in data:
    print(data)