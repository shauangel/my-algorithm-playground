import re
import csv

file = "/Users/angelshau/Downloads/company.txt"

with open(file, "r", encoding="utf-8") as f:
    data = f.readlines()
    f.close()

companies = []

pattern = r'\*\*(.*?)\*\*'
for i in data:
    matches = re.findall(pattern, i)
    if len(matches) > 0:
        companies += matches
filtered = [[i] for i in list(set(companies))]

with open("/Users/angelshau/Downloads/company.csv", "a", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(filtered)



