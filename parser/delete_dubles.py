import csv
from collections import defaultdict

input_path = "yandex_reviews_main_85к.csv"
output_path = "yandex_reviews_cleaned.csv"

unique_rows = {}
with open(input_path, encoding="utf-8") as f:
    reader = csv.reader(f, delimiter=";")
    header = next(reader)
    for row in reader:
        key = tuple(row[:4])
        if key not in unique_rows:
            unique_rows[key] = row

# Запись с экранированием и цитированием
with open(output_path, "w", encoding="utf-8", newline="") as f:
    writer = csv.writer(f, delimiter=";", quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(header)
    writer.writerows(unique_rows.values())
