import csv

def remove_nbsp(csv_file):
    # Read the CSV file and remove NBSP characters
    with open(csv_file, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        # rows = [[cell.replace(u'\xa0', ' ') for cell in row] for row in reader]
        # rows = [[cell.replace('  ', ' ') for cell in row] for row in reader]
        rows = [[cell.replace('\n', '') for cell in row] for row in reader]

    # Write the cleaned content back to the same file
    with open(csv_file, 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

# Example usage:
csv_file = 'output.csv'  # Replace 'example.csv' with your CSV file path
remove_nbsp(csv_file)
print("unwanted symbols removed from the CSV file.")