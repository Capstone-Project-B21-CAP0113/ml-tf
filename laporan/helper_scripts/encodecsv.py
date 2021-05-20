import csv
import os
import string

filepath = os.path.dirname(os.path.abspath(__file__))
filename = os.path.join(filepath, "..", "cleaned_data", "laporan.csv")
targetname = os.path.join(filepath, "..", "cleaned_data", "laporanencoded.csv")

kategorilist = ["perselisihan",
    "infrastruktur",
    "pemerintah",
    "kesehatan",
    "teknologi",
    "administrasi",
    "fasilitas",
    "lingkungan",
    "ketertiban",
    "listrik",
    "bahaya",
    "lainnya",
    "pungli",
    "ilegal",
    "lalulintas",
    "bencana",
    "air",
    "pendidikan",
    "kebersihan",
    "sosial",
    "wisata",
    "sara",
    "pencurian",
    "korupsi",
    "bbm",
    "keuangan"
    ]

rows = []
with open(filename, "r", newline="", encoding="ISO-8859-1") as file:
    reader = csv.reader(file, delimiter=";")
    for row in reader:
        text, label = row
        listoflabel = label.strip().split(",")
        labelencode = [text]
        for kategori in kategorilist:
            if kategori in listoflabel:
                labelencode.append(1)
            else:
                labelencode.append(0)
        rows.append(labelencode)
        

with open(targetname, "w+", newline="", encoding="ISO-8859-1") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(['text'] + kategorilist)
    for row in rows:
        writer.writerow(row)