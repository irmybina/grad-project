# import pandas as pd
# import numpy as np
#
# df = pd.read_csv('output.csv')
#
# print(df.query("name == 'Аршиненко  Игорь  Анатольевич*'"))
#
import csv
def reformat_row(row):
    return "Найден автор: " + row[0] + ",\nУниверситет: " + row[1] + ",\nПубликаций: " + row[2] + ",\nЦитирований: " + row[3] + ",\nИндекс Хирша: " + row[4] + "\n\n"

def find_row(target_value):
    with open('output.csv', 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        answer = ""
        for row in reader:
            if row[0].__contains__(target_value):
                answer += reformat_row(row)
        return answer
    return None


# # Example usage:
# csv_file = 'output.csv'  # Replace 'example.csv' with your CSV file path
# target_value = 'Антонов'
#
#
# found_row = find_row(target_value)
# if found_row:
#     print("Row found:", found_row)
# else:
#     print("Row not found.")


