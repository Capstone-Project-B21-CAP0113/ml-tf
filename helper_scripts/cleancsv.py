import csv
import os
import string

filepath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(filepath, "..", "raw_data", "laporan.csv")
targetname = os.path.join(filepath, "..", "cleaned_data", "laporan.csv")

rows = []
with open(filename, "r", newline="", encoding="ISO-8859-1") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        text, label = row
        text = text.lower().strip().translate(str.maketrans("", "", string.punctuation))
        label = label.strip().lower()
        if label != "invalid":
            rows.append([text, label])
        

with open(targetname, "w+", newline="", encoding="ISO-8859-1") as file:
    writer = csv.writer(file, delimiter=";")
    for row in rows:
        writer.writerow(row)