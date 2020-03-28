import csv
from pathlib import Path
import os

region_data = []
input_file = csv.DictReader(open("region_data/region_data.csv"))
for row in input_file:
    region_data.append(row)